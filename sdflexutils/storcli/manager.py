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

import json
import re
import time

from sdflexutils import exception
from sdflexutils.storcli import storcli


def has_erase_completed():
    try:
        stdout = storcli._storcli("/call/eall/sall", "show", "erase", "J")
    except exception.StorcliOperationError as e:
        raise e

    pd_erase_status_dict = json.loads(stdout)
    if any((pd['Status'] != 'Not in progress') for pd in pd_erase_status_dict[
            'Controllers'][0]['Response Data']):
        return False
    else:
        return True


def erase_devices():
    """Erase all the drives on this server.

    This method performs hardware disk erase on all the physical drives
    in this server. This erase cannot be performed on logical drives.

    :raises exception.StorcliOperationError, if a storcli operation error
        is encountered.
    """
    try:
        stdout = storcli._storcli("/call/eall/sall", "show", "all", "J")
        pd_dict = json.loads(stdout)
        pd_list = [x for x in pd_dict['Controllers'][0][
            'Response Data'].keys() if re.match(r'Drive /c\d+/e\d+/s\d+$', x)]
        for pd in pd_list:
            if pd_dict['Controllers'][0]['Response Data'][pd][0][
                    'State'] == 'UGood':
                # TODO(Kartikeya): Secure Erase
                # Secure Erase only runs on Self-Encrypting Drives (SED)
                # Currently Not Tested
                # storcli._storcli('{}'.format(pd[6:]), 'secureerase',
                #                  'force')
                if pd_dict['Controllers'][0]['Response Data'][
                        pd][0]['SED'] == 'N':
                    storcli._storcli('{}'.format(pd[6:]), 'start', 'erase',
                                     'normal', 'patternA=00000000')
        while not has_erase_completed():
            time.sleep(300)
    except exception.StorcliOperationError as e:
        raise e

    return "Erase Completed"
