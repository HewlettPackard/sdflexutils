# Copyright 2019 Hewlett Packard Enterprise Development LP
# Copyright 2015 Hewlett-Packard Development Company, L.P.
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

import json
import os

import jsonschema
from jsonschema import exceptions as json_schema_exc
from sdflexutils.common import constants
from sdflexutils import exception

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
RAID_CONFIG_SCHEMA = os.path.join(CURRENT_DIR, "raid_config_schema.json")


def validate(raid_config):
    """Validates the provided RAID configuration.

    This method validates the RAID configuration provided against
    a JSON schema.
    :param raid_config: The RAID configuration to be validated.
    :raises: InvalidInputError, if validation of the input fails.
    """
    raid_schema_fobj = open(RAID_CONFIG_SCHEMA, 'r')
    raid_config_schema = json.load(raid_schema_fobj)
    try:
        jsonschema.validate(raid_config, raid_config_schema)
    except json_schema_exc.ValidationError as e:
        raise exception.InvalidInputError(e.message)

    for logical_disk in raid_config['logical_disks']:

        # If user has provided 'number_of_physical_disks' or
        # 'physical_disks', validate that they have mentioned at least
        # minimum number of physical disks required for that RAID level.
        raid_level = logical_disk['raid_level']
        min_disks_reqd = constants.RAID_LEVEL_MIN_DISKS[raid_level]

        no_of_disks_specified = None
        if 'number_of_physical_disks' in logical_disk:
            no_of_disks_specified = logical_disk['number_of_physical_disks']
        elif 'physical_disks' in logical_disk:
            no_of_disks_specified = len(logical_disk['physical_disks'])

        if (no_of_disks_specified and
                no_of_disks_specified < min_disks_reqd):
            msg = ("RAID level %(raid_level)s requires at least %(number)s "
                   "disks." % {'raid_level': raid_level,
                               'number': min_disks_reqd})
            raise exception.InvalidInputError(msg)


def _sort_shared_logical_disks(logical_disks):
    """Sort the logical disks based on the following conditions.

    When the share_physical_disks is True make sure we create the volume
    which needs more disks first. This avoids the situation of insufficient
    disks for some logical volume request.

    For example,
      - two logical disk with number of disks - LD1(3), LD2(4)
      - have 4 physical disks
    In this case, if we consider LD1 first then LD2 will fail since not
    enough disks available to create LD2. So follow a order for allocation
    when share_physical_disks is True.

    Also RAID1 can share only when there is logical volume with only 2 disks.
    So make sure we create RAID 1 first when share_physical_disks is True.

    And RAID 1+0 can share only when the logical volume with even number of
    disks.
    :param logical_disks: 'logical_disks' to be sorted for shared logical
    disks.
    :returns: the logical disks sorted based the above conditions.
    """
    is_shared = (lambda x: True if ('share_physical_disks' in x and
                                    x['share_physical_disks']) else False)
    num_of_disks = (lambda x: x['number_of_physical_disks']
                    if 'number_of_physical_disks' in x else
                    constants.RAID_LEVEL_MIN_DISKS[x['raid_level']])

    # Separate logical disks based on share_physical_disks value.
    # 'logical_disks_shared' when share_physical_disks is True and
    # 'logical_disks_nonshared' when share_physical_disks is False
    logical_disks_shared = []
    logical_disks_nonshared = []
    for x in logical_disks:
        target = (logical_disks_shared if is_shared(x)
                  else logical_disks_nonshared)
        target.append(x)

    # Separete logical disks with raid 1 from the 'logical_disks_shared' into
    # 'logical_disks_shared_raid1' and remaining as
    # 'logical_disks_shared_excl_raid1'.
    logical_disks_shared_raid1 = []
    logical_disks_shared_excl_raid1 = []
    for x in logical_disks_shared:
        target = (logical_disks_shared_raid1 if x['raid_level'] == '1'
                  else logical_disks_shared_excl_raid1)
        target.append(x)

    # Sort the 'logical_disks_shared' in reverse order based on
    # 'number_of_physical_disks' attribute, if provided, otherwise minimum
    # disks required to create the logical volume.
    logical_disks_shared = sorted(logical_disks_shared_excl_raid1,
                                  reverse=True,
                                  key=num_of_disks)

    # Move RAID 1+0 to first in 'logical_disks_shared' when number of physical
    # disks needed to create logical volume cannot be shared with odd number of
    # disks and disks higher than that of RAID 1+0.
    check = True
    for x in logical_disks_shared:
        if x['raid_level'] == "1+0":
            x_num = num_of_disks(x)
            for y in logical_disks_shared:
                if y['raid_level'] != "1+0":
                    y_num = num_of_disks(y)
                    if x_num < y_num:
                        check = (True if y_num % 2 == 0 else False)
                        if check:
                            break
        if not check:
            logical_disks_shared.remove(x)
            logical_disks_shared.insert(0, x)
            check = True

    # Final 'logical_disks_sorted' list should have non shared logical disks
    # first, followed by shared logical disks with RAID 1, and finally by the
    # shared logical disks sorted based on number of disks and RAID 1+0
    # condition.
    logical_disks_sorted = (logical_disks_nonshared +
                            logical_disks_shared_raid1 +
                            logical_disks_shared)
    return logical_disks_sorted
