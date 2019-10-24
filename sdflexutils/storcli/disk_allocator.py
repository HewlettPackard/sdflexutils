# Copyright 2019 Hewlett Packard Enterprise Development LP
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

import json

from sdflexutils.common import constants
from sdflexutils import exception
from sdflexutils.storcli import storcli

FILTER_CRITERIA = ['disk_type', 'interface_type', 'model', 'firmware']


def get_supported_controllers():
    """Finds all controllers with personality RAID

    This method finds all controllers that have personality set as RAID.
    It filters out the controller with personality other than RAID.
    e.g. HBA or JBOD.

    :returns: A list of all RAID supported controllers
    """
    try:
        stdout = storcli._storcli("/call", "show", "personality", "J")
    except exception.StorcliOperationError as e:
        raise e
    ctrl_personality_dict = json.loads(stdout)
    supported_controllers = []
    for ctrl_iter in ctrl_personality_dict['Controllers']:
        if ctrl_iter['Response Data']['Controller Properties'][0][
                'Value'] == "RAID ":
            # append ctrl_id to list of supported_controllers
            supported_controllers.append(
                ctrl_iter['Command Status']['Controller'])
    return supported_controllers


def _get_criteria_matching_disks(logical_disk, physical_drives, controller):
    """Finds the physical drives matching the criteria of logical disk.

    This method finds the physical drives matching the criteria
    of the logical disk passed.

    :param logical_disk: The logical disk dictionary from raid config
    :param physical_drives: The physical drives to consider
    :param controller: Controller id of the controller to which
        physical_drives belong
    :returns: A list of physical drives and their respective sizes which
        match the criteria
    """
    matching_physical_drives = []
    criteria_to_consider = [x for x in FILTER_CRITERIA
                            if x in logical_disk]

    for pd in physical_drives:
        enclosure, slot = pd.split(':')
        pd_str = '/c{}/e{}/s{}'.format(controller, enclosure, slot)
        try:
            stdout = storcli._storcli(pd_str, 'show', 'all', 'J')
        except exception.StorcliOperationError as e:
            raise e
        stdout_json = json.loads(stdout)['Controllers'][0]['Response Data']
        for criteria in criteria_to_consider:
            logical_drive_value = logical_disk.get(criteria)
            if criteria == 'disk_type':
                if (stdout_json['Drive {}'.format(pd_str)][0]['Med'].lower()
                        != logical_drive_value):
                    break
            elif criteria == 'interface_type':
                if (stdout_json['Drive {}'.format(pd_str)][0]['Intf'].lower()
                        != logical_drive_value):
                    break
            elif criteria == 'model':
                if (stdout_json['Drive {}'.format(pd_str)][0]['Model'].lower()
                        != logical_drive_value.lower()):
                    break
            elif criteria == 'firmware':
                if (stdout_json['Drive {} - Detailed Information'.format(
                        pd_str)]['Drive {} Device attributes'.format(pd_str)][
                        'Firmware Revision'].lower() !=
                        logical_drive_value.lower()):
                    break
        else:
            size_gb = (str)(
                stdout_json['Drive {}'.format(pd_str)][0]['Size']).split()[0]
            matching_physical_drives.append([pd, size_gb])

    return matching_physical_drives


def _validate_raid_0(logical_disk, unassigned_pd):
    """Checks if RAID 0 logical drive creation with requested size is possible

    This method finds a list of suitable unassigned physical drives which can
    be used to create a logical volume of requested size

    :param logical_disk: The logical disk dictionary from raid config
    :param unassigned_pd: The list of unassigned physical drives
    :returns: A list of suitable physical drives for logical volume creation
    """
    count = 0
    size = 0
    pd_sort = sorted(unassigned_pd, key=lambda x: float(x[1]))
    while size < logical_disk['size_gb'] and count < len(pd_sort):
        size += float(pd_sort[count][1])
        count += 1
    if size >= logical_disk['size_gb']:
        return pd_sort[:count]
    else:
        return []


def _validate_raid_1(logical_disk, unassigned_pd):
    """Checks if RAID 1 logical drive creation with requested size is possible

    This method finds a list of suitable unassigned physical drives which can
    be used to create a logical volume of requested size

    :param logical_disk: The logical disk dictionary from raid config
    :param unassigned_pd: The list of unassigned physical drives
    :returns: A list of suitable physical drives for logical volume creation
    """
    pd_sort = sorted(unassigned_pd, key=lambda x: float(x[1]))
    count = 0
    for pd in pd_sort[:-1]:
        if float(pd[1]) < logical_disk['size_gb']:
            count += 1
        else:
            return [pd_sort[count], pd_sort[count + 1]]

    if len(pd_sort) == 4 and float(pd_sort[0][1]) + float(
            pd_sort[1][1]) >= logical_disk['size_gb']:
        return pd_sort
    else:
        return []


def _validate_raid_5(logical_disk, unassigned_pd):
    """Checks if RAID 5 logical drive creation with requested size is possible

    This method finds a list of suitable unassigned physical drives which can
    be used to create a logical volume of requested size

    :param logical_disk: The logical disk dictionary from raid config
    :param unassigned_pd: The list of unassigned physical drives
    :returns: A list of suitable physical drives for logical volume creation
    """
    pd_sort = sorted(unassigned_pd, key=lambda x: float(x[1]))
    disk_count = 3
    while disk_count <= len(pd_sort):
        for i in range(len(pd_sort) - disk_count + 1):
            size = 0
            for j in range(disk_count - 1):
                size += float(pd_sort[i + j][1])
            if size >= logical_disk['size_gb']:
                return pd_sort[i:i + disk_count]
        disk_count += 1
    return []


def _validate_raid_6_10(logical_disk, unassigned_pd):
    """Checks if RAID 6/1+0 logical drive creation of requested size possible

    This method finds a list of suitable unassigned physical drives which can
    be used to create a logical volume of requested size

    :param logical_disk: The logical disk dictionary from raid config
    :param unassigned_pd: The list of unassigned physical drives
    :returns: A list of suitable physical drives for logical volume creation
    """
    pd_sort = sorted(unassigned_pd, key=lambda x: float(x[1]))
    if float(pd_sort[0][1]) + float(pd_sort[1][1]) >= logical_disk[
            'size_gb']:
        return pd_sort
    return []


def _validate_disks_size(logical_disk, unassigned_pd):
    """Checks if logical drive creation with requested size is possible

    This method finds a list of suitable unassigned physical drives which can
    be used to create a logical volume of requested size. Only RAID levels 0,
    1, 5, 6 and 1+0 are supported as the max number or physical disks for
    storcli controller in SDFlex is 4.

    :param logical_disk: The logical disk dictionary from raid config
    :param unassigned_pd: The list of unassigned physical drives
    :returns: A list of suitable physical drives for logical volume creation
    """
    no_of_pds = len(unassigned_pd)
    if logical_disk['size_gb'] != 'MAX':
        if no_of_pds >= constants.RAID_LEVEL_MIN_DISKS[
                logical_disk['raid_level']] and logical_disk[
                    'raid_level'] == '0':
            return _validate_raid_0(logical_disk, unassigned_pd)
        if no_of_pds >= constants.RAID_LEVEL_MIN_DISKS[
                logical_disk['raid_level']] and logical_disk[
                    'raid_level'] == '1':
            return _validate_raid_1(logical_disk, unassigned_pd)
        if no_of_pds >= constants.RAID_LEVEL_MIN_DISKS[
                logical_disk['raid_level']] and logical_disk[
                    'raid_level'] == '5':
            return _validate_raid_5(logical_disk, unassigned_pd)
        if no_of_pds >= constants.RAID_LEVEL_MIN_DISKS[
            logical_disk['raid_level']] and (
            logical_disk['raid_level'] == '6' or logical_disk[
                'raid_level'] == '1+0'):
            return _validate_raid_6_10(logical_disk, unassigned_pd)
        return []
    else:
        pd_sort = sorted(
            unassigned_pd, key=lambda x: float(x[1]), reverse=True)
        if len(pd_sort) >= constants.RAID_LEVEL_MIN_DISKS[
                logical_disk['raid_level']]:
            return pd_sort[:no_of_pds]
        return []


def allocate_disks(logical_disk, raid_config):
    """Allocate physical disks to a logical disk.

    This method allocates physical disks to a logical disk based on the
    current state of the server and criteria mentioned in the logical disk.

    :param logical_disk: a dictionary of a logical disk from the RAID
        configuration input to the module.
    :param raid_config: Contains all the logical disks created so far.
    :raises exception.StorcliPhysicalDisksNotFoundError, if cannot find
        physical disks for the request.

    Sample output for stdout = storcli._storcli('/c{}/eall/sall'.format(
                                controller), 'show', 'J'):
        "Drive /c0/e252/s0": [
                    {
                        "EID:Slt": "252:0",
                        "DID": 6,
                        "State": "UGood",
                        "DG": 0,
                        "Size": "111.281 GB",
                        "Intf": "SATA",
                        "Med": "SSD",
                        "SED": "N",
                        "PI": "N",
                        "SeSz": "512B",
                        "Model": "VK0120GEFJE",
                        "Sp": "U",
                        "Type": "-"
                    }
    Sample output from _get_criteria_matching_disks: [['252:0', '111.281']]
    """
    size_gb = logical_disk['size_gb']
    raid_level = logical_disk['raid_level']

    # Try to create a new independent array for this request.
    supported_raid_controllers = get_supported_controllers()

    for controller in supported_raid_controllers:
        try:
            stdout = storcli._storcli(
                '/c{}/eall/sall'.format(controller), 'show', 'J')
        except exception.StorcliOperationError as e:
            raise e
        pd_list = json.loads(
            stdout)['Controllers'][0]['Response Data']['Drive Information']
        unassigned_physical_drives = []

        for pd in pd_list:
            if pd['DG'] == '-' and pd['State'] == 'UGood':
                unassigned_physical_drives.append(pd['EID:Slt'])

        physical_drives = _get_criteria_matching_disks(
            logical_disk, unassigned_physical_drives, controller)

        physical_drives = _validate_disks_size(logical_disk, physical_drives)
        if len(physical_drives):
            physical_drives = [x[0] for x in physical_drives]
            logical_disk['controller'] = controller
            logical_disk['physical_disks'] = physical_drives
            return logical_disk

    # Check if we can get shared physical drives
    if logical_disk.get('share_physical_disks', False):
        # Find other lds that are sharable and have the same raid level
        for ld in raid_config['logical_disks']:
            if ld.get('share_physical_disks', False) and ld[
                    'raid_level'] == logical_disk['raid_level']:
                # Get controller freespace
                stdout = storcli._storcli('/c{}'.format(ld['controller']),
                                          'show', 'freespace', 'J')
                stdout_json = json.loads(stdout)
                # Get freespace for the current ld
                for drive in stdout_json['Controllers'][0][
                        'Response Data']['Response Data'][
                            'FREE SPACE DETAILS']:
                    if ld.get('volume_name') == '/c{}/v{}'.format(
                            controller, drive['DG']):
                        if size_gb == 'MAX' or size_gb < int(float(
                                drive['Size'].split()[0])):
                            # Check if all criterias for pds are matched
                            matching_pds_with_size = (
                                _get_criteria_matching_disks(
                                    logical_disk,
                                    ld.get('physical_disks'), controller))
                            matching_pds = [x[0] for x in
                                            matching_pds_with_size]
                            if matching_pds == ld.get('physical_disks'):
                                logical_disk[
                                    'physical_disks'] = matching_pds
                                logical_disk['controller'] = ld['controller']
                                # If size is MAX use all freespace
                                if size_gb == 'MAX':
                                    logical_disk['size_gb'] = int(float(
                                        drive['Size'].split()[0]))
                                return logical_disk

    # We checked for both options and couldn't get any physical disks.
    raise exception.StorcliPhysicalDisksNotFoundError(
        size_gb=size_gb, raid_level=raid_level)
