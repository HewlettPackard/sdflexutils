# Copyright 2021 Hewlett Packard Enterprise Development LP
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

from sushy.resources import base


class HttpBootURI(base.ResourceBase):
    """A class representing HTTPBootUri resource"""

    httpbooturi = base.Field(['Boot', 'HttpBootUri'])

    def set_http_boot_uri(self, url):
        data = collections.defaultdict(dict)
        data['Boot']['HttpBootUri'] = url
        self._conn.patch(self.path, data=data)
