# Copyright 2021 Hewlett Packard Enterprise Development LP
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

import collections
import json

import mock
from sdflexutils.redfish.resources.system import httpbooturi as http_boot_uri
import testtools


class HttpBootURITestCase(testtools.TestCase):

    def setUp(self):
        super(HttpBootURITestCase, self).setUp()
        self.conn = mock.MagicMock()
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/system.json', 'r') as f:
            self.conn.get.return_value.json.return_value = (
                json.loads(f.read())['default'])

        self.http_boot_uri_inst = http_boot_uri.HttpBootURI(
            self.conn, '/redfish/v1/Systems/Partition1',
            redfish_version='1.0.2')

    def test_field_attributes(self):
        self.assertEqual("http://1.2.3.4/boot.efi",
                         self.http_boot_uri_inst.httpbooturi)

    def test_set_http_boot_uri(self):
        self.http_boot_uri_inst.set_http_boot_uri("http://1.2.3.4/boot.iso")
        data = collections.defaultdict(dict)
        data['Boot']['HttpBootUri'] = "http://1.2.3.4/boot.iso"
        self.http_boot_uri_inst._conn.patch.assert_called_once_with(
            '/redfish/v1/Systems/Partition1', data=data)
