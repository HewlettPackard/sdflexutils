# Copyright 2015 Hewlett-Packard Development Company, L.P.
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
#
# Hewlett Packard Enterprise made changes in this file.

import time

from sdflexutils.common import manager_utils
from sdflexutils import exception
from sdflexutils.hpssa import disk_allocator
from sdflexutils.hpssa import objects


def _update_physical_disk_details(raid_config, server):
    """Adds the physical disk details to the RAID configuration passed."""
    raid_config['physical_disks'] = []
    physical_drives = server.get_physical_drives()
    for physical_drive in physical_drives:
        physical_drive_dict = physical_drive.get_physical_drive_dict()
        raid_config['physical_disks'].append(physical_drive_dict)


def _select_controllers_by(server, select_condition, msg):
    """Filters out the hpssa controllers based on the condition.

    This method updates the server with only the controller which satisfies
    the condition. The controllers which doesn't satisfies the selection
    condition will be removed from the list.

    :param server: The object containing all the supported hpssa controllers
        details.
    :param select_condition: A lambda function to select the controllers based
        on requirement.
    :param msg: A String which describes the controller selection.
    :raises exception.HPSSAOperationError, if all the controller are in HBA
        mode.
    """
    all_controllers = server.controllers
    supported_controllers = [c for c in all_controllers if select_condition(c)]

    if not supported_controllers:
        reason = ("None of the available SSA controllers %(controllers)s "
                  "have %(msg)s"
                  % {'controllers': ', '.join([c.id for c in all_controllers]),
                     'msg': msg})
        raise exception.HPSSAOperationError(reason=reason)

    server.controllers = supported_controllers


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
    :raises exception.HPSSAOperationError, if all the controllers are in HBA
        mode.
    """
    server = objects.Server()

    select_controllers = lambda x: not x.properties.get('HBA Mode Enabled',
                                                        False)
    _select_controllers_by(server, select_controllers, 'RAID enabled')

    manager_utils.validate(raid_config)

    # Make sure we create the large disks first.  This is avoid the
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

    # We figure out the new disk created by recording the wwns
    # before and after the create, and then figuring out the
    # newly found wwn from it.
    wwns_before_create = set([x.wwn for x in
                              server.get_logical_drives()])

    for logical_disk in logical_disks_sorted:

        if 'physical_disks' not in logical_disk:
            disk_allocator.allocate_disks(logical_disk, server,
                                          raid_config)

        controller_id = logical_disk['controller']

        controller = server.get_controller_by_id(controller_id)
        if not controller:
            msg = ("Unable to find controller named '%(controller)s'."
                   " The available controllers are '%(ctrl_list)s'." %
                   {'controller': controller_id,
                    'ctrl_list': ', '.join(
                        [c.id for c in server.controllers])})
            raise exception.InvalidInputError(reason=msg)

        if 'physical_disks' in logical_disk:
            for physical_disk in logical_disk['physical_disks']:
                disk_obj = controller.get_physical_drive_by_id(physical_disk)
                if not disk_obj:
                    msg = ("Unable to find physical disk '%(physical_disk)s' "
                           "on '%(controller)s'" %
                           {'physical_disk': physical_disk,
                            'controller': controller_id})
                    raise exception.InvalidInputError(msg)

        controller.create_logical_drive(logical_disk)

        # Now find the new logical drive created.
        server.refresh()
        wwns_after_create = set([x.wwn for x in
                                 server.get_logical_drives()])

        new_wwn = wwns_after_create - wwns_before_create

        if not new_wwn:
            reason = ("Newly created logical disk with raid_level "
                      "'%(raid_level)s' and size %(size_gb)s GB not "
                      "found." % {'raid_level': logical_disk['raid_level'],
                                  'size_gb': logical_disk['size_gb']})
            raise exception.HPSSAOperationError(reason=reason)

        new_logical_disk = server.get_logical_drive_by_wwn(new_wwn.pop())
        new_log_drive_properties = new_logical_disk.get_logical_drive_dict()
        logical_disk.update(new_log_drive_properties)

        wwns_before_create = wwns_after_create.copy()

    _update_physical_disk_details(raid_config, server)
    return raid_config


def delete_configuration():
    """Delete a RAID configuration on this server.

    :returns: the current RAID configuration after deleting all
        the logical disks.
    """
    server = objects.Server()

    select_controllers = lambda x: not x.properties.get('HBA Mode Enabled',
                                                        False)
    _select_controllers_by(server, select_controllers, 'RAID enabled')

    for controller in server.controllers:
        # Trigger delete only if there is some RAID array, otherwise
        # hpssacli/ssacli will fail saying "no logical drives found.".
        if controller.raid_arrays:
            controller.delete_all_logical_drives()
    return get_configuration()


def get_configuration():
    """Get the current RAID configuration.

    Get the RAID configuration from the server and return it
    as a dictionary.

    :returns: A dictionary of the below format.
        raid_config = {
            'logical_disks': [{
                'size_gb': 100,
                'raid_level': 1,
                'physical_disks': [
                    '5I:0:1',
                    '5I:0:2'],
                'controller': 'Smart array controller'
                },
            ]
        }
    """
    server = objects.Server()
    logical_drives = server.get_logical_drives()
    raid_config = {}
    raid_config['logical_disks'] = []

    for logical_drive in logical_drives:
        logical_drive_dict = logical_drive.get_logical_drive_dict()
        raid_config['logical_disks'].append(logical_drive_dict)

    _update_physical_disk_details(raid_config, server)
    return raid_config


def has_erase_completed():
    server = objects.Server()
    drives = server.get_physical_drives()
    if any((drive.erase_status == 'Erase In Progress')
           for drive in drives):
        return False
    else:
        return True


def erase_devices():
    """Erase all the drives on this server.

    This method performs sanitize erase on all the supported physical drives
    in this server. This erase cannot be performed on logical drives.

    :returns: a dictionary of controllers with drives and the erase status.
    :raises exception.HPSSAException, if none of the drives support
        sanitize erase.
    """
    server = objects.Server()

    for controller in server.controllers:
        drives = [x for x in controller.unassigned_physical_drives
                  if (x.get_physical_drive_dict().get('erase_status', '')
                      == 'OK')]
        if drives:
            controller.erase_devices(drives)

    while not has_erase_completed():
        time.sleep(300)

    server.refresh()

    status = {}
    for controller in server.controllers:
        drive_status = {x.id: x.erase_status
                        for x in controller.unassigned_physical_drives}
        sanitize_supported = controller.properties.get(
            'Sanitize Erase Supported', 'False')
        if sanitize_supported == 'False':
            msg = ("Drives overwritten with zeros because sanitize erase "
                   "is not supported on the controller.")
        else:
            msg = ("Sanitize Erase performed on the disks attached to "
                   "the controller.")

        drive_status.update({'Summary': msg})
        status[controller.id] = drive_status

    return status
