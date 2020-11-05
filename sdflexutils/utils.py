# Copyright 2019-2020 Hewlett Packard Enterprise Company, L.P.
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
import hashlib

import requests
from sdflexutils import exception
from sdflexutils import log
import six
from six.moves import http_client

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


def _get_hash_object(hash_algo_name):
    """Create a hash object based on given algorithm.

    :param hash_algo_name: name of the hashing algorithm.
    :raises: InvalidInputError, on unsupported or invalid input.
    :returns: a hash object based on the given named algorithm.
    """
    algorithms = (hashlib.algorithms_guaranteed if six.PY3
                  else hashlib.algorithms)
    if hash_algo_name not in algorithms:
        msg = ("Unsupported/Invalid hash name '%s' provided."
               % hash_algo_name)
        raise exception.InvalidInputError(msg)

    return getattr(hashlib, hash_algo_name)()


def hash_file(file_like_object, hash_algo='sha256'):
    """Generate a hash for the contents of a file.

    It returns a hash of the file object as a string of double length,
    containing only hexadecimal digits. It supports all the algorithms
    hashlib does.
    :param file_like_object: file like object whose hash to be calculated.
    :param hash_algo: name of the hashing strategy, default being 'sha256'.
    :raises: InvalidInputError, on unsupported or invalid input.
    :returns: a condensed digest of the bytes of contents.
    """
    checksum = _get_hash_object(hash_algo)
    for chunk in iter(lambda: file_like_object.read(32768), b''):
        checksum.update(chunk)
    return checksum.hexdigest()


def verify_image_checksum(image_location, expected_checksum):
    """Verifies checksum (sha256) of image file against the expected one.

    This method generates the checksum of the image file on the fly and
    verifies it against the expected checksum provided as argument.

    :param image_location: location of image file whose checksum is verified.
    :param expected_checksum: checksum to be checked against
    :raises: ImageRefValidationFailed, if invalid file path or
             verification fails.
    """
    try:
        with open(image_location, 'rb') as fd:
            actual_checksum = hash_file(fd)
    except IOError as e:
        raise exception.ImageRefValidationFailed(image_href=image_location,
                                                 reason=e)

    if actual_checksum != expected_checksum:
        msg = ('Error verifying image checksum. Image %(image)s failed to '
               'verify against checksum %(checksum)s. Actual checksum is: '
               '%(actual_checksum)s' %
               {'image': image_location, 'checksum': expected_checksum,
                'actual_checksum': actual_checksum})
        raise exception.ImageRefValidationFailed(image_href=image_location,
                                                 reason=msg)


def validate_href(image_href):
    """Validate HTTP image reference.

    :param image_href: Image reference.
    :raises: exception.ImageRefValidationFailed if HEAD request failed or
        returned response code not equal to 200.
    :returns: Response to HEAD request.
    """
    try:
        response = requests.head(image_href)
        if response.status_code != http_client.OK:
            raise exception.ImageRefValidationFailed(
                image_href=image_href,
                reason=("Got HTTP code %s instead of 200 in response to "
                        "HEAD request." % response.status_code))
    except requests.RequestException as e:
        raise exception.ImageRefValidationFailed(image_href=image_href,
                                                 reason=e)
    return response


def download_href(image_href):
    """Validate HTTP image reference.

    :param image_href: Image reference.
    :raises: exception.ImageRefDownloadFailed if HEAD request failed or
        returned response code not equal to 200.
    :returns: Response to HEAD request.
    """
    try:
        validate_href(image_href)
        response = requests.get(image_href)
        if response.status_code != http_client.OK:
            raise exception.ImageRefDownloadFailed(
                image_href=image_href,
                reason=("Got HTTP code %s instead of 200 in response to "
                        "HEAD request." % response.status_code))
    except requests.RequestException as e:
        raise exception.ImageRefDownloadFailed(image_href=image_href,
                                               reason=e)
    except exception.ImageRefValidationFailed as e:
        raise exception.ImageRefDownloadFailed(image_href=image_href,
                                               reason=e)
    return response
