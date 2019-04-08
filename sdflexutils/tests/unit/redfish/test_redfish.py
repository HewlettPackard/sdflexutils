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


import ddt
import mock
from sdflexutils import exception
from sdflexutils.redfish import main
from sdflexutils.redfish import redfish
from sdflexutils.redfish.resources.system import constants as sys_cons
import sushy
import testtools


@ddt.ddt
class RedfishOperationsTestCase(testtools.TestCase):

    @mock.patch.object(main, 'HPESushy', autospec=True)
    def setUp(self, sushy_mock):
        super(RedfishOperationsTestCase, self).setUp()
        self.sushy = mock.MagicMock()
        sushy_mock.return_value = self.sushy
        self.sdflex_client = redfish.RedfishOperations(
            'https://1.2.3.4', username='foo', password='bar',
            partition_id='redfish/v1/Systems/Partition1', cacert=None)
        args, kwargs = sushy_mock.call_args

    @mock.patch.object(main, 'HPESushy', autospec=True)
    def test_sushy_init_fail(self, sushy_mock):
        sushy_mock.side_effect = sushy.exceptions.SushyError
        self.assertRaisesRegex(
            exception.SDFlexConnectionError,
            'The Redfish controller at "https://1.2.3.4" has thrown error',
            redfish.RedfishOperations,
            'https://1.2.3.4', username='foo', password='bar',
            partition_id='redfish/v1/Systems/Partition1', cacert=None)

    def test__get_sushy_system_fail(self):
        self.sdflex_client._sushy.get_system.side_effect = (
            sushy.exceptions.SushyError)
        self.assertRaisesRegex(
            exception.SDFlexError,
            'The Redfish System "redfish/v1/Systems/Partition1" '
            'was not found.', self.sdflex_client._get_sushy_system)

    def test_get_host_power_status(self):
        self.sushy.get_system().power_state = sushy.SYSTEM_POWER_STATE_ON
        power_state = self.sdflex_client.get_host_power_status()
        self.assertEqual('ON', power_state)

    def test_reset_server(self):
        self.sdflex_client.reset_server()
        self.sushy.get_system().reset_system.assert_called_once_with(
            sushy.RESET_FORCE_RESTART)

    def test_reset_server_invalid_value(self):
        self.sushy.get_system().reset_system.side_effect = (
            sushy.exceptions.SushyError)
        self.assertRaisesRegex(
            exception.SDFlexError,
            'The Redfish controller failed to reset server.',
            self.sdflex_client.reset_server)

    @mock.patch.object(redfish.RedfishOperations, 'get_host_power_status')
    def test_set_host_power_change(self, get_host_power_status_mock):
        get_host_power_status_mock.return_value = 'OFF'
        self.sdflex_client.set_host_power('ON')
        self.sushy.get_system().reset_system.assert_called_once_with(
            sushy.RESET_ON)

    @mock.patch.object(redfish.RedfishOperations, 'get_host_power_status')
    def test_set_host_power_no_change(self, get_host_power_status_mock):
        get_host_power_status_mock.return_value = 'ON'
        self.sdflex_client.set_host_power('ON')
        self.assertTrue(get_host_power_status_mock.called)
        self.assertFalse(self.sushy.get_system().reset_system.called)

    @mock.patch.object(redfish.RedfishOperations, 'get_host_power_status')
    def test_set_host_power_failure(self, get_host_power_status_mock):
        get_host_power_status_mock.return_value = 'OFF'
        self.sushy.get_system().reset_system.side_effect = (
            sushy.exceptions.SushyError)
        self.assertRaisesRegex(
            exception.SDFlexError,
            'The Redfish controller failed to set power state of server to ON',
            self.sdflex_client.set_host_power, 'ON')

    def test_set_host_power_invalid_input(self):
        self.assertRaisesRegex(
            exception.InvalidInputError,
            'The parameter "target_value" value "Off" is invalid.',
            self.sdflex_client.set_host_power, 'Off')

    @mock.patch.object(redfish.LOG, 'debug', autospec=True)
    def test_get_secure_boot_mode(self, log_debug_mock):
        sushy_system_mock = self.sushy.get_system.return_value
        type(sushy_system_mock.secure_boot).current_boot = mock.PropertyMock(
            return_value=sys_cons.SECUREBOOT_CURRENT_BOOT_ENABLED)
        self.sdflex_client.get_secure_boot_mode()
        log_debug_mock.assert_called_once_with(
            '[SDFlex https://1.2.3.4] Secure boot is Enabled')

        log_debug_mock.reset_mock()
        type(sushy_system_mock.secure_boot).current_boot = mock.PropertyMock(
            return_value=sys_cons.SECUREBOOT_CURRENT_BOOT_DISABLED)
        self.sdflex_client.get_secure_boot_mode()
        log_debug_mock.assert_called_once_with(
            '[SDFlex https://1.2.3.4] Secure boot is Disabled')

    def test_get_secure_boot_mode_on_fail(self):
        sushy_system_mock = self.sushy.get_system.return_value
        type(sushy_system_mock).secure_boot = mock.PropertyMock(
            side_effect=sushy.exceptions.SushyError)
        self.assertRaisesRegex(
            exception.SDFlexCommandNotSupportedError,
            'The Redfish controller failed to provide '
            'information about secure boot on the server.',
            self.sdflex_client.get_secure_boot_mode)

    def test__has_secure_boot(self):
        sushy_system_mock = self.sushy.get_system.return_value
        type(sushy_system_mock).secure_boot = mock.PropertyMock(
            return_value='Hey I am secure_boot')
        self.assertTrue(self.sdflex_client._has_secure_boot())

    def test__has_secure_boot_on_fail(self):
        sushy_system_mock = self.sushy.get_system.return_value
        type(sushy_system_mock).secure_boot = mock.PropertyMock(
            side_effect=sushy.exceptions.SushyError)
        self.assertFalse(self.sdflex_client._has_secure_boot())
        type(sushy_system_mock).secure_boot = mock.PropertyMock(
            side_effect=exception.MissingAttributeError)
        self.assertFalse(self.sdflex_client._has_secure_boot())

    def test_set_secure_boot_mode(self):
        self.sdflex_client.set_secure_boot_mode(True)
        secure_boot_mock = self.sushy.get_system.return_value.secure_boot
        secure_boot_mock.enable_secure_boot.assert_called_once_with(True)

    def test_set_secure_boot_mode_on_fail(self):
        secure_boot_mock = self.sushy.get_system.return_value.secure_boot
        secure_boot_mock.enable_secure_boot.side_effect = (
            sushy.exceptions.SushyError)
        self.assertRaisesRegex(
            exception.SDFlexError,
            'The Redfish controller failed to set secure boot settings '
            'on the server.',
            self.sdflex_client.set_secure_boot_mode, True)

    def test_set_secure_boot_mode_for_invalid_value(self):
        secure_boot_mock = self.sushy.get_system.return_value.secure_boot
        secure_boot_mock.enable_secure_boot.side_effect = (
            exception.InvalidInputError('Invalid input'))
        self.assertRaises(
            exception.SDFlexError,
            self.sdflex_client.set_secure_boot_mode, 'some-non-boolean')
