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

import mock
from oslo_utils import importutils
from sdflexutils import exception
from sdflexutils.hpssa import manager as hpssa_manager
from sdflexutils.hpssa import objects as hpssa_objects
from sdflexutils.ipa_hw_manager import hardware_manager
from sdflexutils.storcli import manager as storcli_manager
from sdflexutils.storcli import storcli
from sdflexutils.sum import sum_controller
import testtools

ironic_python_agent = importutils.try_import('ironic_python_agent')


class SDFlexHardwareManagerTestCase(testtools.TestCase):

    def setUp(self):
        self.hardware_manager = hardware_manager.SDFlexHardwareManager()
        super(SDFlexHardwareManagerTestCase, self).setUp()

    def test_get_clean_steps(self):
        self.assertEqual(
            [{'step': 'create_configuration',
              'interface': 'raid',
              'priority': 0,
              'reboot_requested': False},
             {'step': 'delete_configuration',
              'interface': 'raid',
              'priority': 0,
              'reboot_requested': False},
             {'step': 'erase_devices',
              'interface': 'deploy',
              'priority': 0,
              'reboot_requested': False},
             {'step': 'update_firmware_sum',
              'interface': 'management',
              'priority': 0,
              'reboot_requested': False}],
            self.hardware_manager.get_clean_steps("", ""))

    def test_get_deploy_steps(self):
        self.assertEqual(
            [{
                'step': 'apply_configuration',
                'interface': 'raid',
                'priority': 0,
                'reboot_requested': False,
                'argsinfo': (
                    hardware_manager._RAID_APPLY_CONFIGURATION_ARGSINFO),
            },
                {
                'step': 'flash_firmware_sum',
                'interface': 'management',
                'priority': 0,
                'reboot_requested': False,
                'argsinfo': (
                    hardware_manager._FIRMWARE_UPDATE_SUM_ARGSINFO),
            }],
            self.hardware_manager.get_deploy_steps("", ""))

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_create_raid_volumes')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       'delete_configuration')
    def test_apply_configuration_not_delete(self, delete_mock, create_mock):
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
        create_mock.return_value = raid_config
        manager = self.hardware_manager
        ret = manager.apply_configuration({}, {}, raid_config,
                                          delete_existing=False)
        delete_mock.assert_not_called()
        self.assertEqual(raid_config, ret)

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_create_raid_volumes')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       'delete_configuration')
    def test_apply_configuration_delete(self, delete_mock, create_mock):
        raid_config = {
            'logical_disks': [{
                'size_gb': 100,
                'raid_level': 1,
                'physical_disks': [
                    '5I:0:1',
                    '5I:0:2'],
                'controller': 'MSCC SmartRAID controller'
            }]
        }
        create_mock.return_value = raid_config
        manager = self.hardware_manager
        ret = manager.apply_configuration({}, {}, raid_config,
                                          delete_existing=True)
        delete_mock.assert_called()
        self.assertEqual(raid_config, ret)

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_create_raid_volumes')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       'delete_configuration')
    def test_apply_configuration_delete_default(self, delete_mock,
                                                create_mock):
        raid_config = {
            'logical_disks': [{
                'size_gb': 100,
                'raid_level': 1,
                'physical_disks': [
                    '5I:0:1',
                    '5I:0:2'],
                'controller': 'MSCC SmartRAID controller'
            }]
        }
        create_mock.return_value = raid_config
        manager = self.hardware_manager
        ret = manager.apply_configuration({}, {}, raid_config)
        delete_mock.assert_called()
        self.assertEqual(raid_config, ret)

    @mock.patch.object(os.path, 'exists')
    def test_is_ssacli_present(self, os_path_mock):
        manager = self.hardware_manager
        os_path_mock.return_value = True
        ret = manager._is_ssacli_present()
        self.assertEqual(True, ret)

    @mock.patch.object(os.path, 'exists')
    def test_is_ssacli_present_no(self, os_path_mock):
        manager = self.hardware_manager
        os_path_mock.return_value = False
        ret = manager._is_ssacli_present()
        self.assertEqual(False, ret)

    @mock.patch.object(os.path, 'exists')
    def test_is_storcli_present(self, os_path_mock):
        manager = self.hardware_manager
        os_path_mock.return_value = True
        ret = manager._is_storcli_present()
        self.assertEqual(True, ret)

    @mock.patch.object(os.path, 'exists')
    def test_is_storcli_present_no(self, os_path_mock):
        manager = self.hardware_manager
        os_path_mock.return_value = False
        ret = manager._is_storcli_present()
        self.assertEqual(False, ret)

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_present')
    @mock.patch.object(storcli, '_storcli')
    def test_is_storcli_ctrl_present(self, storcli_mock, exist_mock):
        storcli_mock.return_value = "stdout"
        exist_mock.return_value = True
        manager = self.hardware_manager
        ret = manager._is_storcli_ctrl_present()
        self.assertEqual(True, ret)

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_present')
    @mock.patch.object(storcli, '_storcli')
    def test_is_storcli_ctrl_present_exception(self, storcli_mock, exist_mock):
        storcli_mock.side_effect = exception.StorcliOperationError(
            reason='reason')
        exist_mock.return_value = True
        manager = self.hardware_manager
        ret = manager._is_storcli_ctrl_present()
        self.assertEqual(False, ret)

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_present')
    def test_is_storcli_ctrl_not_present(self, exist_mock):
        exist_mock.return_value = False
        manager = self.hardware_manager
        ret = manager._is_storcli_ctrl_present()
        self.assertEqual(False, ret)

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssacli_present')
    @mock.patch.object(hpssa_objects, '_ssacli')
    def test_is_ssa_ctrl_present(self, ssacli_mock, exist_mock):
        ssacli_mock.return_value = ("stdout", "stderr")
        exist_mock.return_value = True
        manager = self.hardware_manager
        ret = manager._is_ssa_ctrl_present()
        self.assertEqual(True, ret)

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssacli_present')
    @mock.patch.object(hpssa_objects, '_ssacli')
    def test_is_ssa_ctrl_present_exception(self, ssacli_mock, exist_mock):
        ssacli_mock.side_effect = exception.HPSSAOperationError(
            reason='reason')
        exist_mock.return_value = True
        manager = self.hardware_manager
        ret = manager._is_ssa_ctrl_present()
        self.assertEqual(False, ret)

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssacli_present')
    def test_is_ssa_ctrl_not_present(self, exist_mock):
        exist_mock.return_value = False
        manager = self.hardware_manager
        ret = manager._is_ssa_ctrl_present()
        self.assertEqual(False, ret)

    def test_create_configuration_no_raid_config(self):
        node = {'target_raid_config': {}}
        manager = self.hardware_manager
        ret = manager.create_configuration(node, {})
        self.assertEqual({}, ret)

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_create_raid_volumes')
    def test_create_configuration_raid_config(self, create_mock):
        target_raid_config = {
            'logical_disks': [{
                'size_gb': 100,
                'raid_level': 1,
                'physical_disks': [
                    '5I:0:1',
                    '5I:0:2'],
                'controller': 'MSCC SmartRAID controller'
            }]
        }
        node = {'target_raid_config': target_raid_config}
        create_mock.return_value = target_raid_config
        manager = self.hardware_manager
        ret = manager.create_configuration(node, {})
        self.assertEqual(target_raid_config, ret)

    @mock.patch.object(hpssa_manager, 'create_configuration')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_ctrl_present')
    def test__create_raid_volumes_invalid_controller(
            self, storcli_ctrl_present, ssa_ctrl_present, hpssa_create_mock):
        ssa_ctrl_present.return_value = True
        storcli_ctrl_present.return_value = True
        raid_config = {
            "logical_disks": [{"size_gb": 100, "raid_level": '0',
                               "controller": 'invalid ctrl',
                               "physical_disks": ['252:0']}]}
        manager = self.hardware_manager
        ret = manager._create_raid_volumes(raid_config)
        self.assertEqual({'logical_disks': []}, ret)

    @mock.patch.object(hpssa_manager, 'create_configuration')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_ctrl_present')
    def test__create_raid_volumes_ssa(self, storcli_ctrl_present,
                                      ssa_ctrl_present, hpssa_create_mock):
        ssa_ctrl_present.return_value = True
        storcli_ctrl_present.return_value = False
        hpssa_create_mock.return_value = 'current-config'
        manager = self.hardware_manager
        target_raid_config = {'foo': 'bar'}
        ret = manager._create_raid_volumes(target_raid_config)
        hpssa_create_mock.assert_called_once_with(raid_config={'foo': 'bar'})
        self.assertEqual('current-config', ret)

    @mock.patch.object(hpssa_manager, 'create_configuration')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_ctrl_present')
    def test__create_raid_volumes_ssa_controller(self, storcli_ctrl_present,
                                                 ssa_ctrl_present,
                                                 hpssa_create_mock):
        ssa_ctrl_present.return_value = True
        storcli_ctrl_present.return_value = False
        hpssa_create_mock.return_value = 'current-config'
        raid_config = {
            "logical_disks": [{"size_gb": 100, "raid_level": '0',
                               "controller": 'MSCC SmartRAID',
                               "physical_disks": ['252:0']}]}
        manager = self.hardware_manager
        ret = manager._create_raid_volumes(raid_config)
        hpssa_create_mock.assert_called_once_with(raid_config=raid_config)
        self.assertEqual('current-config', ret)

    @mock.patch.object(storcli_manager, 'create_configuration')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_ctrl_present')
    def test__create_raid_volumes_storcli(self, storcli_ctrl_present,
                                          ssa_ctrl_present,
                                          storcli_create_mock):
        ssa_ctrl_present.return_value = False
        storcli_ctrl_present.return_value = True
        storcli_create_mock.return_value = 'current-config'
        manager = self.hardware_manager
        target_raid_config = {'foo': 'bar'}
        ret = manager._create_raid_volumes(target_raid_config)
        storcli_create_mock.assert_called_once_with(raid_config={'foo': 'bar'})
        self.assertEqual('current-config', ret)

    @mock.patch.object(hpssa_manager, 'create_configuration')
    @mock.patch.object(storcli_manager, 'create_configuration')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_ctrl_present')
    def test__create_raid_volumes_ssa_storcli(self, storcli_ctrl_present,
                                              ssa_ctrl_present,
                                              storcli_create_mock,
                                              hpssa_create_mock):
        ssa_ctrl_present.return_value = True
        storcli_ctrl_present.return_value = True
        hpssa_create_mock.return_value = {'logical_disks': 'current_config'}
        storcli_create_mock.return_value = {'logical_disks': 'current_config'}
        manager = self.hardware_manager
        target_raid_config = {
            "logical_disks": [
                {"size_gb": 100, "raid_level": '0', "controller": 0,
                 "physical_disks": ['252:0']},
                {"size_gb": 'MAX', "raid_level": '0'},
                {"size_gb": 100, "raid_level": '0',
                 "controller": 'MSCC SmartRAID',
                 "physical_disks": ['252:2']}]}
        ret = manager._create_raid_volumes(target_raid_config)
        storcli_create_mock.assert_called_once_with(raid_config={
            "logical_disks": [{"size_gb": 100, "raid_level": '0',
                               "controller": 0, "physical_disks": ['252:0']}]})
        hpssa_create_mock.assert_called_once_with(raid_config={
            "logical_disks": [{"size_gb": 'MAX', "raid_level": '0'}, {
                "size_gb": 100, "raid_level": '0',
                "controller": 'MSCC SmartRAID', "physical_disks": [
                    '252:2']}]})
        self.assertEqual('current_configcurrent_config', ret['logical_disks'])

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_ctrl_present')
    def test__create_raid_volumes_no_controller(self, storcli_ctrl_present,
                                                ssa_ctrl_present):
        ssa_ctrl_present.return_value = False
        storcli_ctrl_present.return_value = False
        manager = self.hardware_manager
        target_raid_config = {
            "logical_disks": [{"size_gb": 100, "raid_level": '0',
                               "controller": 0, "physical_disks": ['252:0']}]}
        ret = manager._create_raid_volumes(target_raid_config)
        self.assertEqual(ret, None)

    @mock.patch.object(hpssa_manager, 'delete_configuration')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_ctrl_present')
    def test_delete_configuration_ssa(self, storcli_ctrl_present,
                                      ssa_ctrl_present, delete_mock):
        ssa_ctrl_present.return_value = True
        storcli_ctrl_present.return_value = False
        delete_mock.return_value = 'current-config'
        ret = self.hardware_manager.delete_configuration("", "")
        delete_mock.assert_called_once_with()
        self.assertEqual('current-config', ret)

    @mock.patch.object(storcli_manager, 'delete_configuration')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_ctrl_present')
    def test_delete_configuration_storcli(self, storcli_ctrl_present,
                                          ssa_ctrl_present, delete_mock):
        ssa_ctrl_present.return_value = False
        storcli_ctrl_present.return_value = True
        delete_mock.return_value = 'current-config'
        ret = self.hardware_manager.delete_configuration("", "")
        delete_mock.assert_called_once_with()
        self.assertEqual('current-config', ret)

    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_ctrl_present')
    def test_delete_configuration_no_controller(self, storcli_ctrl_present,
                                                ssa_ctrl_present):
        ssa_ctrl_present.return_value = False
        storcli_ctrl_present.return_value = False
        ret = self.hardware_manager.delete_configuration("", "")
        self.assertEqual(None, ret)

    @mock.patch.object(ironic_python_agent.hardware.GenericHardwareManager,
                       'erase_devices')
    @mock.patch.object(hpssa_manager, 'erase_devices')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    def test_erase_devices_ssa(self, ssa_ctrl_present, erase_mock,
                               generic_erase_mock):
        node = {}
        port = {}
        ssa_ctrl_present.return_value = True
        erase_mock.return_value = 'erase_status'
        generic_erase_mock.return_value = {'foo': 'bar'}
        ret = self.hardware_manager.erase_devices(node, port)
        erase_mock.assert_called_once_with()
        generic_erase_mock.assert_called_once_with(node, port)
        self.assertEqual({'Disk Erase Status': 'erase_status', 'foo': 'bar'},
                         ret)

    @mock.patch.object(ironic_python_agent.hardware.GenericHardwareManager,
                       'erase_devices')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    def test_erase_devices_ssa_no_ctrl(self, ssa_ctrl_present,
                                       generic_erase_mock):
        node = {}
        port = {}
        ssa_ctrl_present.return_value = False
        generic_erase_mock.return_value = {'foo': 'bar'}
        ret = self.hardware_manager.erase_devices(node, port)
        generic_erase_mock.assert_called_once_with(node, port)
        self.assertEqual({'foo': 'bar'}, ret)

    @mock.patch.object(ironic_python_agent.hardware.GenericHardwareManager,
                       'erase_devices')
    @mock.patch.object(hpssa_manager, 'erase_devices')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    def test_erase_devices_ssa_not_supported(self, ssa_ctrl_present,
                                             erase_mock, generic_erase_mock):
        node = {}
        port = {}
        ssa_ctrl_present.return_value = True
        value = ("Sanitize erase not supported in the "
                 "available controllers")
        e = exception.HPSSAOperationError(reason=value)
        erase_mock.side_effect = e

        exc = self.assertRaises(exception.HPSSAOperationError,
                                self.hardware_manager.erase_devices,
                                node, port)

        self.assertIn(value, str(exc))

    @mock.patch.object(ironic_python_agent.hardware.GenericHardwareManager,
                       'erase_devices')
    @mock.patch.object(storcli_manager, 'erase_devices')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_ssa_ctrl_present')
    @mock.patch.object(hardware_manager.SDFlexHardwareManager,
                       '_is_storcli_ctrl_present')
    def test_erase_devices_storcli(self, storcli_present, ssa_present,
                                   erase_mock, generic_erase_mock):
        node = {}
        port = {}
        storcli_present.return_value = True
        ssa_present.return_value = False
        erase_mock.return_value = 'Erase Completed'
        generic_erase_mock.return_value = {'foo': 'bar'}
        ret = self.hardware_manager.erase_devices(node, port)
        erase_mock.assert_called_once_with()
        generic_erase_mock.assert_called_once_with(node, port)
        self.assertEqual({'Disk Erase Status': 'Erase Completed',
                          'foo': 'bar'}, ret)

    @mock.patch.object(sum_controller, 'update_firmware')
    def test_update_firmware_sum(self, update_mock):
        update_mock.return_value = "log files"
        url = 'http://1.2.3.4/SPP.iso'
        checksum = '1234567890'
        clean_step = {
            'interface': 'management',
            'step': 'update_firmware_sum',
            'args': {'url': url,
                     'checksum': checksum}}
        node = {'clean_step': clean_step}
        ret = self.hardware_manager.update_firmware_sum(node, "")
        update_mock.assert_called_once_with(node, url, checksum)
        self.assertEqual('log files', ret)

    @mock.patch.object(sum_controller, 'update_firmware')
    def test_flash_firmware_sum(self, update_mock):
        update_mock.return_value = "log files"
        url = 'http://1.2.3.4/SPP.iso'
        checksum = '1234567890'
        node = {'foo': 'bar'}
        ret = self.hardware_manager.flash_firmware_sum(node, "", url, checksum)
        update_mock.assert_called_once_with(node, url, checksum)
        self.assertEqual('log files', ret)
