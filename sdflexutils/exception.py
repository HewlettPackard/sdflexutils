# Copyright 2014 Hewlett-Packard Development Company, L.P.
# Copyright 2019-2020 Hewlett Packard Enterprise Development LP
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

"""Exception Class for sdflexutils module."""


class SDFlexUtilsException(Exception):
    """Parent class for all sdflexutils exceptions."""
    pass


class InvalidInputError(Exception):

    message = "Invalid Input: %(reason)s"

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


class SDFlexCommandNotSupportedError(SDFlexError):
    """Command not supported on the platform.

    This exception is raised when SDFlex client library fails to
    communicate properly with the sdflexrmc
    """
    def __init__(self, message, errorcode=None):
        super(SDFlexCommandNotSupportedError, self).__init__(message)


class RedfishError(SDFlexUtilsException):
    """Basic exception for errors raised by Redfish operations."""

    message = None

    def __init__(self, **kwargs):
        if self.message and kwargs:
            self.message = self.message % kwargs

        super(RedfishError, self).__init__(self.message)


class MissingAttributeError(RedfishError):
    message = ('The attribute %(attribute)s is missing from the '
               'resource %(resource)s')


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


class StorcliException(SDFlexUtilsException):

    message = "An exception occured in storcli module"

    def __init__(self, message=None, **kwargs):
        if not message:
            message = self.message

        message = message % kwargs
        super(StorcliException, self).__init__(message)


class StorcliPhysicalDisksNotFoundError(StorcliException):

    message = ("Not enough physical disks were found to create logical disk "
               "of size %(size_gb)s GB and raid level %(raid_level)s")


class StorcliOperationError(StorcliException):

    message = ("An error was encountered while doing storcli configuration: "
               "%(reason)s.")


class ImageRefValidationFailed(SDFlexUtilsException):
    message = ("Validation of image href %(image_href)s failed, "
               "reason: %(reason)s")

    def __init__(self, message=None, **kwargs):
        if not message:
            message = self.message % kwargs

        super(ImageRefValidationFailed, self).__init__(message)


class ImageRefDownloadFailed(SDFlexUtilsException):
    message = ("Downloading image href %(image_href)s failed, "
               "reason: %(reason)s")

    def __init__(self, message=None, **kwargs):
        if not message:
            message = self.message % kwargs

        super(ImageRefDownloadFailed, self).__init__(message)


class SUMOperationError(SDFlexUtilsException):
    """SUM based firmware update operation error.

    This exception is used when a problem is encountered in
    executing a SUM operation.
    """

    message = ("An error occurred while performing SUM based firmware "
               "update, reason: %(reason)s")

    def __init__(self, message=None, **kwargs):
        if not message:
            message = self.message % kwargs

        super(SUMOperationError, self).__init__(message)
