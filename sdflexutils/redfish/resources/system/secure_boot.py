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

__author__ = 'HPE'

from sdflexutils import exception
from sdflexutils import log
from sdflexutils.redfish.resources.system import mappings
from sushy.resources import base

LOG = log.get_logger(__name__)


class SecureBoot(base.ResourceBase):
    """A class representing SecureBoot resource"""

    name = base.Field('Name')
    """secure boot resource name"""

    current_boot = base.MappedField(
        'SecureBootCurrentBoot', mappings.SECUREBOOT_CURRENT_BOOT_MAP)
    """current secure boot"""

    enable = base.Field('SecureBootEnable', required=True)
    """secure boot enable"""

    mode = base.Field('SecureBootMode')
    """secure boot mode"""

    def enable_secure_boot(self, secure_boot_enable):
        """Enable/Disable secure boot on the server.

        Caller needs to reset the server after issuing this command
        to bring this into effect.
        :param secure_boot_enable: True, if secure boot needs to be
               enabled for next boot, else False.
        :raises: InvalidInputError, if the validation of the input fails
        :raises: SushyError, on an error from sdflex-rmc.
        On SDFlex, installing the secureboot default keys is taken care by
        redfish api while enabling the secureboot, no need to saperately
        install the keys. Similarly, un-installing the secureboot default
        keys is taken care by the redfish api while disabling the secureboot.
        """
        if not isinstance(secure_boot_enable, bool):
            msg = ('The parameter "%(parameter)s" value "%(value)s" is '
                   'invalid. Valid values are: True/False.' %
                   {'parameter': 'secure_boot_enable',
                    'value': secure_boot_enable})
            raise exception.InvalidInputError(msg)

        self._conn.patch(self.path,
                         data={'SecureBootEnable': secure_boot_enable})
