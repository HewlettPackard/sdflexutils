# Copyright 2019 Hewlett Packard Enterprise Company, L.P.
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

"""
Non-SDFlex related utilities and helper functions.
"""
from sdflexutils import log

LOG = log.get_logger(__name__)


def apply_bios_properties_filter(settings, filter_to_be_applied):
    """Applies the filter to return the dict of filtered BIOS properties.

    :param settings: dict of BIOS settings on which filter to be applied.
    :param filter_to_be_applied: list of keys to be applied as filter.
    :returns: A dictionary of filtered BIOS settings.
    """

    if not settings or not filter_to_be_applied:
        return settings
    return {k: settings[k] for k in filter_to_be_applied if k in settings}
