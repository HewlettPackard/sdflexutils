# Copyright 2019-2022 Hewlett Packard Enterprise Development LP
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

from sdflexutils.redfish.resources.system import httpbooturi
from sdflexutils.redfish.resources.system import secure_boot
from sdflexutils.redfish.resources.system import virtual_media
from sdflexutils.redfish import utils
from sushy.resources import base
from sushy.resources.system import system
from sushy import utils as sushy_utils


class HPESystem(system.System):
    """Class that extends the functionality of System resource class

    This class extends the functionality of System resource class
    from sushy
    """

    _secure_boot = None  # ref to SecureBoot instance

    vmedia = base.Field(['VirtualMediaConfig', 'ServiceEnabled'])

    @property
    @sushy_utils.cache_it
    def secure_boot(self):
        """Property to provide reference to `SecureBoot` instance

        It is calculated once when the first time it is queried. On refresh,
        this property gets reset.
        """

        return secure_boot.SecureBoot(
            self._conn, utils.get_subresource_path_by(self, 'SecureBoot'),
            redfish_version=self.redfish_version)

    @property
    def http_boot_uri(self):
        """Property to provide reference to 'HTTPBootUri' instance"""

        return httpbooturi.HttpBootURI(self._conn, self._path,
                                       redfish_version=self.redfish_version)

    @property
    def virtual_media(self):
        """Property to provide reference to 'VirtualMedia' instance"""

        return virtual_media.VirtualMedia(
            self._conn, utils.get_subresource_path_by(self, 'VirtualMedia'),
            redfish_version=self.redfish_version)
