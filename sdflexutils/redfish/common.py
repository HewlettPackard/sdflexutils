# Copyright 2014 Hewlett-Packard Development Company, L.P.
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

"""Common functionalities used by both sdflex-redfish."""

import time

from sdflexutils import exception
from sdflexutils import log


LOG = log.get_logger(__name__)

SDFLEX_VER_STR_PATTERN = r"\d+\.\d+"


def wait_for_operation_to_complete(
        has_operation_completed, retry_count=120, delay_bw_retries=5,
        delay_before_attempts=10, failover_exc=exception.SDFlexError,
        failover_msg=("Operation did not complete even after multiple "
                      "attempts."), is_silent_loop_exit=False):
    """Attempts the provided operation for a specified number of times.

    If it runs out of attempts, then it raises an exception. On success,
    it breaks out of the loop.
    :param has_operation_completed: the method to retry and it needs to return
                                    a boolean to indicate success or failure.
    :param retry_count: number of times the operation to be (re)tried,
                        default 120
    :param delay_bw_retries: delay in seconds before attempting after
                             each failure, default 5.
    :param delay_before_attempts: delay in seconds before beginning any
                                  operation attempt, default 10.
    :param failover_exc: the exception which gets raised in case of failure
                         upon exhausting all the attempts, default SDFlexError.
    :param failover_msg: the msg with which the exception gets raised in case
                         of failure upon exhausting all the attempts.
    :param is_silent_loop_exit: decides if exception has to be raised (in case
                                of failure upon exhausting all the attempts)
                                or not, default False (will be raised).
    :raises: failover_exc, if failure happens even after all the attempts,
             default SDFlexError.
    """
    # Delay for ``delay_before_attempts`` secs, before beginning any attempt
    time.sleep(delay_before_attempts)

    while retry_count:
        try:
            LOG.debug("Calling '%s', retries left: %d",
                      has_operation_completed.__name__, retry_count)
            if has_operation_completed():
                break
        except exception.SDFlexError:
            pass
        time.sleep(delay_bw_retries)
        retry_count -= 1
    else:
        LOG.debug("Max retries exceeded with: '%s'",
                  has_operation_completed.__name__)
        if not is_silent_loop_exit:
            raise failover_exc(failover_msg)
