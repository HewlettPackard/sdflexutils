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

import mock
from sdflexutils import exception
from sdflexutils.storcli import disk_allocator
from sdflexutils.storcli import storcli
from sdflexutils.tests.unit.storcli import raid_constants
import testtools


class DiskAllocatorTestCase(testtools.TestCase):

    @mock.patch.object(storcli, '_storcli')
    def test_get_supported_controllers_raid(self, get_all_details_mock):
        get_all_details_mock.return_value = (
            raid_constants.SHOW_PERSONALITY_RAID)
        supported_ctrl = [0]
        self.assertEqual(supported_ctrl,
                         disk_allocator.get_supported_controllers())

    @mock.patch.object(storcli, '_storcli')
    def test_get_supported_controllers_jbod(self, get_all_details_mock):
        get_all_details_mock.return_value = (
            raid_constants.SHOW_PERSONALITY_JBOD)
        supported_ctrl = []
        self.assertEqual(supported_ctrl,
                         disk_allocator.get_supported_controllers())

    @mock.patch.object(storcli, '_storcli', autospec=True)
    def test_get_supported_controllers_exception(self, storcli_mock):
        storcli_mock.side_effect = exception.StorcliOperationError(reason='')
        self.assertRaises(exception.StorcliOperationError,
                          disk_allocator.get_supported_controllers)

    @mock.patch.object(storcli, '_storcli')
    def test__get_criteria_matching_disks_all_criterias(self,
                                                        get_all_details_mock):
        get_all_details_mock.return_value = raid_constants. \
            C0_E252_S1_SHOW_ALL_SSD_SATA
        controller = 0
        physical_drives = ['252:1']

        logical_disk = {'size_gb': 100,
                        'raid_level': '0',
                        'disk_type': 'ssd',
                        'interface_type': 'sata',
                        'model': 'TOSHIBA THNSNJ120PCSZ',
                        'firmware': 'JZET6102'}

        ret_physical_drives = disk_allocator._get_criteria_matching_disks(
            logical_disk, physical_drives, controller)
        self.assertEqual([pd[0] for pd in ret_physical_drives],
                         physical_drives)

    @mock.patch.object(storcli, '_storcli')
    def test__get_criteria_matching_disks_not_all_criterias(
            self, get_all_details_mock):
        get_all_details_mock.return_value = raid_constants. \
            C0_E252_S1_SHOW_ALL_SSD_SATA
        physical_drives = ['252:1']
        controller = 0
        logical_disk = {'size_gb': 100,
                        'raid_level': '0',
                        'disk_type': 'ssd',
                        'interface_type': 'sata',
                        'model': 'TOSHIBA THNSNJ120PCSZ'}

        ret_physical_drives = disk_allocator._get_criteria_matching_disks(
            logical_disk, physical_drives, controller)
        self.assertEqual([pd[0] for pd in ret_physical_drives],
                         physical_drives)

    @mock.patch.object(storcli, '_storcli')
    def test__get_criteria_matching_disks_some_disks_dont_match(
            self, get_all_details_mock):
        get_all_details_mock.side_effect = [
            raid_constants.C0_E252_S0_SHOW_ALL_SSD_SATA,
            raid_constants.C0_E252_S1_SHOW_ALL_SSD_SATA,
            raid_constants.C0_E252_S2_SHOW_ALL_SSD_SATA]
        physical_drives = ['252:0', '252:1', '252:2']
        controller = 0
        logical_disk = {'size_gb': 100,
                        'raid_level': '1',
                        'disk_type': 'ssd',
                        'interface_type': 'sata',
                        'firmware': 'JZET6102'}

        ret_physical_drives = disk_allocator._get_criteria_matching_disks(
            logical_disk, physical_drives, controller)
        exp_physical_drives = physical_drives[1:]
        self.assertEqual(exp_physical_drives,
                         [x[0] for x in ret_physical_drives])

    @mock.patch.object(storcli, '_storcli')
    def test__get_criteria_matching_disks_no_disks_match(
            self, get_all_details_mock):
        get_all_details_mock.side_effect = [
            raid_constants.C0_E252_S0_SHOW_ALL_SSD_SATA,
            raid_constants.C0_E252_S1_SHOW_ALL_SSD_SATA,
            raid_constants.C0_E252_S2_SHOW_ALL_SSD_SATA]
        physical_drives = ['252:0', '252:1', '252:2']
        controller = 0

        logical_disk = {'size_gb': 100,
                        'raid_level': '1',
                        'disk_type': 'ssd',
                        'interface_type': 'sas',
                        'firmware': 'HPD6'}

        ret_physical_drives = disk_allocator._get_criteria_matching_disks(
            logical_disk, physical_drives, controller)
        self.assertEqual(ret_physical_drives, [])

    @mock.patch.object(storcli, '_storcli', autospec=True)
    def test_get_criteria_matching_disks_exception(self, storcli_mock):
        physical_drives = ['252:0', '252:1', '252:2']
        controller = 0

        logical_disk = {'size_gb': 100,
                        'raid_level': '1',
                        'disk_type': 'ssd',
                        'interface_type': 'sas',
                        'firmware': 'HPD6'}
        storcli_mock.side_effect = exception.StorcliOperationError(reason='')
        self.assertRaises(exception.StorcliOperationError,
                          disk_allocator._get_criteria_matching_disks,
                          logical_disk, physical_drives, controller)

    def test__validate_raid_0_no_of_pd_more_than_reqd(self):
        logical_disk = {'size_gb': 200,
                        'raid_level': '0',
                        'number_of_physical_disks': 4}
        unassigned_pd = [['252:0', '110.281'], ['252:1', '110.281'],
                         ['252:2', '110.281'], ['252:3', '110.281']]
        self.assertEqual(unassigned_pd, disk_allocator._validate_raid_0(
            logical_disk, unassigned_pd, 4))

    def test__validate_raid_0_success(self):
        logical_disk = {'size_gb': 200,
                        'raid_level': '0'}
        unassigned_pd = [['252:0', '110.281'], ['252:1', '110.281']]
        self.assertEqual(unassigned_pd, disk_allocator._validate_raid_0(
            logical_disk, unassigned_pd, False))

    def test__validate_raid_0_not_enough_pd(self):
        logical_disk = {'size_gb': 300,
                        'raid_level': '0'}
        unassigned_pd = [['252:0', '110.281'], ['252:1', '110.281']]
        self.assertEqual([], disk_allocator._validate_raid_0(
            logical_disk, unassigned_pd, False))

    def test__validate_raid_0_not_enough_pd_no_of_pd(self):
        logical_disk = {'size_gb': 300,
                        'raid_level': '0',
                        'number_of_physical_disks': 2}
        unassigned_pd = [['252:0', '110.281'], ['252:1', '110.281'],
                         ['252:2', '110.281'], ['252:3', '110.281']]
        self.assertEqual([], disk_allocator._validate_raid_0(
            logical_disk, unassigned_pd, 2))

    def test__validate_raid_1_not_enough_pd_2(self):
        logical_disk = {'size_gb': 200,
                        'raid_level': '1'}
        unassigned_pd = [['252:0', '50'], ['252:1', '90'], ['252:2', '100']]
        self.assertEqual([], disk_allocator._validate_raid_1(
            logical_disk, unassigned_pd, False))

    def test__validate_raid_1_not_enough_pd_4(self):
        logical_disk = {'size_gb': 200,
                        'raid_level': '1'}
        unassigned_pd = [['252:0', '50'], ['252:1', '90'], ['252:2', '100'],
                         ['252:3', '100']]
        self.assertEqual([], disk_allocator._validate_raid_1(
            logical_disk, unassigned_pd, False))

    def test__validate_raid_1_success_4_disks(self):
        logical_disk = {'size_gb': 200,
                        'raid_level': '1'}
        unassigned_pd = [['252:0', '110.281'], ['252:1', '110.281'],
                         ['252:3', '110.281'], ['252:2', '465.25']]
        self.assertEqual(unassigned_pd, disk_allocator._validate_raid_1(
            logical_disk, unassigned_pd, False))

    def test__validate_raid_1_success_2_disks(self):
        logical_disk = {'size_gb': 100,
                        'raid_level': '1'}
        unassigned_pd = [['252:0', '110.281'], ['252:1', '110.281'],
                         ['252:3', '110.281'], ['252:2', '465.25']]
        self.assertEqual(unassigned_pd[:2], disk_allocator._validate_raid_1(
            logical_disk, unassigned_pd, False))

    def test__validate_raid_1_success_4_disks_no_of_pd(self):
        logical_disk = {'size_gb': 200,
                        'raid_level': '1',
                        'number_of_physical_disks': 4}
        unassigned_pd = [['252:0', '110.281'], ['252:1', '110.281'],
                         ['252:3', '110.281'], ['252:2', '465.25']]
        self.assertEqual(unassigned_pd, disk_allocator._validate_raid_1(
            logical_disk, unassigned_pd, 4))

    def test__validate_raid_1_success_2_disks_no_pd(self):
        logical_disk = {'size_gb': 100,
                        'raid_level': '1',
                        'number_of_physical_disks': 2}
        unassigned_pd = [['252:0', '110.281'], ['252:1', '110.281'],
                         ['252:3', '110.281'], ['252:2', '465.25']]
        self.assertEqual(unassigned_pd[:2], disk_allocator._validate_raid_1(
            logical_disk, unassigned_pd, 2))

    def test__validate_raid_5_not_enough_pd(self):
        logical_disk = {
            "size_gb": 350,
            "raid_level": "5"
        }
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        self.assertEqual([], disk_allocator._validate_raid_5(
            logical_disk, unassigned_pd, False))

    def test__validate_raid_5_not_enough_pd_no_of_pd_3(self):
        logical_disk = {
            "size_gb": 300,
            "raid_level": "5",
            'number_of_physical_disks': 3
        }
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        self.assertEqual([], disk_allocator._validate_raid_5(
            logical_disk, unassigned_pd, 3))

    def test__validate_raid_5_not_enough_pd_no_of_pd_4(self):
        logical_disk = {
            "size_gb": 350,
            "raid_level": "5",
            'number_of_physical_disks': 4
        }
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        self.assertEqual([], disk_allocator._validate_raid_5(
            logical_disk, unassigned_pd, 4))

    def test__validate_raid_5_success_3_disks(self):
        logical_disk = {
            "size_gb": 100,
            "raid_level": "5"
        }
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        self.assertEqual(unassigned_pd[:3], disk_allocator._validate_raid_5(
            logical_disk, unassigned_pd, False))

    def test__validate_raid_5_success_4_disks(self):
        logical_disk = {
            "size_gb": 300,
            "raid_level": "5"
        }
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        self.assertEqual(unassigned_pd, disk_allocator._validate_raid_5(
            logical_disk, unassigned_pd, False))

    def test__validate_raid_5_success_3_disks_no_of_pd(self):
        logical_disk = {
            "size_gb": 100,
            "raid_level": "5",
            'number_of_physical_disks': 3
        }
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        self.assertEqual(unassigned_pd[:3], disk_allocator._validate_raid_5(
            logical_disk, unassigned_pd, 3))

    def test__validate_raid_5_success_4_disks_no_pd(self):
        logical_disk = {
            "size_gb": 300,
            "raid_level": "5",
            'number_of_physical_disks': 4
        }
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        self.assertEqual(unassigned_pd, disk_allocator._validate_raid_5(
            logical_disk, unassigned_pd, 4))

    def test__validate_raid_6_10_not_enough_pd(self):
        logical_disk = {
            "size_gb": 250,
            "raid_level": "6"
        }
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        self.assertEqual([], disk_allocator._validate_raid_6_10(
            logical_disk, unassigned_pd))

    def test__validate_raid_6_10_success(self):
        logical_disk = {
            "size_gb": 100,
            "raid_level": "6"
        }
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        self.assertEqual(unassigned_pd, disk_allocator._validate_raid_6_10(
            logical_disk, unassigned_pd))

    def test__validate_disks_size_max_success(self):
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:2', '465.25'], ['252:3', '111.281']]

        logical_disk_0_max = {
            "size_gb": 'MAX',
            "raid_level": "0"
        }
        self.assertEqual(
            disk_allocator._validate_disks_size(logical_disk_0_max,
                                                unassigned_pd),
            [['252:2', '465.25'], ['252:0', '111.281'], ['252:1', '111.281'],
             ['252:3', '111.281']])

        logical_disk_1_max = {
            "size_gb": 'MAX',
            "raid_level": "1"
        }
        self.assertEqual(
            disk_allocator._validate_disks_size(logical_disk_1_max,
                                                unassigned_pd),
            [['252:2', '465.25'], ['252:0', '111.281'], ['252:1', '111.281'],
             ['252:3', '111.281']])

        logical_disk_5_max = {
            "size_gb": 'MAX',
            "raid_level": "5"
        }
        self.assertEqual(
            disk_allocator._validate_disks_size(logical_disk_5_max,
                                                unassigned_pd),
            [['252:2', '465.25'], ['252:0', '111.281'], ['252:1', '111.281'],
             ['252:3', '111.281']])

        logical_disk_10_max = {
            "size_gb": 'MAX',
            "raid_level": "1+0"
        }
        self.assertEqual(
            disk_allocator._validate_disks_size(logical_disk_10_max,
                                                unassigned_pd),
            [['252:2', '465.25'], ['252:0', '111.281'], ['252:1', '111.281'],
             ['252:3', '111.281']])

    def test__validate_disks_size_max_success_no_of_pds(self):
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:2', '465.25'], ['252:3', '111.281']]

        logical_disk_0_max = {
            "size_gb": 'MAX',
            "raid_level": "0",
            'number_of_physical_disks': 3
        }
        self.assertEqual(disk_allocator._validate_disks_size(
            logical_disk_0_max, unassigned_pd),
            [['252:2', '465.25'], ['252:0', '111.281'], ['252:1', '111.281']])

        logical_disk_1_max_2 = {
            "size_gb": 'MAX',
            "raid_level": "1",
            'number_of_physical_disks': 2
        }
        self.assertEqual(disk_allocator._validate_disks_size(
            logical_disk_1_max_2, unassigned_pd),
            [['252:2', '465.25'], ['252:0', '111.281']])

        logical_disk_1_max_4 = {
            "size_gb": 'MAX',
            "raid_level": "1",
            'number_of_physical_disks': 4
        }
        self.assertEqual(disk_allocator._validate_disks_size(
            logical_disk_1_max_4, unassigned_pd),
            [['252:2', '465.25'], ['252:0', '111.281'], ['252:1', '111.281'],
             ['252:3', '111.281']])

        logical_disk_5_max_3 = {
            "size_gb": 'MAX',
            "raid_level": "5",
            'number_of_physical_disks': 3
        }
        self.assertEqual(disk_allocator._validate_disks_size(
            logical_disk_5_max_3, unassigned_pd),
            [['252:2', '465.25'], ['252:0', '111.281'], ['252:1', '111.281']])

        logical_disk_5_max_4 = {
            "size_gb": 'MAX',
            "raid_level": "5",
            'number_of_physical_disks': 4
        }
        self.assertEqual(disk_allocator._validate_disks_size(
            logical_disk_5_max_4, unassigned_pd),
            [['252:2', '465.25'], ['252:0', '111.281'], ['252:1', '111.281'],
             ['252:3', '111.281']])

        logical_disk_10_max = {
            "size_gb": 'MAX',
            "raid_level": "1+0",
            'number_of_physical_disks': 4
        }
        self.assertEqual(disk_allocator._validate_disks_size(
            logical_disk_10_max, unassigned_pd),
            [['252:2', '465.25'], ['252:0', '111.281'], ['252:1', '111.281'],
             ['252:3', '111.281']])

    def test__validate_disks_size_max_less_pd(self):
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]

        logical_disk_1_max = {
            "size_gb": 'MAX',
            "raid_level": "1"
        }
        self.assertEqual([], disk_allocator._validate_disks_size(
            logical_disk_1_max, unassigned_pd[:1]))

        logical_disk_10_max = {
            "size_gb": 'MAX',
            "raid_level": "1+0"
        }
        self.assertEqual([], disk_allocator._validate_disks_size(
            logical_disk_10_max, unassigned_pd[:-1]))

        logical_disk_6_max = {
            "size_gb": 'MAX',
            "raid_level": "6"
        }
        self.assertEqual([], disk_allocator._validate_disks_size(
            logical_disk_6_max, unassigned_pd[:-1]))

        logical_disk_5_max = {
            "size_gb": 'MAX',
            "raid_level": "5"
        }
        self.assertEqual([], disk_allocator._validate_disks_size(
            logical_disk_5_max, unassigned_pd[0:-2]))

    def test__validate_disks_size_no_of_pds_more_than_unassigned(self):
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281']]
        logical_disk_1_max = {
            "size_gb": 'MAX',
            "raid_level": "1",
            'number_of_physical_disks': 4
        }
        self.assertEqual([], disk_allocator._validate_disks_size(
            logical_disk_1_max, unassigned_pd))

    @mock.patch.object(disk_allocator, '_validate_raid_0')
    def test__validate_disks_size_raid_0_success(self, raid_mock):
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:2', '465.25'], ['252:3', '111.281']]
        logical_disk = {
            "size_gb": 500,
            "raid_level": "0"
        }
        mock_ret = [['252:0', '111.281'], ['252:1', '111.281'],
                    ['252:3', '111.281'], ['252:2', '465.25']]
        raid_mock.return_value = mock_ret
        self.assertEqual(mock_ret, disk_allocator._validate_disks_size(
            logical_disk, unassigned_pd))

    def test__validate_disks_size_raid_0_failure_less_pd(self):
        logical_disk = {
            "size_gb": 500,
            "raid_level": "0"
        }
        self.assertEqual([], disk_allocator._validate_disks_size(
            logical_disk, []))

    @mock.patch.object(disk_allocator, '_validate_raid_1')
    def test__validate_disks_size_raid_1_success(self, raid_mock):
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        logical_disk = {
            "size_gb": 100,
            "raid_level": "1"
        }
        mock_ret = [['252:0', '111.281'], ['252:1', '111.281']]
        raid_mock.return_value = mock_ret
        self.assertEqual(mock_ret, disk_allocator._validate_disks_size(
            logical_disk, unassigned_pd))

    @mock.patch.object(disk_allocator, '_validate_raid_1')
    def test__validate_disks_size_raid_1_failure_less_pd(self, raid_mock):
        unassigned_pd = [['252:0', '111.281']]
        logical_disk = {
            "size_gb": 100,
            "raid_level": "1"
        }
        mock_ret = []
        raid_mock.return_value = mock_ret
        self.assertEqual(mock_ret, disk_allocator._validate_disks_size(
            logical_disk, unassigned_pd))

    @mock.patch.object(disk_allocator, '_validate_raid_5')
    def test__validate_disks_size_raid_5_success(self, raid_mock):
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        logical_disk = {
            "size_gb": 100,
            "raid_level": "5"
        }
        mock_ret = [['252:0', '111.281'], ['252:1', '111.281'],
                    ['252:2', '465.25']]
        raid_mock.return_value = mock_ret
        self.assertEqual(mock_ret, disk_allocator._validate_disks_size(
            logical_disk, unassigned_pd))

    @mock.patch.object(disk_allocator, '_validate_raid_5')
    def test__validate_disks_size_raid_5_failure_less_pd(self, raid_mock):
        unassigned_pd = [['252:0', '111.281']]
        logical_disk = {
            "size_gb": 100,
            "raid_level": "5"
        }
        mock_ret = []
        raid_mock.return_value = mock_ret
        self.assertEqual(mock_ret, disk_allocator._validate_disks_size(
            logical_disk, unassigned_pd))

    @mock.patch.object(disk_allocator, '_validate_raid_6_10')
    def test__validate_disks_size_raid_6_10_success(self, raid_mock):
        unassigned_pd = [['252:0', '111.281'], ['252:1', '111.281'],
                         ['252:3', '111.281'], ['252:2', '465.25']]
        logical_disk = {
            "size_gb": 100,
            "raid_level": "6"
        }
        mock_ret = [['252:0', '111.281'], ['252:1', '111.281'],
                    ['252:2', '465.25']]
        raid_mock.return_value = mock_ret
        self.assertEqual(mock_ret, disk_allocator._validate_disks_size(
            logical_disk, unassigned_pd))

    @mock.patch.object(disk_allocator, '_validate_raid_6_10')
    def test__validate_disks_size_raid_6_10_failure_less_pd(self, raid_mock):
        unassigned_pd = [['252:0', '111.281']]
        logical_disk = {
            "size_gb": 100,
            "raid_level": "1+0"
        }
        mock_ret = []
        raid_mock.return_value = mock_ret
        self.assertEqual(mock_ret, disk_allocator._validate_disks_size(
            logical_disk, unassigned_pd))

    @mock.patch.object(storcli, '_storcli')
    @mock.patch.object(disk_allocator, '_get_criteria_matching_disks')
    def test_allocate_disks_okay(self, get_match_disks, get_all_details_mock):
        get_all_details_mock.side_effect = [
            raid_constants.SHOW_PERSONALITY_RAID,
            raid_constants.C0_EALL_SALL_SHOW]
        get_match_disks.return_value = [['252:0', '111.281'],
                                        ['252:1', '111.281'],
                                        ['252:2', '111.281']]
        logical_disk = {'size_gb': 100,
                        'raid_level': '1',
                        'disk_type': 'ssd',
                        'interface_type': 'sata'}

        raid_config = {'logical_disks': [logical_disk]}
        disk_allocator.allocate_disks(logical_disk, raid_config)
        self.assertEqual(0, logical_disk['controller'])
        self.assertEqual(sorted(['252:0', '252:1']),
                         sorted(logical_disk['physical_disks']))

    @mock.patch.object(storcli, '_storcli')
    @mock.patch.object(disk_allocator, '_get_criteria_matching_disks')
    def test_allocate_disks_max_okay(self, get_match_disks,
                                     get_all_details_mock):
        get_all_details_mock.side_effect = [
            raid_constants.SHOW_PERSONALITY_RAID,
            raid_constants.C0_EALL_SALL_SHOW]

        logical_disk = {'size_gb': 'MAX',
                        'raid_level': '1',
                        'disk_type': 'ssd',
                        'interface_type': 'sata'}
        get_match_disks.return_value = [['252:0', '111.281'],
                                        ['252:1', '111.281'],
                                        ['252:2', '111.281']]
        raid_config = {'logical_disks': [logical_disk]}
        disk_allocator.allocate_disks(logical_disk, raid_config)
        self.assertEqual(0, logical_disk['controller'])
        self.assertEqual(sorted(['252:0', '252:1']),
                         sorted(logical_disk['physical_disks']))

    @mock.patch.object(storcli, '_storcli')
    @mock.patch.object(disk_allocator, '_get_criteria_matching_disks')
    def test_allocate_disks_disk_size_not_matching(self, get_match_disks,
                                                   get_all_details_mock):
        get_all_details_mock.side_effect = [
            raid_constants.SHOW_PERSONALITY_RAID,
            raid_constants.C0_EALL_SALL_SHOW]
        get_match_disks.return_value = [['252:0', '111.281'],
                                        ['252:1', '111.281'],
                                        ['252:2', '111.281']]
        logical_disk = {'size_gb': 700,
                        'raid_level': '1',
                        'disk_type': 'hdd',
                        'interface_type': 'sas'}
        raid_config = {'logical_disks': [logical_disk]}
        self.assertRaises(exception.StorcliPhysicalDisksNotFoundError,
                          disk_allocator.allocate_disks, logical_disk,
                          raid_config)

    @mock.patch.object(storcli, '_storcli')
    @mock.patch.object(disk_allocator, '_get_criteria_matching_disks')
    def test_allocate_disks_disk_not_enough_disks(self, get_match_disks,
                                                  get_all_details_mock):
        get_all_details_mock.side_effect = [
            raid_constants.SHOW_PERSONALITY_RAID,
            raid_constants.C0_EALL_SALL_SHOW]
        get_match_disks.return_value = [['252:0', '111.281'],
                                        ['252:1', '111.281'],
                                        ['252:2', '111.281']]
        logical_disk = {'size_gb': 600,
                        'raid_level': '6',
                        'disk_type': 'ssd',
                        'interface_type': 'sata'}
        raid_config = {'logical_disks': [logical_disk]}
        self.assertRaises(exception.StorcliPhysicalDisksNotFoundError,
                          disk_allocator.allocate_disks,
                          logical_disk, raid_config)

    @mock.patch.object(storcli, '_storcli')
    @mock.patch.object(disk_allocator, '_get_criteria_matching_disks')
    def test_allocate_disks_share_raid_level_not_matching(
            self, get_match_disks, get_all_details_mock):
        # Change all the physical drives to assigned
        pd_list = raid_constants.C0_EALL_SALL_SHOW_4_DISKS.replace(
            '"DG": "-"', '"DG": "0"')
        get_all_details_mock.side_effect = [
            raid_constants.SHOW_PERSONALITY_RAID, pd_list]
        get_match_disks.return_value = []

        logical_disk = {'size_gb': 50,
                        'raid_level': '6',
                        'disk_type': 'ssd',
                        'interface_type': 'sata',
                        'share_physical_disks': True}
        raid_config = {
            'logical_disks': [
                {'size_gb': 50,
                 'raid_level': '1+0',
                 'disk_type': 'ssd',
                 'controller': 0,
                 'interface_type': 'sata',
                 'share_physical_disks': True,
                 'physical_disks': ['252:0', '252:1', '252:2', '252:3'],
                 'volume_name': '/c0/v0'}]}
        self.assertRaises(exception.StorcliPhysicalDisksNotFoundError,
                          disk_allocator.allocate_disks,
                          logical_disk, raid_config)

    @mock.patch.object(storcli, '_storcli')
    @mock.patch.object(disk_allocator, '_get_criteria_matching_disks')
    def test_allocate_disks_share_no_other_sharable_logical_drive(
            self, get_match_disks, get_all_details_mock):
        # Change all the physical drives to assigned
        pd_list = raid_constants.C0_EALL_SALL_SHOW_4_DISKS.replace(
            '"DG": "-"', '"DG": "0"')
        get_all_details_mock.side_effect = [
            raid_constants.SHOW_PERSONALITY_RAID, pd_list]
        get_match_disks.return_value = []

        logical_disk = {'size_gb': 50,
                        'raid_level': '6',
                        'disk_type': 'ssd',
                        'interface_type': 'sata',
                        'share_physical_disks': True}
        raid_config = {
            'logical_disks': [
                {'size_gb': 50,
                 'raid_level': '1+0',
                 'disk_type': 'ssd',
                 'controller': 0,
                 'interface_type': 'sata',
                 'physical_disks': ['252:0', '252:1', '252:2', '252:3'],
                 'volume_name': '/c0/v0'}]}
        self.assertRaises(exception.StorcliPhysicalDisksNotFoundError,
                          disk_allocator.allocate_disks,
                          logical_disk, raid_config)

    @mock.patch.object(storcli, '_storcli')
    @mock.patch.object(disk_allocator, '_get_criteria_matching_disks')
    def test_allocate_disks_share_create_logical_drive(
            self, get_match_disks, get_all_details_mock):
        # Change all the physical drives to assigned
        pd_list = raid_constants.C0_EALL_SALL_SHOW_4_DISKS.replace(
            '"DG": "-"', '"DG": "0"')
        get_all_details_mock.side_effect = [
            raid_constants.SHOW_PERSONALITY_RAID,
            pd_list,
            raid_constants.C0_FREESPACE]
        get_match_disks.side_effect = [[], [['252:0', '111.281'],
                                            ['252:1', '111.281'],
                                            ['252:2', '465.25'],
                                            ['252:3', '111.281']]]

        logical_disk = {'size_gb': 40,
                        'raid_level': '1+0',
                        'disk_type': 'ssd',
                        'interface_type': 'sata',
                        'share_physical_disks': True}
        raid_config = {
            'logical_disks': [
                {'size_gb': 50,
                 'raid_level': '1+0',
                 'disk_type': 'ssd',
                 'interface_type': 'sata',
                 'controller': 0,
                 'share_physical_disks': True,
                 'physical_disks': ['252:0', '252:1', '252:2', '252:3'],
                 'volume_name': '/c0/v0'}]}
        ret_ld = {
            "controller": 0,
            "share_physical_disks": True,
            "size_gb": 40,
            "physical_disks": [
                "252:0",
                "252:1",
                "252:2",
                "252:3"
            ],
            "disk_type": "ssd",
            "interface_type": "sata",
            "raid_level": "1+0"
        }
        self.assertEqual(
            disk_allocator.allocate_disks(logical_disk, raid_config), ret_ld)

    @mock.patch.object(storcli, '_storcli')
    @mock.patch.object(disk_allocator, '_get_criteria_matching_disks')
    def test_allocate_disks_share_create_logical_drive_max(
            self, get_match_disks, get_all_details_mock):
        # Change all the physical drives to assigned
        pd_list = raid_constants.C0_EALL_SALL_SHOW_4_DISKS.replace(
            '"DG": "-"', '"DG": "0"')
        get_all_details_mock.side_effect = [
            raid_constants.SHOW_PERSONALITY_RAID,
            pd_list,
            raid_constants.C0_FREESPACE]
        get_match_disks.side_effect = [[], [['252:0', '111.281'],
                                            ['252:1', '111.281'],
                                            ['252:2', '465.25'],
                                            ['252:3', '111.281']]]

        logical_disk = {'size_gb': 'MAX',
                        'raid_level': '1+0',
                        'disk_type': 'ssd',
                        'interface_type': 'sata',
                        'share_physical_disks': True}
        raid_config = {
            'logical_disks': [
                {'size_gb': 50,
                 'raid_level': '1+0',
                 'disk_type': 'ssd',
                 'interface_type': 'sata',
                 'controller': 0,
                 'share_physical_disks': True,
                 'physical_disks': ['252:0', '252:1', '252:2', '252:3'],
                 'volume_name': '/c0/v0'}]}
        ret_ld = {
            "controller": 0,
            "share_physical_disks": True,
            "size_gb": 172,
            "physical_disks": [
                "252:0",
                "252:1",
                "252:2",
                "252:3"
            ],
            "disk_type": "ssd",
            "interface_type": "sata",
            "raid_level": "1+0"
        }
        self.assertEqual(
            disk_allocator.allocate_disks(logical_disk, raid_config), ret_ld)

    @mock.patch.object(storcli, '_storcli')
    def test_allocate_disks_controller_exception(self, storcli_mock):
        logical_disk = {'size_gb': 'MAX',
                        'raid_level': '1+0',
                        'disk_type': 'ssd',
                        'interface_type': 'sata',
                        'share_physical_disks': True}
        raid_config = {
            'logical_disks': [
                {'size_gb': 50,
                 'raid_level': '1+0',
                 'disk_type': 'ssd',
                 'interface_type': 'sata',
                 'controller': 0,
                 'share_physical_disks': True,
                 'physical_disks': ['252:0', '252:1', '252:2', '252:3'],
                 'volume_name': '/c0/v0'}]}
        storcli_mock.side_effect = exception.StorcliOperationError(reason='')
        self.assertRaises(exception.StorcliOperationError,
                          disk_allocator.allocate_disks,
                          logical_disk, raid_config)

    @mock.patch.object(storcli, '_storcli')
    @mock.patch.object(disk_allocator, 'get_supported_controllers')
    def test_allocate_disks_controller_exception_shared(
            self, ctrl_mock, storcli_mock):
        ctrl_mock.return_value = []
        logical_disk = {'size_gb': 'MAX',
                        'raid_level': '1+0',
                        'disk_type': 'ssd',
                        'interface_type': 'sata',
                        'share_physical_disks': True}
        raid_config = {
            'logical_disks': [
                {'size_gb': 50,
                 'raid_level': '1+0',
                 'disk_type': 'ssd',
                 'interface_type': 'sata',
                 'controller': 0,
                 'share_physical_disks': True,
                 'physical_disks': ['252:0', '252:1', '252:2', '252:3'],
                 'volume_name': '/c0/v0'}]}
        storcli_mock.side_effect = exception.StorcliOperationError(reason='')
        self.assertRaises(exception.StorcliOperationError,
                          disk_allocator.allocate_disks,
                          logical_disk, raid_config)
