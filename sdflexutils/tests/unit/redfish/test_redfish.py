# Copyright 2019-2020 Hewlett Packard Enterprise Development LP
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

    @mock.patch.object(redfish.RedfishOperations, '_get_sushy_system')
    def test_get_current_bios_settings(self, get_system_mock):
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/bios.json', 'r') as f:
            jsonval = json.loads(f.read()).get("Default")
        get_system_mock.return_value.bios.json = jsonval
        actual_bios_data = self.sdflex_client.get_current_bios_settings()
        expected = {'BootSlots': "3,5", "HThread": "on", "RASMode": "on",
                    'UrlBootFile2': '', 'UrlBootFile': ''}
        self.assertEqual(expected, actual_bios_data)

    @mock.patch.object(redfish.RedfishOperations, '_get_sushy_system')
    def test_get_current_bios_settings_allow_all(self, get_system_mock):
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/bios.json', 'r') as f:
            jsonval = json.loads(f.read()).get("Default")
        get_system_mock.return_value.bios.json = jsonval
        actual = self.sdflex_client.get_current_bios_settings(False)
        expected = {'RASMode': 'on', 'UrlBootFile2': '',
                    'UrlBootFile': '', 'BootSlots': '3,5', 'HThread': 'on'}
        self.assertEqual(expected, actual)

    @mock.patch.object(redfish.RedfishOperations, 'get_current_bios_settings',
                       autospec=True)
    def test_get_current_bios_settings_fail(self, mock_bios_data):
        mock_bios_data.side_effect = sushy.exceptions.SushyError
        self.assertRaises(
            sushy.exceptions.SushyError,
            self.sdflex_client.get_current_bios_settings)

    @mock.patch.object(redfish.RedfishOperations, '_get_sushy_system')
    def test_get_pending_bios_settings(self, get_system_mock):
        with open('sdflexutils/tests/unit/redfish/json_samples/'
                  'pending_bios.json', 'r') as f:
            jsonval = json.loads(f.read()).get("Default")
        get_system_mock.return_value.bios.pending_attributes = jsonval
        expected = {'BootSlots': "3,5", "HThread": "on", "RASMode": "on",
                    'UrlBootFile': 'tftp://1.2.3.4/tftp/bootx.efi',
                    'UrlBootFile2': 'tftp://1.2.3.5/tftp/bootx.efi'}
        actual = self.sdflex_client.get_pending_bios_settings()
        self.assertEqual(expected, actual)

    @mock.patch.object(redfish.RedfishOperations, '_get_sushy_system')
    def test_get_pending_bios_settings_allow_all(self, get_system_mock):
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/pending_bios.json', 'r') as f:
            jsonval = json.loads(f.read()).get("Default")
        get_system_mock.return_value.bios.pending_attributes = jsonval
        expected = {'RASMode': 'on',
                    'BootSlots': '3,5', 'HThread': 'on',
                    'UrlBootFile': 'tftp://1.2.3.4/tftp/bootx.efi',
                    'UrlBootFile2': 'tftp://1.2.3.5/tftp/bootx.efi'}
        actual = self.sdflex_client.get_pending_bios_settings(False)
        self.assertEqual(expected, actual)

    @mock.patch.object(redfish.RedfishOperations, 'get_pending_bios_settings',
                       autospec=True)
    def test_get_pending_bios_settings_fail(self, mock_pending_bios_data):
        mock_pending_bios_data.side_effect = sushy.exceptions.SushyError
        self.assertRaises(
            sushy.exceptions.SushyError,
            self.sdflex_client.get_pending_bios_settings)

    @mock.patch.object(redfish.RedfishOperations, '_get_sushy_system')
    def test_set_bios_settings(self, get_system_mock):
        with open('sdflexutils/tests/unit/redfish/json_samples/'
                  'pending_bios.json', 'r') as f:
            jsonval = json.loads(f.read()).get("Default")
        get_system_mock.return_value.bios.pending_attributes = jsonval
        data = {'RASMode': 'on', 'BootSlots': '3,5', 'HThread': 'on',
                'UrlBootFile': u'tftp://1.2.3.4/tftp/bootx.efi',
                'UrlBootFile2': u'tftp://1.2.3.5/tftp/bootx.efi'}
        self.sdflex_client.set_bios_settings(data)
        pending_bios_settings = self.sdflex_client.get_pending_bios_settings()
        self.assertEqual(data, pending_bios_settings)

    @mock.patch.object(redfish.RedfishOperations, 'set_bios_settings',
                       autospec=True)
    def test_set_bios_settings_unsupported_settings(self,
                                                    mock_set_bios_setting):
        mock_set_bios_setting.side_effect = sushy.exceptions.SushyError
        data = {'Ip': u'1.2.3.5'}
        self.assertRaises(
            sushy.exceptions.SushyError,
            self.sdflex_client.set_bios_settings, data)

    @mock.patch.object(redfish.RedfishOperations, '_get_sushy_system')
    def test_set_bios_settings_empty_data(self, get_system_mock):
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/pending_bios.json', 'r') as f:
            jsonval = json.loads(f.read()).get("Default")
        get_system_mock.return_value.bios.pending_attributes = jsonval
        data = None
        self.assertRaises(
            exception.SDFlexError,
            self.sdflex_client.set_bios_settings, data)

    @mock.patch.object(redfish.RedfishOperations, 'set_bios_settings',
                       autospec=True)
    def test_set_bios_settings_fail(self, mock_pending_bios_data):
        mock_pending_bios_data.side_effect = sushy.exceptions.SushyError
        self.assertRaises(
            sushy.exceptions.SushyError,
            self.sdflex_client.set_bios_settings)

    def test_update_firmware(self):
        self.sdflex_client.update_firmware('fw_file_url')
        (self.sushy.get_update_service.return_value.flash_firmware.
         assert_called_once_with(self.sdflex_client, 'fw_file_url',
                                                     False, False))

    def test_update_firmware_reinstall(self):
        self.sdflex_client.update_firmware('fw_file_url', True, False)
        (self.sushy.get_update_service.return_value.flash_firmware.
         assert_called_once_with(self.sdflex_client, 'fw_file_url',
                                                     True, False))

    def test_update_firmware_excludenparfw(self):
        self.sdflex_client.update_firmware('fw_file_url', False, True)
        (self.sushy.get_update_service.return_value.flash_firmware.
         assert_called_once_with(self.sdflex_client, 'fw_file_url',
                                                     False, True))

    def test_update_firmware_reinstall_excludenparfw(self):
        self.sdflex_client.update_firmware('fw_file_url', True, True)
        (self.sushy.get_update_service.return_value.flash_firmware.
         assert_called_once_with(self.sdflex_client, 'fw_file_url',
                                                     True, True))

    def test_update_firmware_flash_firmware_fail(self):
        (self.sushy.get_update_service.return_value.
         flash_firmware.side_effect) = sushy.exceptions.SushyError
        self.assertRaisesRegex(
            exception.SDFlexError,
            'The Redfish controller failed to update firmware',
            self.sdflex_client.update_firmware, 'fw_file_url')

    def test_update_firmware_get_update_service_fail(self):
        self.sushy.get_update_service.side_effect = sushy.exceptions.SushyError
        self.assertRaisesRegex(
            exception.SDFlexError,
            'The Redfish controller failed to update firmware',
            self.sdflex_client.update_firmware, 'fw_file_url')

    @mock.patch.object(redfish.RedfishOperations, '_get_sushy_system')
    def test_get_vmedia_status(self, get_system_mock):
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/vmedia_config.json', 'r') as f:
            json_data = json.loads(f.read()).get("VirtualMediaConfig")
        get_system_mock.return_value.vmedia.service_enabled = json_data
        actual_vmedia_status_data = self.sdflex_client.get_vmedia_status()
        expected = {"ServiceEnabled": True}
        self.assertEqual(expected, actual_vmedia_status_data)

    @mock.patch.object(redfish.RedfishOperations, '_get_sushy_system')
    def test_get_vmedia_status_fail(self, get_system_mock):
        get_system_mock.side_effect = sushy.exceptions.SushyError
        self.assertRaises(exception.SDFlexError,
                          self.sdflex_client.get_vmedia_status)

    @mock.patch.object(redfish.RedfishOperations, '_get_sushy_system')
    def test_enable_vmedia(self, get_system_mock):
        self.sdflex_client.enable_vmedia(True)
        expected_data = {"ServiceEnabled": True}
        with open('sdflexutils/tests/unit/redfish/'
                  'json_samples/vmedia_config.json', 'r') as f:
            json_data = json.loads(f.read()).get("VirtualMediaConfig")
        get_system_mock.return_value.vmedia.service_enabled = json_data
        vmedia_status = self.sdflex_client.get_vmedia_status()
        self.assertEqual(expected_data, vmedia_status)

    def test_set_vmedia_status_invalid_value(self):
        self.assertRaises(exception.InvalidInputError,
                          self.sdflex_client.enable_vmedia,
                          'some-non-boolean')

    def test_validate_vmedia_device(self):
        device = sys_cons.VIRTUALMEDIA_DEVICE0
        self.sdflex_client.validate_vmedia_device(device)

    def test_validate_vmedia_invalid_device(self):
        self.assertRaises(exception.SDFlexError,
                          self.sdflex_client.validate_vmedia_device, 'cd2')

    @mock.patch.object(redfish.RedfishOperations, 'eject_vmedia')
    def test_eject_vmedia(self, eject_mock):
        eject_mock.return_value = None
        self.sdflex_client.eject_vmedia()
        self.sdflex_client.eject_vmedia.assert_called_once_with()

    @mock.patch.object(redfish.RedfishOperations, 'eject_vmedia')
    def test_eject_vmedia_device(self, eject_mock):
        eject_mock.return_value = None
        self.sdflex_client.eject_vmedia('cd0')
        self.sdflex_client.eject_vmedia.assert_called_once_with('cd0')

    def test_eject_vmedia_invalid_device(self):
        self.assertRaises(exception.SDFlexError,
                          self.sdflex_client.eject_vmedia, 'cd2')

    @mock.patch.object(redfish.RedfishOperations, 'insert_vmedia')
    def test_insert_vmedia_nfs(self, insert_mock):
        insert_mock.return_value = None
        url = "http://1.2.3.4:5678/xyz.iso"
        data = {'remote_image_share_type': 'nfs'}
        self.sdflex_client.insert_vmedia(url, 'cd0', data)
        insert_mock.assert_called_once_with(url, 'cd0', data)

    @mock.patch.object(redfish.RedfishOperations, 'insert_vmedia')
    def test_insert_vmedia_cifs(self, insert_mock):
        insert_mock.return_value = None
        url = "http://1.2.3.4:5678/xyz.iso"
        data = {'remote_image_user_name': 'guest',
                'remote_image_user_password': 'guest',
                'remote_image_share_type': 'cifs'}
        self.sdflex_client.insert_vmedia(url, 'cd0', data)
        insert_mock.assert_called_once_with(url, 'cd0', data)

    def test_insert_vmedia_invalid_device(self):
        url = "http://1.2.3.4:5678/xyz.iso"
        self.assertRaises(exception.SDFlexError,
                          self.sdflex_client.insert_vmedia, url, 'device1232',
                          {'remote_image_user_name': 'guest',
                           'remote_image_user_password': 'guest',
                           'remote_image_share_type': 'cifs'})
