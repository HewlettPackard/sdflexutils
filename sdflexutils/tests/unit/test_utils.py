# Copyright 2016-2020 Hewlett Packard Enterprise Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""Test class for Utils Module."""

import hashlib

import mock
import requests
from sdflexutils import exception
from sdflexutils import utils
import six
import six.moves.builtins as __builtin__
from six.moves import http_client
import testtools


class UtilsTestCase(testtools.TestCase):

    def setUp(self):
        super(UtilsTestCase, self).setUp()

    @mock.patch.object(utils, 'hashlib', autospec=True)
    def test__get_hash_object(self, hashlib_mock):
        algorithms_available = ('md5', 'sha1', 'sha224',
                                'sha256', 'sha384', 'sha512')
        hashlib_mock.algorithms_guaranteed = algorithms_available
        hashlib_mock.algorithms = algorithms_available
        # | WHEN |
        utils._get_hash_object('md5')
        utils._get_hash_object('sha1')
        utils._get_hash_object('sha224')
        utils._get_hash_object('sha256')
        utils._get_hash_object('sha384')
        utils._get_hash_object('sha512')
        # | THEN |
        calls = [mock.call.md5(), mock.call.sha1(), mock.call.sha224(),
                 mock.call.sha256(), mock.call.sha384(), mock.call.sha512()]
        hashlib_mock.assert_has_calls(calls)

    def test__get_hash_object_throws_for_invalid_or_unsupported_hash_name(
            self):
        # | WHEN | & | THEN |
        self.assertRaises(exception.InvalidInputError,
                          utils._get_hash_object,
                          'hickory-dickory-dock')

    def test_hash_file_for_sha256(self):
        # | GIVEN |
        data = b'Mary had a little lamb, its fleece as white as snow'
        file_like_object = six.BytesIO(data)
        expected = hashlib.sha256(data).hexdigest()
        # | WHEN |
        actual = utils.hash_file(file_like_object)  # using default, 'sha256'
        # | THEN |
        self.assertEqual(expected, actual)

    def test_hash_file_for_sha1(self):
        # | GIVEN |
        data = b'Mary had a little lamb, its fleece as white as snow'
        file_like_object = six.BytesIO(data)
        expected = hashlib.sha1(data).hexdigest()
        # | WHEN |
        actual = utils.hash_file(file_like_object, 'sha1')
        # | THEN |
        self.assertEqual(expected, actual)

    def test_hash_file_for_sha512(self):
        # | GIVEN |
        data = b'Mary had a little lamb, its fleece as white as snow'
        file_like_object = six.BytesIO(data)
        expected = hashlib.sha512(data).hexdigest()
        # | WHEN |
        actual = utils.hash_file(file_like_object, 'sha512')
        # | THEN |
        self.assertEqual(expected, actual)

    def test_hash_file_throws_for_invalid_or_unsupported_hash(self):
        # | GIVEN |
        data = b'Mary had a little lamb, its fleece as white as snow'
        file_like_object = six.BytesIO(data)
        # | WHEN | & | THEN |
        self.assertRaises(exception.InvalidInputError, utils.hash_file,
                          file_like_object, 'hickory-dickory-dock')

    @mock.patch.object(__builtin__, 'open', autospec=True)
    def test_verify_image_checksum(self, open_mock):
        # | GIVEN |
        data = b'Yankee Doodle went to town riding on a pony;'
        file_like_object = six.BytesIO(data)
        open_mock().__enter__.return_value = file_like_object
        actual_hash = hashlib.sha256(data).hexdigest()
        # | WHEN |
        utils.verify_image_checksum(file_like_object, actual_hash)
        # | THEN |
        # no any exception thrown

    def test_verify_image_checksum_throws_for_nonexistent_file(self):
        # | GIVEN |
        invalid_file_path = '/some/invalid/file/path'
        # | WHEN | & | THEN |
        self.assertRaises(exception.ImageRefValidationFailed,
                          utils.verify_image_checksum,
                          invalid_file_path, 'hash_xxx')

    @mock.patch.object(__builtin__, 'open', autospec=True)
    def test_verify_image_checksum_throws_for_failed_validation(self,
                                                                open_mock):
        # | GIVEN |
        data = b'Yankee Doodle went to town riding on a pony;'
        file_like_object = six.BytesIO(data)
        open_mock().__enter__.return_value = file_like_object
        invalid_hash = 'invalid_hash_value'
        # | WHEN | & | THEN |
        self.assertRaises(exception.ImageRefValidationFailed,
                          utils.verify_image_checksum,
                          file_like_object,
                          invalid_hash)

    @mock.patch.object(requests, 'head', autospec=True)
    def test_validate_href(self, head_mock):
        href = 'http://1.2.3.4/abc.iso'
        response = head_mock.return_value
        response.status_code = http_client.OK
        utils.validate_href(href)
        head_mock.assert_called_once_with(href)
        response.status_code = http_client.NO_CONTENT
        self.assertRaises(exception.ImageRefValidationFailed,
                          utils.validate_href,
                          href)
        response.status_code = http_client.BAD_REQUEST
        self.assertRaises(exception.ImageRefValidationFailed,
                          utils.validate_href, href)

    @mock.patch.object(requests, 'head', autospec=True)
    def test_validate_href_error_code(self, head_mock):
        href = 'http://1.2.3.4/abc.iso'
        head_mock.return_value.status_code = http_client.BAD_REQUEST
        self.assertRaises(exception.ImageRefValidationFailed,
                          utils.validate_href, href)
        head_mock.assert_called_once_with(href)

    @mock.patch.object(requests, 'head', autospec=True)
    def test_validate_href_error(self, head_mock):
        href = 'http://1.2.3.4/abc.iso'
        head_mock.side_effect = requests.ConnectionError()
        self.assertRaises(exception.ImageRefValidationFailed,
                          utils.validate_href, href)
        head_mock.assert_called_once_with(href)

    @mock.patch.object(utils, 'validate_href', autospec=True)
    @mock.patch.object(requests, 'get', autospec=True)
    def test_download_href(self, get_mock, validate_mock):
        rsp = validate_mock.return_value
        rsp.status_code = http_client.OK
        href = 'http://1.2.3.4/abc.iso'
        response = get_mock.return_value
        response.status_code = http_client.OK
        response.content = b'abc'
        utils.download_href(href)
        get_mock.assert_called_once_with(href)

        response.status_code = http_client.NO_CONTENT
        self.assertRaises(exception.ImageRefDownloadFailed,
                          utils.download_href,
                          href)
        response.status_code = http_client.BAD_REQUEST
        self.assertRaises(exception.ImageRefDownloadFailed,
                          utils.download_href, href)

    @mock.patch.object(utils, 'validate_href', autospec=True)
    @mock.patch.object(requests, 'get', autospec=True)
    def test_download_href_error_code(self, get_mock, validate_mock):
        rsp = validate_mock.return_value
        rsp.status_code = http_client.OK
        href = 'http://1.2.3.4/abc.iso'
        get_mock.return_value.status_code = http_client.BAD_REQUEST
        self.assertRaises(exception.ImageRefDownloadFailed,
                          utils.download_href, href)
        get_mock.assert_called_once_with(href)
        validate_mock.assert_called_once_with(href)

    @mock.patch.object(utils, 'validate_href', autospec=True)
    @mock.patch.object(requests, 'get', autospec=True)
    def test_download_href_error(self, get_mock, validate_mock):
        rsp = validate_mock.return_value
        rsp.status_code = http_client.OK
        href = 'http://1.2.3.4/abc.iso'
        get_mock.side_effect = requests.ConnectionError()
        self.assertRaises(exception.ImageRefDownloadFailed,
                          utils.download_href, href)
        get_mock.assert_called_once_with(href)
        validate_mock.assert_called_once_with(href)

    @mock.patch.object(utils, 'validate_href', autospec=True)
    @mock.patch.object(requests, 'get', autospec=True)
    def test_download_href_validate_error(self, get_mock, val_mock):
        href = 'http://1.2.3.4/abc.iso'
        val_mock.side_effect = (
            exception.ImageRefValidationFailed(reason='', image_href=href))
        self.assertRaises(exception.ImageRefDownloadFailed,
                          utils.download_href, href)
        val_mock.assert_called_once_with(href)
        self.assertFalse(get_mock.called)
