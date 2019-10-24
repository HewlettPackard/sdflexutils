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

import os
import re

from oslo_concurrency import processutils
from sdflexutils import exception


def _storcli(*args):
    """Function for executing storcli command.

    This function executes storcli command if it exists.

    :param args: args to be provided to storcli command
    :returns: the stdout after running the process.
    :raises: StorcliOperationError, if an OSError or a
        processutils.ProcessExecutionError is encountered.
    """
    try:
        if os.path.exists("/opt/MegaRAID/storcli/"):
            os.chdir("/opt/MegaRAID/storcli/")
            stdout, stderr = processutils.execute("./storcli64",
                                                  *args)
    except (OSError, processutils.ProcessExecutionError) as e:
        raise exception.StorcliOperationError(reason=str(e))

    return re.sub('(\n)*(\t)*', '', stdout)
