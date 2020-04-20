# Copyright 2019 Hewlett Packard Enterprise Development LP
# Copyright 2014 Hewlett-Packard Development Company, L.P.
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

from sdflexutils.common import manager_utils
from sdflexutils import exception
import testtools


class ManagerTestCases(testtools.TestCase):
    def test__sort_shared_logical_disks(self):
        logical_disk_sorted_expected = [
            {'size_gb': 500, 'disk_type': 'hdd', 'raid_level': '1'},
            {'share_physical_disks': True, 'size_gb': 450, 'disk_type': 'hdd',
             'number_of_physical_disks': 6, 'raid_level': '0'},
            {'share_physical_disks': True, 'size_gb': 200, 'disk_type': 'hdd',
             'raid_level': '1+0'},
            {'share_physical_disks': True, 'size_gb': 200, 'disk_type': 'hdd',
             'raid_level': '0'},
            {'share_physical_disks': True, 'size_gb': 100, 'disk_type': 'hdd',
             'raid_level': '0'}]
        logical_disks = [{'size_gb': 500,
                          'disk_type': 'hdd',
                          'raid_level': '1'},
                         {'share_physical_disks': True,
                          'size_gb': 450,
                          'disk_type': 'hdd',
                          'number_of_physical_disks': 6,
                          'raid_level': '0'},
                         {'share_physical_disks': True,
                          'size_gb': 200,
                          'disk_type': 'hdd',
                          'raid_level': '1+0'},
                         {'share_physical_disks': True,
                          'size_gb': 200,
                          'disk_type': 'hdd',
                          'raid_level': '0'},
                         {'share_physical_disks': True,
                          'size_gb': 100,
                          'disk_type': 'hdd',
                          'raid_level': '0'}]
        logical_disks_sorted = manager_utils._sort_shared_logical_disks(
            logical_disks)
        self.assertEqual(logical_disks_sorted, logical_disk_sorted_expected)

    def test__sort_shared_logical_disks_raid10(self):
        logical_disk_sorted_expected = [
            {'size_gb': 600, 'disk_type': 'hdd', 'raid_level': '1'},
            {'share_physical_disks': False, 'size_gb': 400, 'disk_type': 'hdd',
             'raid_level': '1+0'},
            {'share_physical_disks': False, 'size_gb': 100, 'disk_type': 'hdd',
             'raid_level': '5'},
            {'share_physical_disks': True, 'size_gb': 550, 'disk_type': 'hdd',
             'raid_level': '1'},
            {'share_physical_disks': True, 'size_gb': 200, 'disk_type': 'hdd',
             'raid_level': '1+0'},
            {'share_physical_disks': True, 'size_gb': 450, 'disk_type': 'hdd',
             'number_of_physical_disks': 5, 'raid_level': '0'},
            {'share_physical_disks': True, 'size_gb': 300, 'disk_type': 'hdd',
             'raid_level': '5'}]
        logical_disks = [
            {'size_gb': 600, 'disk_type': 'hdd', 'raid_level': '1'},
            {'share_physical_disks': True, 'size_gb': 550, 'disk_type': 'hdd',
             'raid_level': '1'},
            {'share_physical_disks': True, 'size_gb': 450, 'disk_type': 'hdd',
             'number_of_physical_disks': 5, 'raid_level': '0'},
            {'share_physical_disks': False, 'size_gb': 400, 'disk_type': 'hdd',
             'raid_level': '1+0'},
            {'share_physical_disks': True, 'size_gb': 300, 'disk_type': 'hdd',
             'raid_level': '5'},
            {'share_physical_disks': True, 'size_gb': 200, 'disk_type': 'hdd',
             'raid_level': '1+0'},
            {'share_physical_disks': False, 'size_gb': 100, 'disk_type': 'hdd',
             'raid_level': '5'}]
        logical_disks_sorted = manager_utils._sort_shared_logical_disks(
            logical_disks)
        self.assertEqual(logical_disks_sorted, logical_disk_sorted_expected)


class RaidConfigValidationTestCases(testtools.TestCase):

    def test_validate_fails_min_disks_number(self):
        raid_config = {'logical_disks':
                       [{'size_gb': 100,
                         'raid_level': '5',
                         'number_of_physical_disks': 2}]}
        msg = "RAID level 5 requires at least 3 disks"
        self.assertRaisesRegex(exception.InvalidInputError, msg,
                               manager_utils.validate, raid_config)

    def test_validate_fails_min_physical_disks(self):
        raid_config = {'logical_disks':
                       [{'size_gb': 100, 'raid_level': '5',
                         'physical_disks': ['foo']}]}
        msg = "RAID level 5 requires at least 3 disks"
        self.assertRaisesRegex(exception.InvalidInputError, msg,
                               manager_utils.validate, raid_config)
