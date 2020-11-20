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
from sdflexutils.hpssa import manager
from sdflexutils.hpssa import objects
from sdflexutils.tests.unit.hpssa import raid_constants
import testtools


@mock.patch.object(objects.Server, '_get_all_details')
class ManagerTestCases(testtools.TestCase):

    def _test_create_configuration_with_disk_input(self,
                                                   controller_exec_cmd_mock,
                                                   get_all_details_mock):
        ld1 = {'size_gb': 50,
               'raid_level': '1',
               'controller': 'MSCC SmartRAID 3154-8e in Slot 2085',
               'physical_disks': ['CN1:1:4',
                                  'CN1:1:5']}
        ld2 = {'size_gb': 100,
               'raid_level': '5',
               'controller': 'MSCC SmartRAID 3154-8e in Slot 2085',
               'physical_disks': ['CN1:1:1',
                                  'CN1:1:2',
                                  'CN1:1:3']}

        raid_info = {'logical_disks': [ld1, ld2]}

        current_config = manager.create_configuration(raid_info)

        ld1_drives = 'CN1:1:4,CN1:1:5'
        ld2_drives = 'CN1:1:1,CN1:1:2,CN1:1:3'
        controller_exec_cmd_mock.assert_any_call("create",
                                                 "type=logicaldrive",
                                                 "drives=%s" % ld2_drives,
                                                 "raid=5",
                                                 "size=%d" % (100*1024),
                                                 process_input='y')
        # Verify that we created the 50GB disk the last.
        controller_exec_cmd_mock.assert_called_with("create",
                                                    "type=logicaldrive",
                                                    "drives=%s" % ld1_drives,
                                                    "raid=1",
                                                    "size=%d" % (50*1024),
                                                    process_input='y')

        ld1_ret = [x for x in current_config['logical_disks']
                   if x['raid_level'] == '1'][0]
        ld2_ret = [x for x in current_config['logical_disks']
                   if x['raid_level'] == '5'][0]

        self.assertIsNotNone(ld1_ret['root_device_hint']['wwn'])
        self.assertIsNotNone(ld2_ret['root_device_hint']['wwn'])
        # self.assertIsNotNone(ld1_ret['volume_name'])
        # self.assertIsNotNone(ld2_ret['volume_name'])

        # Assert physical disk info
        pds_active = [x['id'] for x in current_config['physical_disks']
                      if x['status'] == 'active']
        pds_ready = [x['id'] for x in current_config['physical_disks']
                     if x['status'] == 'ready']
        pds_active_expected = ['CN1:1:5', 'CN1:1:4', 'CN1:1:3',
                               'CN1:1:1', 'CN1:1:2']
        pds_ready_expected = ['CN1:1:11', 'CN1:1:12']
        self.assertEqual(sorted(pds_active_expected), sorted(pds_active))
        self.assertEqual(sorted(pds_ready_expected), sorted(pds_ready))

    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_create_configuration_with_disk_input_create_succeeds(
            self, controller_exec_cmd_mock, get_all_details_mock):
        no_drives = raid_constants.HPSSA_NO_DRIVES
        one_drive = raid_constants.HPSSA_ONE_DRIVE_100GB_RAID_5
        two_drives = raid_constants.HPSSA_TWO_DRIVES_100GB_RAID5_50GB_RAID1
        get_all_details_mock.side_effect = [no_drives, one_drive, two_drives]
        self._test_create_configuration_with_disk_input(
            controller_exec_cmd_mock, get_all_details_mock)

    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_create_configuration_with_disk_input_create_fails(
            self, controller_exec_cmd_mock, get_all_details_mock):
        no_drives = raid_constants.HPSSA_NO_DRIVES
        one_drive = raid_constants.HPSSA_ONE_DRIVE_100GB_RAID_5
        get_all_details_mock.side_effect = [no_drives, one_drive, one_drive]
        ex = self.assertRaises(exception.HPSSAOperationError,
                               self._test_create_configuration_with_disk_input,
                               controller_exec_cmd_mock, get_all_details_mock)
        self.assertIn("raid_level '1' and size 50 GB not found", str(ex))

    @mock.patch('os.path.exists')
    def test_create_configuration_invalid_logical_disks(self, mock_path,
                                                        get_all_details_mock):

        drives = raid_constants.HPSSA_NO_DRIVES
        get_all_details_mock.return_value = drives
        mock_path.return_value = True
        raid_info = {}
        self.assertRaises(exception.InvalidInputError,
                          manager.create_configuration,
                          raid_info)

        raid_info = {'logical_disks': 'foo'}
        self.assertRaises(exception.InvalidInputError,
                          manager.create_configuration,
                          raid_info)

        no_drives = raid_constants.HPSSA_NO_DRIVES
        get_all_details_mock.return_value = no_drives
        raid_info = {'logical_disks': [
                     {'size_gb': 50,
                      'raid_level': '1',
                      'controller': 'MSCC SmartRAID 3154-8e in Slot 0',
                      'physical_disks': ["CN1:1:11", "CN1:1:12"]}]}
        msg = ("Invalid Input: Unable to find controller named 'MSCC "
               "SmartRAID 3154-8e in Slot 0'. The available controllers are "
               "'MSCC SmartRAID 3154-8e in Slot 2085'.")
        ex = self.assertRaises(exception.InvalidInputError,
                               manager.create_configuration,
                               raid_info)
        self.assertEqual(msg, str(ex))

    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_create_configuration_without_disk_input_succeeds(
            self, controller_exec_cmd_mock, get_all_details_mock):
        no_drives = raid_constants.HPSSA_NO_DRIVES
        one_drive = raid_constants.HPSSA_ONE_DRIVE_100GB_RAID_5
        two_drives = raid_constants.HPSSA_TWO_DRIVES_100GB_RAID5_50GB_RAID1
        get_all_details_mock.side_effect = [no_drives, one_drive, two_drives]
        raid_info = {'logical_disks': [{'size_gb': 50,
                                        'raid_level': '1'},
                                       {'size_gb': 100,
                                        'raid_level': '5'}]}
        current_config = manager.create_configuration(raid_info)
        controller_exec_cmd_mock.assert_any_call("create",
                                                 "type=logicaldrive",
                                                 mock.ANY,
                                                 "raid=5",
                                                 "size=%d" % (100*1024),
                                                 process_input='y')
        # Verify that we created the 50GB disk the last.
        controller_exec_cmd_mock.assert_called_with("create",
                                                    "type=logicaldrive",
                                                    mock.ANY,
                                                    "raid=1",
                                                    "size=%d" % (50*1024),
                                                    process_input='y')

        ld1_ret = [x for x in current_config['logical_disks']
                   if x['raid_level'] == '1'][0]
        ld2_ret = [x for x in current_config['logical_disks']
                   if x['raid_level'] == '5'][0]
        self.assertEqual('0x600508b1001c7575',
                         ld2_ret['root_device_hint']['wwn'])
        self.assertEqual('0x600508b1001ca177',
                         ld1_ret['root_device_hint']['wwn'])

    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_create_configuration_without_disk_input_fails_on_disk_type(
            self, controller_exec_cmd_mock, get_all_details_mock):
        no_drives = raid_constants.HPSSA_NO_DRIVES
        one_drive = raid_constants.HPSSA_ONE_DRIVE_100GB_RAID_5
        two_drives = raid_constants.HPSSA_TWO_DRIVES_100GB_RAID5_50GB_RAID1
        get_all_details_mock.side_effect = [no_drives, one_drive, two_drives]
        raid_info = {'logical_disks': [{'size_gb': 50,
                                        'raid_level': '1',
                                        'disk_type': 'hdd'},
                                       {'size_gb': 100,
                                        'raid_level': '5',
                                        'disk_type': 'ssd'}]}
        exc = self.assertRaises(exception.PhysicalDisksNotFoundError,
                                manager.create_configuration, raid_info)
        self.assertIn("of size 50 GB and raid level 1", str(exc))

    def test_create_configuration_hba_enabled(self, get_all_details_mock):
        drives = raid_constants.HPSSA_HBA_MODE
        get_all_details_mock.return_value = drives

        raid_info = {'logical_disks': 'foo'}

        msg = ("An error was encountered while doing ssa configuration: None"
               " of the available SSA controllers MSCC SmartRAID 3154-8e in "
               "Slot 2085 have RAID enabled")
        ex = self.assertRaises(exception.HPSSAOperationError,
                               manager.create_configuration,
                               raid_info)
        self.assertIn(msg, str(ex))

    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_create_configuration_share_physical_disks(
            self, controller_exec_cmd_mock, get_all_details_mock):
        no_drives = raid_constants.HPSSA_NO_DRIVES_3_PHYSICAL_DISKS
        one_drive = raid_constants.ONE_DRIVE_RAID_1
        two_drives = raid_constants.TWO_DRIVES_50GB_RAID1
        get_all_details_mock.side_effect = [no_drives, one_drive, two_drives]
        controller_exec_cmd_mock.side_effect = [
            (None, None),
            (raid_constants.DRIVE_2_RAID_1_OKAY_TO_SHARE, None),
            (None, None)]
        raid_info = {'logical_disks': [{'size_gb': 50,
                                        'share_physical_disks': True,
                                        'number_of_physical_disks': 2,
                                        'raid_level': '0',
                                        'disk_type': 'hdd'},
                                       {'size_gb': 50,
                                        'share_physical_disks': True,
                                        'raid_level': '1',
                                        'disk_type': 'hdd'}]}
        raid_info = manager.create_configuration(raid_info)
        ld1 = raid_info['logical_disks'][0]
        ld2 = raid_info['logical_disks'][1]
        self.assertEqual('MSCC SmartRAID 3154-8e in Slot 2085',
                         ld1['controller'])
        self.assertEqual('MSCC SmartRAID 3154-8e in Slot 2085',
                         ld2['controller'])
        self.assertEqual(sorted(['CN1:1:1', 'CN1:1:2']),
                         sorted(ld1['physical_disks']))
        self.assertEqual(sorted(['CN1:1:1', 'CN1:1:2']),
                         sorted(ld2['physical_disks']))
        controller_exec_cmd_mock.assert_any_call(
            'create', 'type=logicaldrive', 'drives=CN1:1:1,CN1:1:2',
            'raid=1', 'size=51200', process_input='y')
        controller_exec_cmd_mock.assert_any_call(
            'array', 'A', 'create', 'type=logicaldrive', 'raid=0', 'size=?',
            dont_transform_to_hpssa_exception=True)
        controller_exec_cmd_mock.assert_any_call(
            'array', 'A', 'create', 'type=logicaldrive', 'raid=0',
            'size=51200', process_input='y')

    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_create_configuration_share_nonshare_physical_disks(
            self, controller_exec_cmd_mock, get_all_details_mock):
        no_drives = raid_constants.HPSSA_NO_DRIVES_3_PHYSICAL_DISKS
        one_drive = raid_constants.ONE_DRIVE_RAID_1
        two_drives = raid_constants.TWO_DRIVES_50GB_RAID1
        get_all_details_mock.side_effect = [no_drives, one_drive, two_drives]
        controller_exec_cmd_mock.side_effect = [
            (None, None),
            (raid_constants.DRIVE_2_RAID_1_OKAY_TO_SHARE, None),
            (None, None)]
        raid_info = {'logical_disks': [{'size_gb': 50,
                                        'raid_level': '1',
                                        'disk_type': 'hdd'},
                                       {'size_gb': 50,
                                        'share_physical_disks': True,
                                        'raid_level': '0',
                                        'disk_type': 'hdd'}]}
        raid_info = manager.create_configuration(raid_info)
        ld1 = raid_info['logical_disks'][0]
        ld2 = raid_info['logical_disks'][1]
        self.assertEqual('MSCC SmartRAID 3154-8e in Slot 2085',
                         ld1['controller'])
        self.assertEqual('MSCC SmartRAID 3154-8e in Slot 2085',
                         ld2['controller'])
        self.assertEqual(sorted(['CN1:1:1', 'CN1:1:2']),
                         sorted(ld1['physical_disks']))
        self.assertEqual(sorted(['CN1:1:1', 'CN1:1:2']),
                         sorted(ld2['physical_disks']))
        controller_exec_cmd_mock.assert_any_call(
            'create', 'type=logicaldrive', 'drives=CN1:1:1,CN1:1:2',
            'raid=1', 'size=51200', process_input='y')
        controller_exec_cmd_mock.assert_any_call(
            'create', 'type=logicaldrive', 'drives=CN1:1:3', 'raid=0',
            'size=51200', process_input='y')

    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_create_configuration_max_as_size_gb(
            self, controller_exec_cmd_mock, get_all_details_mock):
        no_drives = raid_constants.NO_DRIVES_HPSSA_7_DISKS
        one_drive = raid_constants.ONE_DRIVE_RAID_1_50_GB
        two_drives = raid_constants.TWO_DRIVES_50GB_RAID1_MAXGB_RAID5
        get_all_details_mock.side_effect = [no_drives, one_drive, two_drives]
        raid_info = {'logical_disks': [{'size_gb': 50,
                                        'raid_level': '1',
                                        'disk_type': 'hdd'},
                                       {'size_gb': 'MAX',
                                        'raid_level': '5',
                                        'disk_type': 'hdd'}]}
        raid_info = manager.create_configuration(raid_info)
        ld1 = raid_info['logical_disks'][0]
        ld2 = raid_info['logical_disks'][1]
        self.assertEqual('MSCC SmartRAID 3154-8e in Slot 2085',
                         ld1['controller'])
        self.assertEqual('MSCC SmartRAID 3154-8e in Slot 2085',
                         ld2['controller'])
        self.assertEqual(sorted(['CN1:1:1', 'CN1:1:2']),
                         sorted(ld1['physical_disks']))
        self.assertEqual(sorted(['CN1:1:3', 'CN1:1:4', 'CN0:1:5']),
                         sorted(ld2['physical_disks']))
        controller_exec_cmd_mock.assert_any_call(
            'create', 'type=logicaldrive', 'drives=CN1:1:1,CN1:1:2',
            'raid=1', 'size=51200', process_input='y')
        controller_exec_cmd_mock.assert_any_call(
            'create', 'type=logicaldrive', 'drives=CN1:1:3,CN1:1:4,CN0:1:5',
            'raid=5', process_input='y')

    @mock.patch.object(manager, 'get_configuration')
    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_delete_configuration(self, controller_exec_cmd_mock,
                                  get_configuration_mock,
                                  get_all_details_mock):
        get_all_details_mock.return_value = raid_constants.HPSSA_ONE_DRIVE
        get_configuration_mock.return_value = 'foo'

        ret = manager.delete_configuration()

        controller_exec_cmd_mock.assert_called_with(
            "logicaldrive", "all", "delete", "forced")
        get_configuration_mock.assert_called_once_with()
        self.assertEqual('foo', ret)

    @mock.patch.object(manager, 'get_configuration')
    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_delete_configuration_no_arrays(
            self, controller_exec_cmd_mock,
            get_configuration_mock, get_all_details_mock):

        get_all_details_mock.return_value = raid_constants.HPSSA_NO_DRIVES
        get_configuration_mock.return_value = 'foo'

        ret = manager.delete_configuration()

        self.assertFalse(controller_exec_cmd_mock.called)
        get_configuration_mock.assert_called_once_with()
        self.assertEqual('foo', ret)

    @mock.patch.object(manager, 'get_configuration')
    def test_delete_configuration_hba_enabled(self, get_configuration,
                                              get_all_details_mock):
        drives = raid_constants.HPSSA_HBA_MODE
        get_all_details_mock.return_value = drives

        msg = ("An error was encountered while doing ssa configuration: None"
               " of the available SSA controllers MSCC SmartRAID 3154-8e in "
               "Slot 2085 have RAID enabled")
        ex = self.assertRaises(exception.HPSSAOperationError,
                               manager.delete_configuration)
        self.assertIn(msg, str(ex))

    def test_get_configuration(self, get_all_details_mock):

        get_all_details_mock.return_value = raid_constants.HPSSA_ONE_DRIVE

        raid_info_returned = manager.get_configuration()

        ld1_expected = {'size_gb': 99,
                        'raid_level': '1',
                        'controller': 'MSCC SmartRAID 3154-8e in Slot 2085',
                        'physical_disks': ['CN1:1:1', 'CN1:1:2'],
                        'volume_name': '0216D8AE8A02F3004A0    DFDE',
                        'root_device_hint': {
                            'wwn': '0x600508b1001ca177'}}

        # NOTE(rameshg87: Cannot directly compare because
        # of 'physical_disks' key.
        ld1_returned = raid_info_returned['logical_disks'][0]
        self.assertEqual(ld1_expected['size_gb'],
                         ld1_returned['size_gb'])
        self.assertEqual(ld1_expected['raid_level'],
                         ld1_returned['raid_level'])
        self.assertEqual(ld1_expected['controller'],
                         ld1_returned['controller'])
        self.assertEqual(ld1_expected['volume_name'],
                         ld1_returned['volume_name'])
        self.assertEqual(ld1_expected['root_device_hint'],
                         ld1_returned['root_device_hint'])
        self.assertEqual(sorted(ld1_expected['physical_disks']),
                         sorted(ld1_returned['physical_disks']))

        # Assert physical disk info
        pds_active = [x['id'] for x in raid_info_returned['physical_disks']
                      if x['status'] == 'active']
        pds_ready = [x['id'] for x in raid_info_returned['physical_disks']
                     if x['status'] == 'ready']
        pds_active_expected = ['CN1:1:1', 'CN1:1:2']
        pds_ready_expected = ['CN1:1:3', 'CN1:1:4', 'CN1:1:5', 'CN1:1:11',
                              'CN1:1:12']
        self.assertEqual(sorted(pds_active_expected), sorted(pds_active))
        self.assertEqual(sorted(pds_ready_expected), sorted(pds_ready))

    def test__select_controllers_by_hba(self, get_all_details_mock):
        get_all_details_mock.return_value = raid_constants.HPSSA_HBA_MODE

        server = objects.Server()
        select_controllers = lambda x: not x.properties.get('HBA Mode Enabled',
                                                            False)

        msg = ("An error was encountered while doing ssa configuration: "
               "None of the available SSA controllers MSCC SmartRAID 3154-8e "
               "in Slot 2085 have Raid enabled.")
        ex = self.assertRaises(exception.HPSSAOperationError,
                               manager._select_controllers_by,
                               server, select_controllers, 'Raid enabled')
        self.assertIn(msg, str(ex))

    def test__select_controllers_by(self, get_all_details_mock):
        get_all_details_mock.return_value = raid_constants.HPSSA_NO_DRIVES

        server = objects.Server()
        select_controllers = lambda x: not x.properties.get('HBA Mode Enabled',
                                                            False)
        ctrl_expected = server.controllers

        manager._select_controllers_by(server, select_controllers,
                                       'Raid enabled')
        self.assertEqual(ctrl_expected, server.controllers)

    @mock.patch.object(time, 'sleep')
    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_erase_devices(self, controller_exec_cmd_mock,
                           sleep_mock,
                           get_all_details_mock):
        erase_drive = raid_constants.SSA_ERASE_DRIVE
        erase_complete = raid_constants.SSA_ERASE_COMPLETE
        cmd_args = []
        cmd_args.append("pd 1I:2:1")
        cmd_args.extend(['modify', 'erase',
                         'erasepattern=overwrite',
                         'unrestricted=off',
                         'forced'])
        expt_ret = {
            'MSCC SmartRAID 3154-8e in Slot 2085': {
                'CN1:1:14': 'Erase Complete. Reenable Before Using.',
                'Summary': ('Sanitize Erase performed on the disks attached to'
                            ' the controller.')}}
        get_all_details_mock.side_effect = [erase_drive, erase_complete,
                                            erase_complete]

        ret = manager.erase_devices()
        self.assertTrue(controller_exec_cmd_mock.called)
        controller_exec_cmd_mock.assert_any_call(*cmd_args)
        self.assertEqual(expt_ret, ret)
        self.assertFalse(sleep_mock.called)

    @mock.patch.object(time, 'sleep')
    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_erase_devices_in_progress(self, controller_exec_cmd_mock,
                                       sleep_mock,
                                       get_all_details_mock):

        erase_drive = raid_constants.SSA_ERASE_DRIVE
        erase_progress = raid_constants.SSA_ERASE_IN_PROGRESS
        erase_complete = raid_constants.SSA_ERASE_COMPLETE

        expt_ret = {
            'MSCC SmartRAID 3154-8e in Slot 2085': {
                'CN1:1:14': 'Erase Complete. Reenable Before Using.',
                'Summary': ('Sanitize Erase performed on the disks attached to'
                            ' the controller.')}}
        get_all_details_mock.side_effect = [erase_drive, erase_progress,
                                            erase_complete, erase_complete]

        ret = manager.erase_devices()
        self.assertTrue(controller_exec_cmd_mock.called)
        self.assertEqual(expt_ret, ret)
        self.assertTrue(sleep_mock.called)

    @mock.patch.object(time, 'sleep')
    @mock.patch.object(objects.Controller, 'execute_cmd')
    def test_erase_devices_not_supported(self, controller_exec_cmd_mock,
                                         sleep_mock,
                                         get_all_details_mock):
        erase_not_supported = raid_constants.SSA_ERASE_NOT_SUPPORTED
        erase_complete = raid_constants.SSA_ERASE_COMPLETE_NOT_SUPPORTED
        erase_progress = raid_constants.SSA_ERASE_IN_PROGRESS_NOT_SUPPORTED
        get_all_details_mock.side_effect = [erase_not_supported,
                                            erase_progress,
                                            erase_complete, erase_complete]
        value = ("Drive CN1:1:14 This operation is not supported in this "
                 "physical drive")
        controller_exec_cmd_mock.return_value = value
        expt_ret = {
            'MSCC SmartRAID 3154-8e in Slot 2085': {
                'CN1:2:1': 'Erase Complete. Reenable Before Using.',
                'Summary': ('Drives overwritten with zeros because '
                            'sanitize erase is not supported on the '
                            'controller.')
                }}

        ret = manager.erase_devices()
        self.assertEqual(expt_ret, ret)
        self.assertTrue(controller_exec_cmd_mock.called)
        self.assertTrue(sleep_mock.called)