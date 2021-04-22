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

import os

from ironic_python_agent import hardware
from sdflexutils import exception
from sdflexutils.hpssa import manager as hpssa_manager
from sdflexutils.hpssa import objects as hpssa_objects
from sdflexutils import log
from sdflexutils.storcli import manager as storcli_manager
from sdflexutils.storcli import storcli
from sdflexutils.sum import sum_controller

LOG = log.get_logger(__name__)

_RAID_APPLY_CONFIGURATION_ARGSINFO = {
    "raid_config": {
        "description": "The RAID configuration to apply.",
        "required": True,
    },
    "delete_existing": {
        "description": (
            "Setting this to 'True' indicates to delete existing RAID "
            "configuration prior to creating the new configuration. "
            "Default value is 'True'."
        ),
        "required": False,
    }
}

_FIRMWARE_UPDATE_SUM_ARGSINFO = {
    'url': {
        'description': (
            "The image location for HPE Superdome Flex I/O Service Pack ISO."
        ),
        'required': True,
    },
    'checksum': {
        'description': (
            "The md5 checksum of the SPP image file."
        ),
        'required': True,
    }
}


class SDFlexHardwareManager(hardware.GenericHardwareManager):

    HARDWARE_MANAGER_VERSION = "3"

    def get_clean_steps(self, node, ports):
        """Return the clean steps supported by this hardware manager.

        This method returns the clean steps that are supported by
        sdflex hardware manager.  This method is invoked on every
        hardware manager by Ironic Python Agent to give this information
        back to Ironic.

        :param node: A dictionary of the node object
        :param ports: A list of dictionaries containing information of ports
            for the node
        :returns: A list of dictionaries, each item containing the step name,
            interface and priority for the clean step.
        """
        return [
            {
                'step': 'create_configuration',
                'interface': 'raid',
                'priority': 0,
                'reboot_requested': False
            },
            {
                'step': 'delete_configuration',
                'interface': 'raid',
                'priority': 0,
                'reboot_requested': False
            },
            {
                'step': 'erase_devices',
                'interface': 'deploy',
                'priority': 0,
                'reboot_requested': False
            },
            {
                'step': 'update_firmware_sum',
                'interface': 'management',
                'priority': 0,
                'reboot_requested': False
            }
        ]

    def get_deploy_steps(self, node, ports):
        """Return the deploy steps supported by this hardware manager.

        This method returns the deploy steps that are supported by
        proliant hardware manager.  This method is invoked on every
        hardware manager by Ironic Python Agent to give this information
        back to Ironic.

        :param node: A dictionary of the node object
        :param ports: A list of dictionaries containing information of ports
            for the node
        :returns: A list of dictionaries, each item containing the step name,
            interface, priority, reboot_requested and
            argsinfo for the deploy step.
        """
        return [
            {
                'step': 'apply_configuration',
                'interface': 'raid',
                'priority': 0,
                'reboot_requested': False,
                'argsinfo': _RAID_APPLY_CONFIGURATION_ARGSINFO,
            },
            {
                'step': 'flash_firmware_sum',
                'interface': 'management',
                'priority': 0,
                'reboot_requested': False,
                'argsinfo': _FIRMWARE_UPDATE_SUM_ARGSINFO,
            }
        ]

    def evaluate_hardware_support(cls):
        return hardware.HardwareSupport.SERVICE_PROVIDER

    def apply_configuration(self, node, ports, raid_config,
                            delete_existing=True):
        """Apply RAID configuration.

        :param node: A dictionary of the node object.
        :param ports: A list of dictionaries containing information
                      of ports for the node.
        :param raid_config: The configuration to apply.
        :param delete_existing: Whether to delete the existing configuration.
        :returns: The current RAID configuration of the below format.
            raid_config = {
                'logical_disks': [{
                    'size_gb': 100,
                    'raid_level': 1,
                    'physical_disks': [
                        '5I:0:1',
                        '5I:0:2'],
                    'controller': 'MSCC SmartRAID controller'
                    },
                ]
            }
        """
        if delete_existing:
            self.delete_configuration(node, ports)
        LOG.debug("Creating raid with configuration %(raid_config)s",
                  {'raid_config': raid_config})
        return self._create_raid_volumes(raid_config)

    def _is_ssacli_present(self):
        if os.path.exists("/usr/sbin/ssacli"):
            return True
        else:
            return False

    def _is_storcli_present(self):
        if os.path.exists("/opt/MegaRAID/storcli/"):
            return True
        else:
            return False

    def _is_ssa_ctrl_present(self):
        try:
            if self._is_ssacli_present():
                hpssa_objects._ssacli('ctrl', 'all', 'show', 'config')
            else:
                return False
        except exception.HPSSAOperationError:
            return False
        return True

    def _is_storcli_ctrl_present(self):
        try:
            if self._is_storcli_present():
                storcli._storcli('/call', 'show', 'J')
            else:
                return False
        except exception.StorcliOperationError:
            return False
        return True

    def _create_raid_volumes(self, target_raid_config):
        """Utility function that creates RAID.

        This method separates out SSA and Storcli RAID volumes from
        target_raid_config and creates them on respective controllers.

        :param target_raid_config: The RAID configuration requested.
        :returns: The current RAID configuration of the below format.
            raid_config = {
                'logical_disks': [{
                    'size_gb': 100,
                    'raid_level': 1,
                    'physical_disks': [
                        '5I:0:1',
                        '5I:0:2'],
                    'controller': 'MSCC SmartRAID controller'
                    },
                ]
            }
        """
        # Check if SSA controller is present
        if self._is_ssa_ctrl_present():
            # Check if storcli controller is present
            if not self._is_storcli_ctrl_present():
                # Only SSA controller is present in the system
                return hpssa_manager.create_configuration(
                    raid_config=target_raid_config)
            else:
                # Both SSA and storcli controllers are present
                storcli_raid_config = {}
                storcli_raid_config['logical_disks'] = []
                hpssa_raid_config = {}
                hpssa_raid_config['logical_disks'] = []

                for ld in target_raid_config['logical_disks']:
                    # Check if user has specified controller details
                    if 'controller' in ld.keys():
                        try:
                            # If controller specified is an integer,
                            # use storcli controller
                            int(ld['controller'])
                            storcli_raid_config['logical_disks'].append(ld)
                        except ValueError:
                            # The user specified controller is not a storcli
                            # controller. Check if it is an SSA controller
                            # All SSA controllers for SDFlex have 'SmartRAID'
                            # in their ids.
                            if 'SmartRAID' in ld['controller']:
                                hpssa_raid_config['logical_disks'].append(ld)
                    else:
                        # If no controller information is specified,
                        # default to SSA controller
                        hpssa_raid_config['logical_disks'].append(ld)

                # Create all SSA controller logical volumes
                if hpssa_raid_config['logical_disks']:
                    hpssa_raid_config = hpssa_manager.create_configuration(
                        raid_config=hpssa_raid_config)
                # Create all storcli controller logical volumes
                if storcli_raid_config['logical_disks']:
                    storcli_raid_config = storcli_manager.create_configuration(
                        raid_config=storcli_raid_config)
                ret = {}
                ret['logical_disks'] = hpssa_raid_config[
                    'logical_disks'] + storcli_raid_config['logical_disks']
                return ret
        # Check if storcli controller is present
        if self._is_storcli_ctrl_present():
            # Only storli controller is present in the system
            return storcli_manager.create_configuration(
                raid_config=target_raid_config)

    def create_configuration(self, node, ports):
        """Create RAID configuration on the bare metal.

        This method creates the desired RAID configuration as read from
        node['target_raid_config'].

        :param node: A dictionary of the node object
        :param ports: A list of dictionaries containing information of ports
            for the node
        :returns: The current RAID configuration of the below format.
            raid_config = {
                'logical_disks': [{
                    'size_gb': 100,
                    'raid_level': 1,
                    'physical_disks': [
                        '5I:0:1',
                        '5I:0:2'],
                    'controller': 'MSCC SmartRAID controller'
                    },
                ]
            }
        """
        target_raid_config = node.get('target_raid_config', {}).copy()
        if not target_raid_config:
            LOG.debug('No target_raid_config found')
            return {}
        LOG.debug("Creating raid with configuration %(raid_config)s",
                  {'raid_config': target_raid_config})
        return self._create_raid_volumes(target_raid_config)

    def delete_configuration(self, node, ports):
        """Deletes RAID configuration on the bare metal.

        This method deletes all the RAID disks on the bare metal.
        :param node: A dictionary of the node object
        :param ports: A list of dictionaries containing information of ports
            for the node
        """
        if self._is_ssa_ctrl_present():
            return hpssa_manager.delete_configuration()
        if self._is_storcli_ctrl_present():
            return storcli_manager.delete_configuration()

    def erase_devices(self, node, port):
        """Erase the drives on the bare metal.

        This method erase all the drives which supports sanitize and the drives
        which are not part of any logical volume on the bare metal. It calls
        generic erase method after the success of Sanitize disk erase.
        :param node: A dictionary of the node object.
        :param port: A list of dictionaries containing information of ports
            for the node.
        :raises exception.HPSSAOperationError, if there is a failure on the
            erase operation on the controllers.
        :returns: The dictionary of controllers with the drives and erase
            status for each drive.
        """
        result = {}
        if self._is_ssa_ctrl_present():
            result['Disk Erase Status'] = hpssa_manager.erase_devices()
        if self._is_storcli_ctrl_present():
            result['Disk Erase Status'] = storcli_manager.erase_devices()

        result.update(super(SDFlexHardwareManager,
                            self).erase_devices(node, port))
        return result

    def update_firmware_sum(self, node, port):
        """Performs SUM based firmware update on the bare metal node.

        This method performs firmware update on all or some of the firmware
        components on the bare metal node.

        :returns: A string with return code and the statistics of
            updated/failed components.
        :raises: SUMOperationError, when the SUM based firmware update
            operation on the node fails.
        """
        url = node['clean_step']['args'].get('url')
        checksum = node['clean_step']['args'].get('checksum')
        return sum_controller.update_firmware(node, url, checksum)

    def flash_firmware_sum(self, node, port, url, checksum):
        """Performs SUM based I/O firmware update on the bare metal node.

        This method performs firmware update on all the I/O firmware
        components on the bare metal node.
        :param node: A dictionary of the node object.
        :param port: A list of dictionaries containing information of ports
            for the node.
        :param url: URL for the HPE Superdome Flex I/O Service Pack ISO.
        :param checksum: sha256 checksum of the HPE Superdome Flex
             I/O Service Pack ISO to verify the image.
        :returns: A string with return code and the statistics of
            updated/failed components.
        :raises: SUMOperationError, when the SUM based firmware update
            operation on the node fails.
        """
        LOG.debug("Flashing firmware from %(url)s", {'url': url})
        return sum_controller.update_firmware(node, url, checksum)
