# Copyright 2019-2020 Hewlett Packard Enterprise Development LP
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

__author__ = 'HPE'
import collections

from sdflexutils import exception
from sdflexutils import log
from sdflexutils.redfish import main
from sdflexutils.redfish.resources.system import constants as sys_cons
import sushy
from sushy import auth
from sushy.resources.manager import virtual_media

"""
Class specific for Redfish APIs.
"""

GET_POWER_STATE_MAP = {
    sushy.SYSTEM_POWER_STATE_ON: 'ON',
    sushy.SYSTEM_POWER_STATE_POWERING_ON: 'ON',
    sushy.SYSTEM_POWER_STATE_OFF: 'OFF',
    sushy.SYSTEM_POWER_STATE_POWERING_OFF: 'OFF'
}

POWER_RESET_MAP = {
    'ON': sushy.RESET_ON,
    'OFF': sushy.RESET_FORCE_OFF,
}

GET_SECUREBOOT_CURRENT_BOOT_MAP = {
    sys_cons.SECUREBOOT_CURRENT_BOOT_ENABLED: True,
    sys_cons.SECUREBOOT_CURRENT_BOOT_DISABLED: False
}

VMEDIA_DEVICES = {
    sys_cons.VIRTUALMEDIA_DEVICE0:
        'redfish/v1/Systems/Partition0/VirtualMedia/CD0',
    sys_cons.VIRTUALMEDIA_DEVICE1:
        'redfish/v1/Systems/Partition0/VirtualMedia/CD1'
}


LOG = log.get_logger(__name__)


class RedfishOperations(object):
    """Operations supported on redfish based hardware.

    This class holds APIs which are currently supported via Redfish mode
    of operation. This is a growing list which needs to be updated as and when
    the existing API/s are implemented.
    """

    def __init__(self, redfish_controller_ip, username, password,
                 partition_id, bios_password=None, cacert=None,
                 root_prefix='/redfish/v1/'):
        """A class representing supported RedfishOperations

        :param redfish_controller_ip: The ip address of the Redfish controller.
        :param username: User account with admin/server-profile access
            privilege
        :param password: User account password
        :param bios_password: bios password
        :param cacert: a path to a CA_BUNDLE file or directory with
            certificates of trusted CAs. If set to None, the driver will
            ignore verifying the SSL certificate; if it's a path the driver
            will use the specified certificate or one of the certificates in
            the directory. Defaults to None.
        :param root_prefix: The default URL prefix. This part includes
            the root service and version. Defaults to /redfish/v1
        """
        super(RedfishOperations, self).__init__()
        address = (redfish_controller_ip)
        LOG.debug('Redfish address: %s', address)
        verify = False if cacert is None else cacert

        # for error reporting purpose
        self.host = redfish_controller_ip
        self.partition_id = partition_id

        try:
            basic_auth = auth.BasicAuth(username=username, password=password)
            self._sushy = main.HPESushy(redfish_controller_ip, verify=verify,
                                        auth=basic_auth)
        except sushy.exceptions.SushyError as e:
            msg = (self._('The Redfish controller at "%(controller)s" has '
                          'thrown error. Error %(error)s') %
                   {'controller': redfish_controller_ip, 'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexConnectionError(msg)

    def _(self, msg):
        """Prepends host information if available to msg and returns it."""
        try:
            return "[SDFlex %s] %s" % (self.host, msg)
        except AttributeError:
            return "[SDFlex <unknown>] %s" % msg

    def _get_sushy_system(self):
        """Get the sushy system for system_id

        :param system_id: The identity of the System resource
        :returns: the Sushy system instance
        :raises: SDFlexError
        """
        try:
            return self._sushy.get_system(self.partition_id)
        except sushy.exceptions.SushyError as e:
            msg = (self._('The Redfish System "%(partition_id)s" was '
                          'not found.Error %(error)s') %
                   {'partition_id': self.partition_id, 'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)

    def get_host_power_status(self):
        """Request the power state of the server.

        :returns: Power State of the server, 'ON' or 'OFF'
        :raises: SDFlexError, on an error from SDFlex.
        """
        sushy_system = self._get_sushy_system()
        return GET_POWER_STATE_MAP.get(sushy_system.power_state)

    def reset_server(self):
        """Resets the server.

        :raises: SDFlexError, on an error from SDFlex.
        """
        sushy_system = self._get_sushy_system()
        try:
            sushy_system.reset_system(sushy.RESET_FORCE_RESTART)
        except sushy.exceptions.SushyError as e:
            msg = (self._('The Redfish controller failed to reset server. '
                          'Error %(error)s') %
                   {'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)

    def set_host_power(self, target_value):
        """Sets the power state of the system.

        :param target_value: The target value to be set. Value can be:
            'ON' or 'OFF'.
        :raises: SDFlexError, on an error from SDFlex.
        :raises: InvalidInputError, if the target value is not
            allowed.
        """
        if target_value not in POWER_RESET_MAP:
            msg = ('The parameter "%(parameter)s" value "%(target_value)s" is '
                   'invalid. Valid values are: %(valid_power_values)s' %
                   {'parameter': 'target_value', 'target_value': target_value,
                    'valid_power_values': POWER_RESET_MAP.keys()})
            raise exception.InvalidInputError(msg)

        # Check current power status, do not act if it's in requested state.
        current_power_status = self.get_host_power_status()
        if current_power_status == target_value:
            LOG.debug(self._("Node is already in '%(target_value)s' power "
                             "state."), {'target_value': target_value})
            return

        sushy_system = self._get_sushy_system()
        try:
            sushy_system.reset_system(POWER_RESET_MAP[target_value])
        except sushy.exceptions.SushyError as e:
            msg = (self._('The Redfish controller failed to set power state '
                          'of server to %(target_value)s. Error %(error)s') %
                   {'target_value': target_value, 'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)

    def get_secure_boot_mode(self):
        """Get the status of secure boot.

        :returns: True, if enabled, else False
        :raises: SDFlexError, on an error from sdflex-rmc.
        :raises: SDFlexCommandNotSupportedError, if the command is not
                 supported on the server.
        """
        sushy_system = self._get_sushy_system()
        try:
            secure_boot_enabled = GET_SECUREBOOT_CURRENT_BOOT_MAP.get(
                sushy_system.secure_boot.current_boot)
        except sushy.exceptions.SushyError as e:
            msg = (self._('The Redfish controller failed to provide '
                          'information about secure boot on the server. '
                          'Error: %(error)s') %
                   {'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexCommandNotSupportedError(msg)

        if secure_boot_enabled:
            LOG.debug(self._("Secure boot is Enabled"))
        else:
            LOG.debug(self._("Secure boot is Disabled"))
        return secure_boot_enabled

    def _has_secure_boot(self):
        try:
            self._get_sushy_system().secure_boot
        except (exception.MissingAttributeError, sushy.exceptions.SushyError):
            return False
        return True

    def set_secure_boot_mode(self, secure_boot_enable):
        """Enable/Disable secure boot on the server.

        Resetting the server post updating this settings is needed
        from the caller side to make this into effect.
        :param secure_boot_enable: True, if secure boot needs to be
               enabled for next boot, else False.
        :raises: SDFlexError, on an error from SDFlex.
        :raises: SDFlexCommandNotSupportedError, if the command is not
                 supported on the server.
        On SDFlex, installing the secureboot default keys is taken care by
        redfish api while enabling the secureboot, no need to saperately
        install the keys. Similarly, un-installing the secureboot default keys
        is taken care by the redfish api while disabling the secureboot.
        """
        sushy_system = self._get_sushy_system()
        try:
            sushy_system.secure_boot.enable_secure_boot(secure_boot_enable)
        except exception.InvalidInputError as e:
            msg = (self._('Invalid input. Error %(error)s')
                   % {'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)
        except sushy.exceptions.SushyError as e:
            msg = (self._('The Redfish controller failed to set secure '
                          'boot settings on the server. Error: %(error)s')
                   % {'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)

    def get_current_bios_settings(self, only_allowed_settings=True):
        """Get current BIOS settings.

        :param: only_allowed_settings: True when only allowed BIOS settings
                are to be returned. If False, All the BIOS settings supported
                by sdflex-rmc are returned.
        :return: a dictionary of current BIOS settings is returned. Depending
                 on the 'only_allowed_settings', either only the allowed
                 settings are returned or all the supported settings are
                 returned.
        :raises: SDFlexError, on an error from sdflex-rmc
        """

        sushy_system = self._get_sushy_system()
        try:
            current_settings = sushy_system.bios.json
        except sushy.exceptions.SushyError as e:
            msg = (self._('The current BIOS Settings were not found. Error '
                          '%(error)s') %
                   {'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)

        attributes = current_settings.get("Attributes")
        return attributes

    def get_pending_bios_settings(self, only_allowed_settings=True):
        """Get pending BIOS settings.

        :param: only_allowed_settings: True when only allowed BIOS settings are
                to be returned. If False, All the BIOS settings supported by
                sdflex-rmc are returned.
        :return: a dictionary of pending BIOS settings is returned. Depending
                 on the 'only_allowed_settings', either only the allowed
                 settings are returned or all the supported settings are
                 returned.
        :raises: SDFlexError, on an error from sdflex-rmc.
        """

        sushy_system = self._get_sushy_system()
        try:
            settings = sushy_system.bios.pending_attributes
        except sushy.exceptions.SushyError as e:
            msg = (self._('The pending BIOS Settings were not found. Error '
                          '%(error)s') %
                   {'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)

        attributes = settings.get("Attributes")
        return attributes

    def set_bios_settings(self, data=None):
        """Sets current BIOS settings to the provided data.

        :param: only_allowed_settings: True when only allowed BIOS settings
                are to be set. If False, all the BIOS settings supported by
                sdflex-rmc and present in the 'data' are set.
        :param: data: a dictionary of BIOS settings to be applied. Depending
                on the 'only_allowed_settings', either only the allowed
                settings are set or all the supported settings that are in the
                'data' are set.
        :raises: SDFlexError, on an error from sdflex-rmc.
        """

        if not data:
            raise exception.SDFlexError("Could not apply settings with"
                                        " empty data")
        sushy_system = self._get_sushy_system()

        try:
            for key in data.keys():
                sushy_system.bios.set_attribute(key, data[key])
        except sushy.exceptions.SushyError as e:
            message_extended_info = e.body.get('@Message.ExtendedInfo')
            error_message = message_extended_info[0]['Message']

            msg = (self._("Setting the value of Bios attribute "
                          "'%(atrribute)s' is not succesfull. "
                          "Error: %(error)s") %
                   {'error': str(error_message), 'atrribute': key})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)

    def update_firmware(self, file_url, reinstall=False,
                        exclude_npar_fw=False):
        """Updates the given firmware on the server.

        :param: file_url: location of the firmware bundle.
        :param: reinstall: to force re-install the firmware components
                though the same version is present in the system.
        :param: exclude_npar_fw: to exclude flashing npar firmware in case
                someone wants only mamageability firmware to be updated.
        :raises: SDFLexError, on an error from sdflexrmc.
        """
        try:
            update_service_inst = self._sushy.get_update_service()
            update_service_inst.flash_firmware(
                self, file_url, reinstall, exclude_npar_fw)
        except sushy.exceptions.SushyError as e:
            msg = (self._('The Redfish controller failed to update firmware '
                          'with firmware %(file)s Error %(error)s') %
                   {'file': file_url, 'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)

    def validate_vmedia_device(self, device):
        if device not in VMEDIA_DEVICES:
            msg = (self._('The "%(device)s" is not a valid vmedia device.')
                   % {'device': device})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)
        else:
            return True

    def eject_vmedia(self, device):
        """Ejects the iso from the vmedia

        :raises: SDFlexError if this function couldnot eject the vmedia
        """
        if self.validate_vmedia_device(device):
            vmedia_partition_id = VMEDIA_DEVICES[device]
            try:
                self.sys_virtual_media = virtual_media.VirtualMedia(
                    self._sushy._conn, vmedia_partition_id)
                self.sys_virtual_media.eject_media()
            except sushy.exceptions.SushyError as e:
                msg = (self._('The Redfish System "%(partition_id)s" was '
                              'not found. Error %(error)s') %
                       {'partition_id': vmedia_partition_id, 'error': str(e)})
                LOG.debug(msg)
                raise exception.SDFlexError(msg)

    def insert_vmedia(self, image, device, remote_server_data, inserted=True,
                      write_protected=False):
        """Insert's the iso inside the vmedia

        :param image: The location of image which is on NFS/CIFS
        :remote_server_data : This dictionary contains remote image server
                              details
        :raises: SDFlexError if this function could not eject the vmedia
        """
        if self.validate_vmedia_device(device):
            vmedia_partition_id = VMEDIA_DEVICES[device]
            try:
                self.sys_virtual_media = virtual_media.VirtualMedia(
                    self._sushy._conn, vmedia_partition_id)
                if remote_server_data['remote_image_share_type'] == 'nfs':
                    # Incase of NFS as image share type. We use sushy object
                    # and sushy function to insert the image url into
                    # Vmedia device
                    self.sys_virtual_media.insert_media(image, inserted,
                                                        write_protected)
                elif remote_server_data['remote_image_share_type'] == 'cifs':
                    # Incase of CIFS  as image share type. We use
                    # normal post to insert the image url into Vmedia device
                    input_data = collections.defaultdict(dict)
                    input_data['UserName'] = (
                        remote_server_data['remote_image_user_name'])
                    input_data['Password'] = (
                        remote_server_data['remote_image_user_password'])
                    input_data['Image'] = image
                    input_data['Inserted'] = inserted
                    input_data['WriteProtected'] = write_protected

                    target_uri = self.sys_virtual_media._actions.insert_media.target_uri  # noqa E501

                    self._sushy._conn.post(target_uri, data=input_data)
                else:
                    msg = (self._('The %(remote_image_share_type)s is not a '
                           'valid remote_image_share_type.') %
                           {'remote_image_share_type': (
                            remote_server_data['remote_image_share_type'])}
                           )
                    LOG.debug(msg)
                    raise exception.SDFlexError(msg)
            except sushy.exceptions.SushyError as e:
                msg = (self._('The "%(device)s" is not a valid vmedia device.'
                              'Error %(error)s')
                       % {'device': device, 'error': str(e)})
                LOG.debug(msg)
                raise exception.SDFlexError(msg)

    def get_vmedia_status(self):
        """Returns the Virtual Media state whether it is Enabled or Disabled"""

        try:
            sushy_system = self._get_sushy_system()
            vmedia_status = sushy_system.vmedia.service_enabled
        except sushy.exceptions.SushyError as e:
            msg = (self._('The vmedia is not found. Error '
                          '%(error)s') %
                   {'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)
        return vmedia_status

    def enable_vmedia(self, set_vmedia_state):
        """Set's the Virtual Media state on the Sdflex Machine

        :params set_vmedia_state:To which state we have to set the vmedia
        :raises : SdflexError if a valid value is not passed to set the vmedia
        """
        if not isinstance(set_vmedia_state, bool):
            msg = ('The parameter "%(parameter)s" value "%(value)s" for '
                   'vmedia is invalid. Valid values are: True/False.' %
                   {'parameter': 'ServiceEnabled',
                    'value': set_vmedia_state})
            raise exception.InvalidInputError(msg)
        data = collections.defaultdict(dict)
        sushy_system = self._get_sushy_system()
        data['VirtualMediaConfig']['ServiceEnabled'] = set_vmedia_state

        self._sushy._conn.patch(sushy_system._path, data=data)
