# Copyright 2020-2022 Hewlett Packard Enterprise Development LP
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


class VirtualMedia(object):
    """Class that extends the functionality of Virtual Media"""

    @staticmethod
    def enable_vmedia(sushy_system, set_vmedia_state):
        data = collections.defaultdict(dict)
        data['VirtualMediaConfig']['ServiceEnabled'] = set_vmedia_state
        sushy_system._conn.patch(sushy_system._path, data=data)

    @staticmethod
    def insert_vmedia_cifs(sushy_system, target_uri, data):
        sushy_system._conn.post(target_uri, data=data)
