# Copyright 2019 Hewlett Packard Enterprise Development LP
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import json
import time

import mock
from sdflexutils import exception
from sdflexutils.redfish import main
from sdflexutils.redfish import redfish
from sdflexutils.redfish.resources import update_service
import sushy
import testtools


class HPEUpdateServiceTestCase(testtools.TestCase):

    @mock.patch.object(main, 'HPESushy', autospec=True)
    def setUp(self, sushy_mock):
        super(HPEUpdateServiceTestCase, self).setUp()
        self.conn = mock.MagicMock()
        self.sushy = mock.MagicMock()
        sushy_mock.return_value = self.sushy
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/update_service.json', 'r') as f:
            self.conn.get.return_value.json.return_value = json.loads(f.read())

        self.sdflex_client = redfish.RedfishOperations(
            'https://1.2.3.4', username='foo', password='bar',
            partition_id='redfish/v1/Systems/Partition1', cacert=None)
        self.us_inst = update_service.HPEUpdateService(
            self.conn, '/redfish/v1/UpdateService/1',
            redfish_version='1.0.2')

    def test__get_firmware_update_element(self):
        value = self.us_inst._get_firmware_update_element()
        expected_uri = ('/redfish/v1/UpdateService/Actions/'
                        'SDFlexUpdateService.UpdateAll')
        self.assertEqual(expected_uri, value.target_uri)

    def test__get_firmware_update_element_missing_url_action(self):
        self.us_inst._actions.update_firmware = None
        self.assertRaisesRegex(
            sushy.exceptions.MissingActionError,
            'action #SDFlexUpdateService.UpdateAll',
            self.us_inst._get_firmware_update_element)

    @mock.patch.object(time, 'sleep')
    @mock.patch.object(update_service.HPEUpdateService,
                       'wait_for_redfish_firmware_update_to_complete',
                       autospec=True)
    def test_flash_firmware(self,
                            wait_for_redfish_firmware_update_to_complete_mock,
                            sleep_mock):
        file_url = ("'https://1.1.1.1/fwdepot/hawks2/baseline_20190910_3.20."
                    "100_STABLE/hawks2-fw.tars'")
        # | GIVEN |
        target_uri = ('/redfish/v1/UpdateService/Actions/'
                      'SDFlexUpdateService.UpdateAll')
        # | WHEN |
        m = mock.MagicMock()
        m.status_code = '202'
        m.content = ('{"Messages": [], "Id": "1234",'
                     '"@odata.id": "/redfish/v1/TaskService/TaskId/1234",'
                     '"TaskState": "Completed", "TaskStatus": "OK",'
                     '"StartTime": "2019-08-23T10:48:k",'
                     '"@odata.type": "#Task.v1_1_0.Task"}').encode('ascii')
        self.conn.post.return_value = m
        self.us_inst.flash_firmware(self.sdflex_client, file_url)
        # | THEN |
        self.us_inst._conn.post.assert_called_once_with(
            target_uri, data={'ImageURI': file_url, 'ExcludeNparFw': False,
                              'Reinstall': False})
        self.assertTrue(wait_for_redfish_firmware_update_to_complete_mock.
                        called)

    @mock.patch.object(time, 'sleep')
    @mock.patch.object(update_service.HPEUpdateService,
                       'get_firmware_update_progress', autospec=True)
    def test_flash_firmware_post_fails(self, get_firmware_update_progress_mock,
                                       sleep_mock):
        msg = 'failed'
        get_firmware_update_progress_mock.return_value = ('Complete',
                                                          'Warrning', msg)
        self.us_inst._conn.post.side_effect = (
            sushy.exceptions.SushyError)
        self.assertRaisesRegex(
            exception.SDFlexError,
            'The Redfish controller failed to update firmware',
            self.us_inst.flash_firmware, self.sdflex_client, 'web_url')

    @mock.patch.object(update_service.LOG, 'info')
    @mock.patch.object(time, 'sleep')
    @mock.patch.object(update_service.HPEUpdateService,
                       'get_firmware_update_progress', autospec=True)
    def test_wait_for_redfish_firmware_update_to_complete_ok(
            self, get_firmware_update_progress_mock, sleep_mock, log_mock):
        task_id = ("'https://1.1.1.1/redfish/v1/TaskService/Tasks/1dc20966d4"
                   "e742078f37cced05b89cf7'")
        file_url = 'https://1.1.1.1:/fw_bundle.tar'
        msg = ''
        # | GIVEN |
        get_firmware_update_progress_mock.side_effect = [('Running', 'OK',
                                                          msg),
                                                         ('Completed',
                                                          'OK', msg)]
        # | WHEN |
        (self.us_inst.
         wait_for_redfish_firmware_update_to_complete(self.sdflex_client,
                                                      task_id, file_url))
        # | THEN |
        self.assertEqual(2, get_firmware_update_progress_mock.call_count)
        self.assertTrue(get_firmware_update_progress_mock.called)
        success_msg = ("Flashing firmware bundle: https://1.1.1.1:/"
                       "fw_bundle.tar ... done")
        self.assertTrue(log_mock.called)
        log_mock.assert_called_once_with(success_msg)

    @mock.patch.object(time, 'sleep')
    @mock.patch.object(update_service.HPEUpdateService,
                       'get_firmware_update_progress', autospec=True)
    def test_wait_for_redfish_firmware_update_to_complete_multiple_retries(
            self, get_firmware_update_progress_mock, sleep_mock):
        task_id = ("'https://1.1.1.1/redfish/v1/TaskService/Tasks/1dc20966d4"
                   "e742078f37cced05b89cf7'")
        file_url = 'https://1.1.1.1:/fw_bundle.tar'
        msg1 = 'failed'
        # | GIVEN |
        get_firmware_update_progress_mock.side_effect = (
            [('New', 'OK', ''), ('Running', 'OK', ''), ('Running', 'OK', ''),
             ('Running', 'OK', ''), ('Completed', 'Warning', msg1)])
        # | WHEN |
        (self.us_inst.
         wait_for_redfish_firmware_update_to_complete(self.sdflex_client,
                                                      task_id, file_url))
        # | THEN |
        self.assertEqual(5, get_firmware_update_progress_mock.call_count)

    @mock.patch.object(time, 'sleep')
    @mock.patch.object(update_service.HPEUpdateService,
                       'get_firmware_update_progress', autospec=True)
    def test_wait_for_redfish_firmware_update_to_complete_retry_on_exception(
            self, get_firmware_update_progress_mock, sleep_mock):
        task_id = ("'https://1.1.1.1/redfish/v1/TaskService/Tasks/1dc20966d4"
                   "e742078f37cced05b89cf7'")
        file_url = 'https://1.1.1.1:/fw_bundle.tar'
        msg = ''
        # | GIVEN |
        exc = exception.SDFlexError('error')
        get_firmware_update_progress_mock.side_effect = (
            [('Running', 'OK', msg), exc, ('Completed', 'OK', msg)])
        # | WHEN |
        (self.us_inst.
         wait_for_redfish_firmware_update_to_complete(self.sdflex_client,
                                                      task_id, file_url))
        # | THEN |
        self.assertEqual(3, get_firmware_update_progress_mock.call_count)

    @mock.patch.object(time, 'sleep')
    @mock.patch.object(update_service.HPEUpdateService,
                       'get_firmware_update_progress', autospec=True)
    def test_wait_for_redfish_firmware_update_to_complete_very_quick_update(
            self, get_firmware_update_progress_mock, sleep_mock):
        task_id = ("'https://1.1.1.1/redfish/v1/TaskService/Tasks/1dc20966d4"
                   "e742078f37cced05b89cf7'")
        file_url = 'https://1.1.1.1:/fw_bundle.tar'
        # | GIVEN |
        get_firmware_update_progress_mock.side_effect = [('Completed',
                                                          'OK', '')]
        # | WHEN |
        (self.us_inst.
         wait_for_redfish_firmware_update_to_complete(self.sdflex_client,
                                                      task_id, file_url))
        # | THEN |
        self.assertEqual(1, get_firmware_update_progress_mock.call_count)

    @mock.patch.object(update_service.LOG, 'error')
    @mock.patch.object(time, 'sleep')
    @mock.patch.object(update_service.HPEUpdateService,
                       'get_firmware_update_progress', autospec=True)
    def test_wait_for_redfish_firmware_update_to_complete_fail(
            self, get_firmware_update_progress_mock, sleep_mock, log_mock):
        task_id = ("'https://1.1.1.1/redfish/v1/TaskService/Tasks/1dc20966d4"
                   "e742078f37cced05b89cf7'")
        file_url = 'https://1.1.1.1:/fw_bundle.tar'
        msg1 = ("The firmware update could not start, because it needs to "
                "update hardware which requires all npars to be powered off. "
                "Resolution: Schedule time to power down all npars, then "
                "try again.")
        # | GIVEN |
        get_firmware_update_progress_mock.side_effect = (
            [('New', 'OK', ''), ('Running', 'OK', ''), ('Running', 'OK', ''),
             ('Running', 'OK', ''), ('Completed', 'Warning', msg1)])
        # | WHEN |
        (self.us_inst.
         wait_for_redfish_firmware_update_to_complete(self.sdflex_client,
                                                      task_id, file_url))
        # | THEN |
        self.assertEqual(5, get_firmware_update_progress_mock.call_count)
        self.assertTrue(get_firmware_update_progress_mock.called)
        fail_msg = ("Flashing firmware bundle: https://1.1.1.1:/fw_bundle.tar "
                    "... FAILED due to " + msg1)
        self.assertTrue(log_mock.called)
        log_mock.assert_called_once_with(fail_msg)

    @mock.patch.object(update_service.HPEUpdateService,
                       'refresh', autospec=True)
    def test_get_firmware_update_progress_exception(self, refresh_mock):
        task_id = ("'https://1.1.1.1/redfish/v1/TaskService/Tasks/1dc20966d4"
                   "e742078f37cced05b89cf7'")
        refresh_mock.side_effect = (sushy.exceptions.SushyError)
        state, status, msg = self.us_inst.get_firmware_update_progress(task_id)
        self.assertEqual(('Running', 'OK', ''), (state, status, msg))
