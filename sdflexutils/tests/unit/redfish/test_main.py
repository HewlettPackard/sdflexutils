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

import mock
from sdflexutils.redfish import main
from sdflexutils.redfish.resources.system import system
from sdflexutils.redfish.resources import update_service
from sushy import connector as sushy_connector
import testtools


class HPESushyTestCase(testtools.TestCase):

    @mock.patch.object(sushy_connector, 'Connector', autospec=True)
    def setUp(self, mock_connector):
        super(HPESushyTestCase, self).setUp()
        self.conn = mock.Mock()
        mock_connector.return_value = self.conn
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/root.json', 'r') as f:
            self.conn.get.return_value.json.return_value = (json.load(f))
        self.hpe_sushy = main.HPESushy('https://1.2.3.4',
                                       username='foo', password='bar',
                                       verify=True)
        mock_connector.assert_called_once_with(
            'https://1.2.3.4', verify=True)

    def test__init_throws_exception(self):
        self.assertRaises(
            ValueError, main.HPESushy, 'https://1.2.3.4',
            'foo', 'bar', auth=mock.MagicMock())

    @mock.patch.object(system, 'HPESystem', autospec=True)
    def test_get_system(self, mock_system):
        sys_inst = self.hpe_sushy.get_system('1234')
        self.assertIsInstance(sys_inst,
                              system.HPESystem.__class__)
        mock_system.assert_called_once_with(self.hpe_sushy._conn,
                                            '1234',
                                            self.hpe_sushy.redfish_version)

    @mock.patch.object(update_service, 'HPEUpdateService', autospec=True)
    def test_get_update_service_ah(self, mock_update_service):
        self.hpe_sushy._get_action_list = mock.Mock()
        self.hpe_sushy._get_action_list.return_value = [
            'Oem', 'Hpe', '#SDFlexUpdateService.UpdateAll']
        us_inst = self.hpe_sushy.get_update_service()
        self.assertIsInstance(us_inst,
                              update_service.HPEUpdateService.__class__)
        mock_update_service.assert_called_once_with(
            self.hpe_sushy._conn, "/redfish/v1/UpdateService",
            redfish_version=self.hpe_sushy.redfish_version)

    @mock.patch.object(update_service, 'HPEUpdateService', autospec=True)
    def test_get_update_service_ch(self, mock_update_service):
        self.hpe_sushy._get_action_list = mock.Mock()
        self.hpe_sushy._get_action_list.return_value = ['Oem',
                                                        '#SD.UpdateAll']
        us_inst = self.hpe_sushy.get_update_service()
        self.assertIsInstance(us_inst,
                              update_service.HPEUpdateService.__class__)
        mock_update_service.assert_called_once_with(
            self.hpe_sushy._conn, "/redfish/v1/UpdateService",
            redfish_version=self.hpe_sushy.redfish_version)

    def test__get_action_list_ah(self):
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/update_service_ah.json', 'r') as f:
            ret_mock = mock.Mock()
            ret_mock.content = (f.read()).encode('ascii')
            self.hpe_sushy._conn.get.return_value = ret_mock

        self.assertEqual(
            self.hpe_sushy._get_action_list("/redfish/v1/UpdateService"),
            ['Oem', 'Hpe', '#SDFlexUpdateService.UpdateAll'])

    def test__get_action_list_ch(self):
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/update_service_ch.json', 'r') as f:
            ret_mock = mock.Mock()
            ret_mock.content = (f.read()).encode('ascii')
            self.hpe_sushy._conn.get.return_value = ret_mock

        self.assertEqual(
            self.hpe_sushy._get_action_list("/redfish/v1/UpdateService"),
            ['Oem', '#SD.UpdateAll'])
