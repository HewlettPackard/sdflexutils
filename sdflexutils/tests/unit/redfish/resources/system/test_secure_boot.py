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
from sdflexutils import exception
from sdflexutils.redfish.resources.system import constants as sys_cons
from sdflexutils.redfish.resources.system import secure_boot
import testtools


class SecureBootTestCase(testtools.TestCase):

    def setUp(self):
        super(SecureBootTestCase, self).setUp()
        self.conn = mock.MagicMock()
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/secure_boot.json', 'r') as f:
            self.conn.get.return_value.json.return_value = (
                json.loads(f.read())['default'])

        self.secure_boot_inst = secure_boot.SecureBoot(
            self.conn, '/redfish/v1/Systems/Partition1/SecureBoot',
            redfish_version='1.0.2')

    def test_field_attributes(self):
        self.assertEqual('nPartition 1 secure boot information',
                         self.secure_boot_inst.name)
        self.assertEqual(sys_cons.SECUREBOOT_CURRENT_BOOT_DISABLED,
                         self.secure_boot_inst.current_boot)
        self.assertFalse(self.secure_boot_inst.enable)
        self.assertEqual('UserMode', self.secure_boot_inst.mode)

    def test_enable_secure_boot(self):
        self.secure_boot_inst.enable_secure_boot(True)
        self.secure_boot_inst._conn.patch.assert_called_once_with(
            '/redfish/v1/Systems/Partition1/SecureBoot',
            data={'SecureBootEnable': True})

    def test_enable_secure_boot_invalid_value(self):
        self.assertRaisesRegex(
            exception.InvalidInputError,
            'The parameter "secure_boot_enable" value "some-non-boolean" is '
            'invalid. Valid values are: True/False.',
            self.secure_boot_inst.enable_secure_boot, 'some-non-boolean')
