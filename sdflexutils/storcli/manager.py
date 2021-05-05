# Copyright 2015 Hewlett-Packard Development Company, L.P.
# Copyright 2019-2021 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Hewlett Packard Enterprise made changes in this file.

import json
import re
import time

from sdflexutils.common import manager_utils
from sdflexutils import exception
from sdflexutils import log
from sdflexutils.storcli import disk_allocator
from sdflexutils.storcli import storcli

LOG = log.get_logger(__name__)


def _validate_pds_in_controller(logical_disk):
    """Checks if the physical disks in the controller exist

    This method checks if the physical disks provided by the
    user exist in the said controller.

    :param logical_disk: The logical_disk dictionary from user
        provided raid_config
    :raises exception.InvalidInputError exception, if any of the user
        provided physical disk is not found at the said controller
    """
    controller_id = logical_disk['controller']
    try:
        stdout = storcli._storcli(
            "/c{}/eall/sall".format(controller_id), "show", "J")
    except exception.StorcliOperationError as e:
        raise e
    detected_pd_ids = []
    for detected_pd in json.loads(stdout)['Controllers'][0][
            'Response Data']['Drive Information']:
        detected_pd_ids.append(detected_pd['EID:Slt'])
    for physical_disk in logical_disk['physical_disks']:
        if physical_disk not in detected_pd_ids:
            msg = ("Unable to find physical disk '%(physical_disk)s' "
                   "on '%(controller)s'" %
                   {'physical_disk': physical_disk,
                    'controller': controller_id})
            raise exception.InvalidInputError(msg)


def _create_logical_drive(logical_disk, controller_id, cmd_args):
    """Creates logical drive based on information from create_configuration

    This function creates the logical drive based on the information
    received from create_configuration method.

    :param logical_disk: The logical_disk dictionary from user
        provided raid_config
    :param controller_id: Controller id of the controller at which
        logical volume is to be created
    :param cmd_args: Command line arguments for storcli to create the
        logical volume
    :raises exception.StorcliOperationError, if error occurs during
        logical volume creation.
    """
    if logical_disk['raid_level'] == '1+0':
        cmd_args.append('pdperarray=2')
    cmd_args.append('J')
    cmd = ['/c{}'.format(controller_id), "add", "vd",
           "type=raid{}".format(logical_disk[
               'raid_level'].replace('+', ''))] + cmd_args
    try:
        stdout = storcli._storcli(*cmd)
    except exception.StorcliOperationError as e:
        raise e
    stdout_json = json.loads(stdout)
    if stdout_json['Controllers'][0]['Command Status'][
            'Status'] != 'Success':
        reason = ("Error in creating logical disk with raid_level "
                  "'%(raid_level)s' and size %(size_gb)s GB. "
                  "%(description)s" % {
                      'raid_level': logical_disk['raid_level'],
                      'size_gb': logical_disk['size_gb'],
                      'description': stdout_json['Controllers'][0][
                          'Command Status']['Description']})
        raise exception.StorcliOperationError(reason=reason)


def _change_controller_type(raid_config, type):
    """Typecast the controller values to requested type

    :param raid_config: The dictionary containing the requested
        RAID configuration.
    :param type: Requested type for the typecast
    :returns raid_config: The modified raid_config with typecasted
        controller value.
    """
    for ld in raid_config['logical_disks']:
        if 'controller' in ld.keys():
            ld['controller'] = type(ld['controller'])
    return raid_config


def _create_configuration_validate(raid_config):
    """Validates user provided target RAID configuration.

    This method validates the given RAID configuration.
    :param raid_config: The dictionary containing the requested
        RAID configuration. This data structure should be as follows:
        raid_config = {'logical_disks': [{'raid_level': 1, 'size_gb': 100},
                                         <info-for-logical-disk-2>
                                        ]}
    :raises exception.InvalidInputError, if input is invalid.
    """
    manager_utils.validate(raid_config)
    for ld in raid_config['logical_disks']:
        if ld['raid_level'] == '5+0' or ld['raid_level'] == '6+0':
            msg = ("RAID level '{}' is currently not supported with HPE "
                   "9361-4i RAID Controller on this platform.".format(
                       ld['raid_level']))
            raise exception.InvalidInputError(msg)
        if ld.get('number_of_physical_disks', False) and ld[
                'number_of_physical_disks'] > 4:
            msg = ("HPE 9361-4i RAID Controller currently supports a maximum "
                   "of only 4 physical disks on this platform.")
            raise exception.InvalidInputError(msg)
        if ld['raid_level'] == '1' and ld.get(
            'number_of_physical_disks', False) and ld[
                'number_of_physical_disks'] == 3:
            msg = ("RAID 1 can only be created with 2 or 4 physical disks")
            raise exception.InvalidInputError(msg)


def create_configuration(raid_config):
    """Create a RAID configuration on this server.

    This method creates the given RAID configuration on the
    server based on the input passed.
    :param raid_config: The dictionary containing the requested
        RAID configuration. This data structure should be as follows:
        raid_config = {'logical_disks': [{'raid_level': 1, 'size_gb': 100},
                                         <info-for-logical-disk-2>
                                        ]}
    :returns: the current raid configuration. This is same as raid_config
        with some extra properties like root_device_hint, volume_name,
        controller, physical_disks, etc filled for each logical disk
        after its creation.
    :raises exception.InvalidInputError, if input is invalid.
    :raises exception.StorcliOperationError, if a storcli operation fails
    """

    supported_controllers = disk_allocator.get_supported_controllers()
    _create_configuration_validate(raid_config)
    # converting controller names to integers
    if 'logical_disks' in raid_config.keys():
        raid_config = _change_controller_type(raid_config, int)

    # Make sure we create the large disks first.  This is to avoid the
    # situation that we avoid giving large disks to smaller requests.
    # For example, consider this:
    #   - two logical disks - LD1(50), LD(100)
    #   - have 4 physical disks - PD1(50), PD2(50), PD3(100), PD4(100)
    #
    # In this case, for RAID1 configuration, if we were to consider
    # LD1 first and allocate PD3 and PD4 for it, then allocation would
    # fail. So follow a particular order for allocation.
    #
    # Also make sure we create the MAX logical_disks the last to make sure
    # we allot only the remaining space available.

    logical_disks_sorted = (
        sorted((x for x in raid_config['logical_disks']
                if x['size_gb'] != "MAX"),
               reverse=True,
               key=lambda x: x['size_gb']) +
        [x for x in raid_config['logical_disks'] if x['size_gb'] == "MAX"])

    if any(logical_disk['share_physical_disks']
            for logical_disk in logical_disks_sorted
            if 'share_physical_disks' in logical_disk):
        logical_disks_sorted = manager_utils._sort_shared_logical_disks(
            logical_disks_sorted)

    # A temporary raid_config that contains the logical drives created so far.
    # This helps in identifying newly created logical drives and is used in
    # disk_allocator for physical disks sharing among logical drives.
    temp_raid_config = {'logical_disks': []}

    for logical_disk in logical_disks_sorted:

        if 'physical_disks' not in logical_disk:
            logical_disk = disk_allocator.allocate_disks(
                logical_disk, temp_raid_config)

        controller_id = logical_disk['controller']
        try:
            stdout = storcli._storcli("show", "J")
        except exception.StorcliOperationError as e:
            raise e
        cmd_json = json.loads(stdout)
        number_of_controllers = cmd_json['Controllers'][0]['Response Data'][
            'Number of Controllers']
        ctrl_list = []
        for i in range(number_of_controllers):
            detected_ctrl_number = cmd_json['Controllers'][0][
                'Response Data']['System Overview'][i]['Ctl']
            ctrl_list.append(detected_ctrl_number)

        if controller_id not in ctrl_list or \
                controller_id not in supported_controllers:
            msg = ("Unable to find controller named '%(controller)d'."
                   " The available controllers are '%(ctrl_list)s'." %
                   {'controller': controller_id,
                    'ctrl_list': ', '.join(map(str, supported_controllers))})
            raise exception.InvalidInputError(reason=msg)

        cmd_args = []
        if logical_disk['size_gb'] != "MAX":
            cmd_args.append("size=%sgb" % logical_disk['size_gb'])

        if 'physical_disks' in logical_disk:
            _validate_pds_in_controller(logical_disk)
            phy_drive_ids = ','.join(logical_disk['physical_disks'])
            cmd_args.append("drives=%s" % phy_drive_ids)

        # find list of all existing raid volumes
        # Sample data to be matched
            # "Response Data": {
            #     "/c0/v0": [
            #         {
            #             "DG/VD": "0/0",
            #             "TYPE": "RAID1",
            #             "State": "Optl",
            #             "Access": "RW",
            #             "Consist": "No",
            #             "Cache": "RWBD",
            #             "Cac": "-",
            #             "sCC": "ON",
            #             "Size": "100.0 GB",
            #             "Name": ""
            #         }
            #     ],
            #     "PDs for VD 0": [...],
            #     "VD0 Properties": {...},
            #     "/c0/v1": [...],
            #     ...
            # }
        try:
            stdout = storcli._storcli(
                '/c{}/vall'.format(controller_id), 'show', 'all', 'J')
            stdout_json = json.loads(stdout)
            if stdout_json['Controllers'][controller_id]['Command Status'][
                    'Description'] == 'No VDs have been configured':
                volume_list = []
            else:
                volume_list = [key for key in stdout_json['Controllers'][
                    controller_id]['Response Data'] if re.match('c*/v*', key)]

            _create_logical_drive(logical_disk, controller_id, cmd_args)

            # If successful, update the volume_list.
            stdout = storcli._storcli(
                '/c{}/vall'.format(controller_id), 'show', 'all', 'J')
        except exception.StorcliOperationError as e:
            raise e
        stdout_json = json.loads(stdout)
        new_volume_list = [key for key in stdout_json['Controllers']
                           [0]['Response Data'] if re.match('c*/v*', key)]

        new_volume = list(set(new_volume_list) - set(volume_list))[0]
        # This helps uniquely identifying a logical drive.
        # Used in disk_allocator to share physical drives
        logical_disk['volume_name'] = new_volume
        ld_serial = stdout_json['Controllers'][0]['Response Data'][
            'VD{} Properties'.format(new_volume.split('v')[1])]['SCSI NAA Id']
        logical_disk['root_device_hint'] = {'serial': ld_serial}
        temp_raid_config['logical_disks'].append(logical_disk)

    raid_config = _change_controller_type(raid_config, str)

    return raid_config


def delete_configuration():
    """Delete the RAID configuration on this server

    :raises exception.StorcliOperationError, if a storcli operation error
        occurs except when no logical drives are found
    """
    supported_controllers = disk_allocator.get_supported_controllers()
    for ctrl in supported_controllers:
        try:
            storcli._storcli("/c{}/vall".format(ctrl), "delete", "force")
        except exception.StorcliOperationError as e:
            if "No VDs have been configured" not in str(e):
                raise exception.StorcliOperationError(reason=str(e))
            LOG.info(str(e))


def has_erase_completed():
    """Return erase completion status.

    This method returns the hardware disk erase status.

    :returns: Erase completion status. (True/False)
    :raises exception.StorcliOperationError, if a storcli operation fails
    """
    try:
        stdout = storcli._storcli("/call/eall/sall", "show", "erase", "J")
    except exception.StorcliOperationError as e:
        raise e

    pd_erase_status_dict = json.loads(stdout)
    if any((pd['Status'] != 'Not in progress') for pd in pd_erase_status_dict[
            'Controllers'][0]['Response Data']):
        return False
    else:
        return True


def erase_devices():
    """Erase all the drives on this server.

    This method performs hardware disk erase on all the physical drives
    in this server. This erase cannot be performed on logical drives.

    :raises exception.StorcliOperationError, if a storcli operation error
        is encountered.
    """
    try:
        stdout = storcli._storcli("/call/eall/sall", "show", "all", "J")
        pd_dict = json.loads(stdout)
        pd_list = [x for x in pd_dict['Controllers'][0][
            'Response Data'].keys() if re.match(r'Drive /c\d+/e\d+/s\d+$', x)]
        for pd in pd_list:
            if pd_dict['Controllers'][0]['Response Data'][pd][0][
                    'State'] == 'UGood':
                # TODO(Kartikeya): Secure Erase
                # Secure Erase only runs on Self-Encrypting Drives (SED)
                # Currently Not Tested
                # storcli._storcli('{}'.format(pd[6:]), 'secureerase',
                #                  'force')
                if pd_dict['Controllers'][0]['Response Data'][
                        pd][0]['SED'] == 'N':
                    storcli._storcli('{}'.format(pd[6:]), 'start', 'erase',
                                     'normal', 'patternA=00000000')
        while not has_erase_completed():
            time.sleep(300)
    except exception.StorcliOperationError as e:
        raise e

    return "Erase Completed"
