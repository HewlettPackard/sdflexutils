# Copyright 2014 Hewlett-Packard Development Company, L.P.
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

import mock
from sdflexutils import exception
from sdflexutils.storcli import disk_allocator
from sdflexutils.storcli import manager
from sdflexutils.storcli import storcli
from sdflexutils.tests.unit.storcli import raid_constants
import testtools


class ManagerTestCases(testtools.TestCase):

    @mock.patch.object(storcli, '_storcli', autospec=True)
    def test_has_erase_completed_progress(self, storcli_mock):
        storcli_mock.return_value = (
            raid_constants.C0_EALL_SALL_SHOW_ERASE_IN_PROGRESS)
        ret = manager.has_erase_completed()
        self.assertFalse(ret)

    @mock.patch.object(storcli, '_storcli', autospec=True)
    def test_has_erase_completed_not_in_progress(self, storcli_mock):
        storcli_mock.return_value = (
            raid_constants.C0_EALL_SALL_SHOW_ERASE_NOT_IN_PROGRESS)
        ret = manager.has_erase_completed()
        self.assertTrue(ret)

    @mock.patch.object(storcli, '_storcli', autospec=True)
    def test_has_erase_completed_exception(self, storcli_mock):
        storcli_mock.side_effect = exception.StorcliOperationError(reason='')
        self.assertRaises(exception.StorcliOperationError,
                          manager.has_erase_completed)

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(time, 'sleep')
    @mock.patch.object(manager, 'has_erase_completed')
    def test_erase_devices(self, has_erase_completed_mock,
                           sleep_mock, storcli_mock):
        storcli_mock.side_effect = [
            raid_constants.C0_EALL_SALL_SHOW_ALL,
            'start erase output 1', 'start erase output 2',
            'start erase output 3']
        has_erase_completed_mock.side_effect = [False, True]
        ret = manager.erase_devices()
        self.assertEqual(storcli_mock.call_count, 4)
        storcli_mock.assert_any_call(
            '/c0/e252/s0', 'start', 'erase', 'normal', 'patternA=00000000')
        storcli_mock.assert_any_call(
            '/c0/e252/s1', 'start', 'erase', 'normal', 'patternA=00000000')
        storcli_mock.assert_any_call(
            '/c0/e252/s2', 'start', 'erase', 'normal', 'patternA=00000000')
        self.assertEqual("Erase Completed", ret)
        self.assertTrue(sleep_mock.called)

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(time, 'sleep')
    @mock.patch.object(manager, 'has_erase_completed')
    def test_erase_devices_online_pds(self, has_erase_completed_mock,
                                      sleep_mock, storcli_mock):
        # Out of 4 pds a raid 0 volume is created on pds 0 and 1.
        # Hence disk erase runs only on the remaining pds, namely 2 and 3
        storcli_mock.side_effect = [
            raid_constants.C0_EALL_SALL_SHOW_ALL_ONLINE,
            'start erase output 2', 'start erase output 3']
        has_erase_completed_mock.side_effect = [False, True]
        ret = manager.erase_devices()
        self.assertEqual(storcli_mock.call_count, 3)
        storcli_mock.assert_any_call(
            '/c0/e252/s2', 'start', 'erase', 'normal', 'patternA=00000000')
        self.assertEqual("Erase Completed", ret)
        storcli_mock.assert_any_call(
            '/c0/e252/s3', 'start', 'erase', 'normal', 'patternA=00000000')
        self.assertEqual("Erase Completed", ret)
        self.assertTrue(sleep_mock.called)

    @mock.patch.object(storcli, '_storcli', autospec=True)
    def test_erase_devices_exception(self, storcli_mock):
        storcli_mock.side_effect = exception.StorcliOperationError(reason='')
        self.assertRaises(exception.StorcliOperationError,
                          manager.erase_devices)

    @mock.patch.object(storcli, '_storcli', autospec=True)
    def test__validate_pds_in_controller_invalid(self, storcli_mock):
        logical_disk = {"size_gb": 50, "raid_level": '0',
                        'controller': '0',
                        'physical_disks': ['252:5']}
        storcli_mock.return_value = raid_constants.C0_EALL_SALL_SHOW
        self.assertRaises(exception.InvalidInputError,
                          manager._validate_pds_in_controller,
                          logical_disk)

    @mock.patch.object(storcli, '_storcli', autospec=True)
    def test__validate_pds_in_controller(self, storcli_mock):
        logical_disk = {"size_gb": 50, "raid_level": '0',
                        'controller': '0',
                        'physical_disks': ['252:0']}
        storcli_mock.return_value = raid_constants.C0_EALL_SALL_SHOW
        self.assertEqual(None, manager._validate_pds_in_controller(
            logical_disk))

        logical_disk = {"size_gb": 100, "raid_level": '1',
                        "controller": '0',
                        "physical_disks": ['252:0', '252:1']}
        storcli_mock.return_value = raid_constants.C0_EALL_SALL_SHOW
        self.assertEqual(None, manager._validate_pds_in_controller(
            logical_disk))

        logical_disk = {"size_gb": 60, "raid_level": '5',
                        'controller': '0', 'physical_disks': [
                            '252:0', '252:1', '252:2', '252:3']}
        storcli_mock.return_value = raid_constants.C0_EALL_SALL_SHOW_4_DISKS
        self.assertEqual(None, manager._validate_pds_in_controller(
            logical_disk))

    @mock.patch.object(storcli, '_storcli', autospec=True)
    def test__validate_pds_in_controller_exception(self, storcli_mock):
        logical_disk = {"size_gb": 50, "raid_level": '0',
                        'controller': '0',
                        'physical_disks': ['252:0']}
        storcli_mock.side_effect = exception.StorcliOperationError(reason='')
        self.assertRaises(exception.StorcliOperationError,
                          manager._validate_pds_in_controller,
                          logical_disk)

    def test__create_configuration_validate_invalid_json(self):
        raid_config = {
            'logical_disks': [{'controller': '0'}]
        }
        self.assertRaises(exception.InvalidInputError,
                          manager._create_configuration_validate,
                          raid_config)

    def test__create_configuration_validate_invalid_logical_disks_50(self):
        raid_info = {
            'logical_disks': [
                {'size_gb': 50,
                 'raid_level': '5+0',
                 'controller': '0',
                 'physical_disks': [
                     "252:0", "252:1", "252:2", "252:3",
                     "252:4", "252:5", "252:6", "252:7"]}]}
        msg = ("RAID level '5+0' is currently not supported with HPE 9361-4i"
               " RAID Controller on this platform.")
        ex = self.assertRaises(exception.InvalidInputError,
                               manager._create_configuration_validate,
                               raid_info)
        self.assertEqual(msg, str(ex))

    def test__create_configurationvalidate_invalid_logical_disks_60(self):
        raid_info = {
            'logical_disks': [
                {'size_gb': 50,
                 'raid_level': '6+0',
                 'controller': '0',
                 'physical_disks': [
                     "252:0", "252:1", "252:2", "252:3",
                     "252:4", "252:5", "252:6", "252:7"]}]}
        msg = ("RAID level '6+0' is currently not supported with HPE 9361-4i"
               " RAID Controller on this platform.")
        ex = self.assertRaises(exception.InvalidInputError,
                               manager._create_configuration_validate,
                               raid_info)
        self.assertEqual(msg, str(ex))

    def test_create_configuration_invalid_logical_disks_no_of_pds(self):
        raid_info = {
            'logical_disks': [
                {'size_gb': 50,
                 'raid_level': '0',
                 'number_of_physical_disks': 8,
                 'controller': '0',
                 'physical_disks': [
                     "252:0", "252:1", "252:2", "252:3",
                     "252:4", "252:5", "252:6", "252:7"]}]}
        msg = ("HPE 9361-4i RAID Controller currently supports a maximum "
               "of only 4 physical disks on this platform.")
        ex = self.assertRaises(exception.InvalidInputError,
                               manager._create_configuration_validate,
                               raid_info)
        self.assertEqual(msg, str(ex))

    def test_create_configuration_validate_invalid_no_of_pds_raid_1(self):
        raid_info = {
            'logical_disks': [
                {'size_gb': 50,
                 'raid_level': '1',
                 'number_of_physical_disks': 3,
                 'controller': '0',
                 'physical_disks': [
                     "252:0", "252:1", "252:2"]}]}
        msg = ("RAID 1 can only be created with 2 or 4 physical disks")
        ex = self.assertRaises(exception.InvalidInputError,
                               manager._create_configuration_validate,
                               raid_info)
        self.assertEqual(msg, str(ex))

    def test__change_controller_type_str(self):
        raid_config = {
            'logical_disks': [{'controller': '0'}, {'controller': '1'}]}
        raid_config_int = {
            'logical_disks': [{'controller': 0}, {'controller': 1}]}

        ret = manager._change_controller_type(raid_config_int, str)
        self.assertEqual(ret, raid_config)

    def test__change_controller_type_int(self):
        raid_config = {
            'logical_disks': [{'controller': '0'}, {'controller': '1'}]}
        raid_config_int = {
            'logical_disks': [{'controller': 0}, {'controller': 1}]}

        ret = manager._change_controller_type(raid_config, int)
        self.assertEqual(ret, raid_config_int)

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    @mock.patch.object(manager, '_validate_pds_in_controller')
    def test_create_configuration_with_disk_input(self, validate_pd_mock,
                                                  supported_ctrl_mock,
                                                  storcli_mock):
        raid_info = {"logical_disks": [{"size_gb": 50, "raid_level": '0',
                                        'controller': '0',
                                        'physical_disks': ['252:2']},
                                       {"size_gb": 100, "raid_level": '1',
                                        "controller": '0',
                                        "physical_disks": ['252:0', '252:1']}]}
        supported_ctrl_mock.return_value = [0]
        validate_pd_mock.side_effect = [None, None]
        storcli_mock.side_effect = [
            raid_constants.SHOW,
            raid_constants.C0_VALL_SHOW_ALL_NO_VD,
            raid_constants.CREATE_RAID_SUCCESS,
            raid_constants.C0_VALL_SHOW_ALL_R1_WITH_PD,
            raid_constants.SHOW,
            raid_constants.C0_VALL_SHOW_ALL_R1_WITH_PD,
            raid_constants.CREATE_RAID_SUCCESS,
            raid_constants.C0_VALL_SHOW_ALL_R1_R0_WITH_PD]

        manager.create_configuration(raid_info)

        storcli_mock.assert_any_call("/c0", "add", "vd", "type=raid1",
                                     "size=100gb", "drives=252:0,252:1", "J")
        # Verify that we created the 50GB disk the last.
        storcli_mock.assert_any_call("/c0", "add", "vd", "type=raid0",
                                     "size=50gb", "drives=252:2", "J")

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    @mock.patch.object(manager, '_validate_pds_in_controller')
    def test_create_configuration_with_disk_input_5(self, validate_pd_mock,
                                                    supported_ctrl_mock,
                                                    storcli_mock):
        supported_ctrl_mock.return_value = [0]
        validate_pd_mock.return_value = None
        raid_info = {"logical_disks": [{"size_gb": 60, "raid_level": '5',
                                        'controller': '0', 'physical_disks': [
                                            '252:0', '252:1', '252:2',
                                            '252:3']}]}

        storcli_mock.side_effect = [raid_constants.SHOW,
                                    raid_constants.C0_VALL_SHOW_ALL_NO_VD,
                                    raid_constants.CREATE_RAID_SUCCESS,
                                    raid_constants.C0_VALL_SHOW_ALL_R5_WITH_PD]

        manager.create_configuration(raid_info)

        storcli_mock.assert_any_call("/c0", "add", "vd", "type=raid5",
                                     "size=60gb",
                                     "drives=252:0,252:1,252:2,252:3", "J")

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    @mock.patch.object(manager, '_validate_pds_in_controller')
    def test_create_configuration_with_disk_input_10(self, validate_pd_mock,
                                                     supported_ctrl_mock,
                                                     storcli_mock):
        supported_ctrl_mock.return_value = [0]
        validate_pd_mock.return_value = None
        raid_info = {"logical_disks": [{"size_gb": 100, "raid_level": '1+0',
                                        'controller': '0', 'physical_disks': [
                                            '252:0', '252:1', '252:2',
                                            '252:3']}]}

        storcli_mock.side_effect = [raid_constants.SHOW,
                                    raid_constants.C0_VALL_SHOW_ALL_NO_VD,
                                    raid_constants.CREATE_RAID_SUCCESS,
                                    raid_constants.C0_VALL_SHOW_ALL_R10_WITH_PD
                                    ]

        manager.create_configuration(raid_info)

        storcli_mock.assert_any_call("/c0", "add", "vd", "type=raid10",
                                     "size=100gb",
                                     "drives=252:0,252:1,252:2,252:3",
                                     "pdperarray=2", "J")

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    def test_create_configuration_invalid_logical_disks(self,
                                                        supported_ctrl_mock,
                                                        storcli_mock):
        supported_ctrl_mock.side_effect = [[0], [0], [0]]
        storcli_mock.side_effect = [raid_constants.SHOW]
        raid_info = {}
        self.assertRaises(exception.InvalidInputError,
                          manager.create_configuration,
                          raid_info)

        raid_info = {'logical_disks': [{'foo': 'bar'}]}
        self.assertRaises(exception.InvalidInputError,
                          manager.create_configuration,
                          raid_info)

        raid_info = {'logical_disks': [
                     {'size_gb': 50,
                      'raid_level': '1',
                      'controller': '10',
                      'physical_disks': ["252:10", "252:12"]}]}
        msg = ("Invalid Input: Unable to find controller named '10'. "
               "The available controllers are '0'.")
        ex = self.assertRaises(exception.InvalidInputError,
                               manager.create_configuration,
                               raid_info)
        self.assertEqual(msg, str(ex))

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    @mock.patch.object(disk_allocator, 'allocate_disks')
    @mock.patch.object(manager, '_validate_pds_in_controller')
    def test_create_configuration_without_disk_input_succeeds(
        self, validate_pd_mock, allocate_mock, supported_ctrl_mock,
            storcli_mock):
        raid_info = {"logical_disks": [{"size_gb": 50, "raid_level": '0'},
                                       {"size_gb": 100, "raid_level": '1'}]}
        validate_pd_mock.side_effect = [None, None]
        supported_ctrl_mock.return_value = [0]
        storcli_mock.side_effect = [raid_constants.SHOW,
                                    raid_constants.C0_VALL_SHOW_ALL_NO_VD,
                                    raid_constants.CREATE_RAID_SUCCESS,
                                    raid_constants.C0_VALL_SHOW_ALL_R1_NO_PD,
                                    raid_constants.SHOW,
                                    raid_constants.C0_VALL_SHOW_ALL_R1_NO_PD,
                                    raid_constants.CREATE_RAID_SUCCESS,
                                    raid_constants.C0_VALL_SHOW_ALL_R1_R0_NO_PD
                                    ]
        allocate_mock.side_effect = [{"size_gb": 100,
                                      "raid_level": '1',
                                      "controller": 0,
                                      'physical_disks': ["252:0", "252:1"]},
                                     {"size_gb": 50,
                                      "raid_level": '0',
                                      "controller": 0,
                                      'physical_disks': ["252:3"]}]

        manager.create_configuration(raid_info)

        storcli_mock.assert_any_call("/c0", "add", "vd", "type=raid1",
                                     "size=100gb", "drives=252:0,252:1", "J")
        # Verify that we created the 50GB disk the last.
        storcli_mock.assert_any_call("/c0", "add", "vd", "type=raid0",
                                     "size=50gb", "drives=252:3", "J")

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    def test_create_configuration_without_disk_input_fails_on_disk_type(
            self, supported_ctrl_mock, storcli_mock):
        supported_ctrl_mock.side_effect = [[0], [0]]
        storcli_mock.side_effect = [
            raid_constants.C0_EALL_SALL_SHOW,
            raid_constants.C0_E252_S0_SHOW_ALL_SSD_SATA,
            raid_constants.C0_E252_S1_SHOW_ALL_SSD_SATA,
            raid_constants.C0_E252_S2_SHOW_ALL_SSD_SATA]
        raid_info = {'logical_disks': [{'size_gb': 50,
                                        'raid_level': '0',
                                        'disk_type': 'hdd'}]}
        exc = self.assertRaises(exception.StorcliPhysicalDisksNotFoundError,
                                manager.create_configuration,
                                raid_info)
        self.assertIn("of size 50 GB and raid level 0", str(exc))

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    def test_create_configuration_jbod_enabled(self, supported_ctrl_mock,
                                               storcli_mock):
        supported_ctrl_mock.return_value = []
        storcli_mock.side_effect = [raid_constants.SHOW]

        raid_info = {"logical_disks": [{"size_gb": 50,
                                        "raid_level": '0',
                                        'controller': '0',
                                        'physical_disks': ['252:2']}]}

        msg = ("Invalid Input: Unable to find controller named '0'. "
               "The available controllers are ''.")
        ex = self.assertRaises(exception.InvalidInputError,
                               manager.create_configuration,
                               raid_info)
        self.assertIn(msg, str(ex))

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    @mock.patch.object(disk_allocator, 'allocate_disks')
    @mock.patch.object(manager, '_validate_pds_in_controller')
    def test_create_configuration_max_as_size_gb(
        self, validate_pd_mock, allocate_mock, supported_ctrl_mock,
            storcli_mock):
        supported_ctrl_mock.return_value = [0]
        validate_pd_mock.side_effect = [None, None]
        storcli_mock.side_effect = [
            raid_constants.SHOW,
            raid_constants.C0_VALL_SHOW_ALL_NO_VD,
            raid_constants.CREATE_RAID_SUCCESS,
            raid_constants.C0_VALL_SHOW_ALL_R1_WITH_PD,
            raid_constants.SHOW,
            raid_constants.C0_VALL_SHOW_ALL_R1_WITH_PD,
            raid_constants.CREATE_RAID_SUCCESS,
            raid_constants.C0_VALL_SHOW_ALL_R1_PD_R0_MAX]
        raid_info = {'logical_disks': [{'size_gb': 'MAX',
                                        'raid_level': '0',
                                        'disk_type': 'ssd'},
                                       {'size_gb': 100,
                                        'raid_level': '1',
                                        'disk_type': 'ssd'}]}
        allocate_mock.side_effect = [{"size_gb": 100,
                                      "raid_level": '1',
                                      "controller": 0,
                                      'physical_disks': ["252:0", "252:1"]},
                                     {"size_gb": 100,
                                      "raid_level": '0',
                                      "controller": 0,
                                      'physical_disks': ["252:3"]}]
        raid_info = manager.create_configuration(raid_info)
        storcli_mock.assert_any_call("/c0", "add", "vd", "type=raid1",
                                     "size=100gb", "drives=252:0,252:1", "J")
        # Verify that we created the MAX disk the last.
        storcli_mock.assert_any_call("/c0", "add", "vd", "type=raid0",
                                     "size=100gb", "drives=252:3", "J")

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    def test_delete_configuration(self, supported_ctrl_mock, storcli_mock):
        supported_ctrl_mock.return_value = [0]
        storcli_mock.return_value = raid_constants.C0_VALL_DELETE_FORCE
        manager.delete_configuration()
        self.assertEqual(storcli_mock.call_count, 1)

    @mock.patch.object(storcli, '_storcli', autospec=True)
    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    def test_delete_configuration_no_arrays(self, supported_ctrl_mock,
                                            storcli_mock):
        supported_ctrl_mock.return_value = [0]
        res = "No VDs have been configured"
        storcli_mock.side_effect = exception.StorcliOperationError(res)
        self.assertRaisesRegex(exception.StorcliOperationError,
                               "No VDs have been configured",
                               manager.delete_configuration())

    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    def test_delete_configuration_not_raid(self, supported_ctrl_mock):
        supported_ctrl_mock.return_value = []
        manager.delete_configuration()
        supported_ctrl_mock.assert_called_once()

    @mock.patch.object(storcli, '_storcli', autospec=True)
    def test_delete_configuration_exception(self, storcli_mock):
        storcli_mock.side_effect = exception.StorcliOperationError(reason='')
        self.assertRaises(exception.StorcliOperationError,
                          manager.delete_configuration)
