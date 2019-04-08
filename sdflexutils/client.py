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
"""SDFlexClient module"""

from sdflexutils import exception
from sdflexutils import log
from sdflexutils.redfish import redfish


LOG = log.get_logger(__name__)


class SDFlexClient(object):

    def __init__(self, host, username, password, partition_id, timeout=60,
                 port=443, cacert=None):
        self.redfish = redfish.RedfishOperations(host, username, password,
                                                 partition_id, cacert=cacert)

    def __getattr__(self, method_name):
        """Default method called when instance method not found."""
        try:
            method = getattr(self.redfish, method_name)

            LOG.debug(self.redfish._("Using %(class)s for method %(method)s."),
                      {'class': self.__class__,
                       'method': method_name})
        except AttributeError:
            msg = ("Method '%(method_name)s' is not defined" %
                   {'method_name': method_name})
            raise exception.SDFlexError(msg)
        return method
