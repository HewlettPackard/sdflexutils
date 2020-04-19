# Copyright 2015 Hewlett-Packard Development Company, L.P.
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
#
# Hewlett Packard Enterprise made changes in this file.

"""Test class for Client Module."""

import mock
from sdflexutils import client
from sdflexutils.redfish import redfish
import testtools


class TestSDFlexClient(testtools.TestCase):

    @mock.patch.object(redfish, 'RedfishOperations')
    def setUp(self, redfish_mock):
        super(TestSDFlexClient, self).setUp()
        self.redfish_return_mock = redfish_mock.return_value
        self.sdlfex_client = (
            client.SDFlexClient("1.2.3.4", "admin", "Admin",
                                "redfish/v1/Systems/Partition1",
                                cacert=None))

    def test_get_host_power_status(self):
        redfish_get_host_power_mock = (
            self.redfish_return_mock.get_host_power_status)
        self.sdlfex_client.get_host_power_status()
        redfish_get_host_power_mock.assert_called_once_with()
