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

import time

import mock
from sdflexutils import exception
from sdflexutils.storcli import manager
from sdflexutils.storcli import storcli
from sdflexutils.tests.unit.storcli import raid_constants
import testtools


@mock.patch.object(storcli, '_storcli', autospec=True)
class ManagerTestCases(testtools.TestCase):

    def test_has_erase_completed_progress(self, storcli_mock):
        storcli_mock.return_value = (
            raid_constants.C0_EALL_SALL_SHOW_ERASE_IN_PROGRESS)
        ret = manager.has_erase_completed()
        self.assertFalse(ret)

    def test_has_erase_completed_not_in_progress(self, storcli_mock):
        storcli_mock.return_value = (
            raid_constants.C0_EALL_SALL_SHOW_ERASE_NOT_IN_PROGRESS)
        ret = manager.has_erase_completed()
        self.assertTrue(ret)

    def test_has_erase_completed_exception(self, storcli_mock):
        storcli_mock.side_effect = exception.StorcliOperationError(reason='')
        self.assertRaises(exception.StorcliOperationError,
                          manager.has_erase_completed)

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

    def test_erase_devices_exception(self, storcli_mock):
        storcli_mock.side_effect = exception.StorcliOperationError(reason='')
        self.assertRaises(exception.StorcliOperationError,
                          manager.erase_devices)
