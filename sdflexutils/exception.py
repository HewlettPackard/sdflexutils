# Copyright 2019 Hewlett-Packard Development Company, L.P.
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

"""Exception Class for sdflexutils module."""


class SDFlexUtilsException(Exception):
    """Parent class for all sdflexutils exceptions."""
    pass


class InvalidInputError(Exception):

    message = "Invalid Input: %(reason)s"

    # Note(deray): Not mandating the user to provide the ``reason`` attribute
    # parameter while raising InvalidInputError exception. This is because of
    # backward-compatibility reasons. See its unit test file to know about its
    # different ways of usage.
    def __init__(self, message=None, **kwargs):

        if not message:
            message = self.message

            if 'reason' not in kwargs:
                kwargs['reason'] = 'Unknown'

        message = message % kwargs
        super(InvalidInputError, self).__init__(message)


class SDFlexError(SDFlexUtilsException):
    """Base Exception.

    This exception is used when a problem is encountered in
    executing an operation on the RMC.
    """
    def __init__(self, message, errorcode=None):
        super(SDFlexError, self).__init__(message)


class SDFlexConnectionError(SDFlexError):
    """Cannot connect to SDFlex.

    This exception is used to communicate an HTTP connection
    error from the SDFlex to the caller.
    """
    def __init__(self, message):
        super(SDFlexConnectionError, self).__init__(message)


class HPSSAException(SDFlexUtilsException):

    message = "An exception occured in ssa module"

    def __init__(self, message=None, **kwargs):
        if not message:
            message = self.message

        message = message % kwargs
        super(HPSSAException, self).__init__(message)


class PhysicalDisksNotFoundError(HPSSAException):

    message = ("Not enough physical disks were found to create logical disk "
               "of size %(size_gb)s GB and raid level %(raid_level)s")


class HPSSAOperationError(HPSSAException):

    message = ("An error was encountered while doing ssa configuration: "
               "%(reason)s.")
