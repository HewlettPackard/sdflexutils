# Copyright 2017-2020 Hewlett Packard Enterprise Company, L.P.
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
import shutil
import tarfile
import tempfile

import mock
from oslo_concurrency import processutils
from oslo_serialization import base64
from sdflexutils import exception
from sdflexutils.sum import sum_controller
from sdflexutils.tests.unit.sum import sum_sample_output as constants
from sdflexutils import utils
import testtools


class SUMFirmwareUpdateTest(testtools.TestCase):

    def setUp(self):
        super(SUMFirmwareUpdateTest, self).setUp()
        self.info = {'redfish_address': 'https://1.2.3.4',
                     'redfish_password': '12345678',
                     'redfish_username': 'admin',
                     'redfish_system_id': 'redfish/v1/Systems/Partition1'}
        clean_step = {
            'interface': 'management',
            'step': 'update_firmware_sum',
            'args': {'url': 'http://1.2.3.4/SPP.iso',
                     'checksum': '1234567890'}}
        self.node = {'driver_info': self.info,
                     'clean_step': clean_step}

    @mock.patch.object(sum_controller,
                       '_get_log_file_data_as_encoded_content')
    @mock.patch.object(sum_controller, 'open',
                       mock.mock_open(read_data=constants.SUM_OUTPUT_DATA))
    @mock.patch.object(os.path, 'exists')
    @mock.patch.object(processutils, 'execute')
    def test_execute_sum(self, execute_mock, exists_mock, log_mock):
        exists_mock.return_value = True
        log_mock.return_value = "aaabbbcccdddd"
        value = ("hpsum_service_x64 started successfully. Sending Shutdown "
                 "request to engine. Successfully shutdown the service.")
        execute_mock.side_effect = processutils.ProcessExecutionError(
            stdout=value, stderr=None, exit_code=0)
        ret_value = {
            'Log Data': 'aaabbbcccdddd',
            'Summary': ("The smart component was installed successfully."
                        " Status of updated components: Total: 2 Success: 2 "
                        "Failed: 0.")
            }

        stdout = sum_controller._execute_sum("/tmp/sum/packages/smartupdate",
                                             "/tmp/sum")

        self.assertEqual(ret_value, stdout)
        execute_mock.assert_called_once_with('/tmp/sum/packages/smartupdate',
                                             '--s',
                                             '--romonly', '--use_location',
                                             '/tmp/sum/packages',
                                             '--ignore_tpm',  cwd='/tmp/sum')

    @mock.patch.object(sum_controller,
                       '_get_log_file_data_as_encoded_content')
    @mock.patch.object(
        sum_controller, 'open',
        mock.mock_open(read_data=constants.SUM_OUTPUT_DATA_FAILURE))
    @mock.patch.object(os.path, 'exists')
    @mock.patch.object(processutils, 'execute')
    def test_execute_sum_update_fails(self, execute_mock, exists_mock,
                                      log_mock):
        exists_mock.return_value = True
        log_mock.return_value = "aaabbbcccdddd"
        ret = {
            'Log Data': 'aaabbbcccdddd',
            'Summary': ("The installation of the component failed. Status "
                        "of updated components: Total: 2 Success: 1 "
                        "Failed: 1.")
            }
        value = ("hpsum_service_x64 started successfully. Sending Shutdown "
                 "request to engine. Successfully shutdown the service.")
        execute_mock.side_effect = processutils.ProcessExecutionError(
            stdout=value, stderr=None, exit_code=253)

        stdout = sum_controller._execute_sum("packages/smartupdate",
                                             "/tmp/hpsum")

        self.assertEqual(ret, stdout)
        execute_mock.assert_called_once_with(
            "packages/smartupdate", "--s", "--romonly", "--use_location",
            "/tmp/hpsum/packages", "--ignore_tpm", cwd="/tmp/hpsum")

    @mock.patch.object(processutils, 'execute')
    def test_execute_sum_fails(self, execute_mock):
        value = ("Error: Cannot launch sum_service_x64 locally. Reason: "
                 "General failure.")
        execute_mock.side_effect = processutils.ProcessExecutionError(
            stdout=value, stderr=None, exit_code=255)

        ex = self.assertRaises(exception.SUMOperationError,
                               sum_controller._execute_sum,
                               "packages/smartupdate",
                               "/tmp/sum")
        self.assertIn(value, str(ex))

    def test_get_log_file_data_as_encoded_content(self):
        log_file_content = b'Sample Data for testing SUM log output'
        file_object = tempfile.NamedTemporaryFile(delete=False)
        file_object.write(log_file_content)
        file_object.close()
        sum_controller.OUTPUT_FILES = [file_object.name]

        base64_encoded_text = (sum_controller.
                               _get_log_file_data_as_encoded_content())

        tar_gzipped_content = base64.decode_as_bytes(base64_encoded_text)
        tar_file = tempfile.NamedTemporaryFile(suffix='.tar.gz', delete=False)
        tar_file.write(tar_gzipped_content)
        tar_file.close()

        with tarfile.open(name=tar_file.name) as tar:
            f = tar.extractfile(file_object.name.lstrip('/'))
            self.assertEqual(log_file_content, f.read())
        os.remove(file_object.name)
        os.remove(tar_file.name)

    @mock.patch.object(utils, 'download_href')
    @mock.patch.object(utils, 'validate_href')
    @mock.patch.object(utils, 'verify_image_checksum')
    @mock.patch.object(sum_controller, '_execute_sum')
    @mock.patch.object(os, 'listdir')
    @mock.patch.object(shutil, 'rmtree', autospec=True)
    @mock.patch.object(tempfile, 'mkdtemp', autospec=True)
    @mock.patch.object(os, 'mkdir')
    @mock.patch.object(processutils, 'execute')
    def test_update_firmware_sum(self, execute_mock, mkdir_mock,
                                 mkdtemp_mock, rmtree_mock,
                                 listdir_mock, execute_sum_mock,
                                 verify_image_mock, validate_mock,
                                 download_mock):
        execute_sum_mock.return_value = 'SUCCESS'
        listdir_mock.return_value = ['SPP_LABEL']
        response = mock.Mock()
        download_mock.return_value = response
        rsp = b'abc'
        response.content = rsp
        mkdtemp_mock.return_value = "/tempdir"
        null_output = ["", ""]
        execute_mock.side_effect = [null_output, null_output]

        ret_val = sum_controller.update_firmware(self.node)

        execute_mock.assert_any_call('mount', "/tmp/spp_iso",
                                     "/tempdir")
        execute_sum_mock.assert_any_call('/tempdir/packages/smartupdate',
                                         '/tempdir')
        execute_mock.assert_any_call('umount', "/tempdir")
        mkdtemp_mock.assert_called_once_with()
        rmtree_mock.assert_called_once_with("/tempdir", ignore_errors=True)
        self.assertEqual('SUCCESS', ret_val)

    @mock.patch.object(utils, 'validate_href')
    def test_update_firmware_throws_for_nonexistent_file(self,
                                                         validate_href_mock):
        invalid_file_path = '/some/invalid/file/path'
        value = ("Got HTTP code 503 instead of 200 in response to "
                 "HEAD request.")
        validate_href_mock.side_effect = exception.ImageRefValidationFailed(
            reason=value, image_href=invalid_file_path)

        exc = self.assertRaises(exception.SUMOperationError,
                                sum_controller.update_firmware, self.node)
        self.assertIn(value, str(exc))

    @mock.patch.object(utils, 'download_href')
    @mock.patch.object(utils, 'validate_href')
    @mock.patch.object(os, 'listdir')
    def test_update_firmware_device_file_not_found(self,
                                                   listdir_mock,
                                                   validate_mock,
                                                   download_mock):
        listdir_mock.return_value = ['SPP_LABEL']
        some_href = "http://1.1.1.1/spp"
        ex = exception.ImageRefDownloadFailed(reason="Failed",
                                              image_href=some_href)
        download_mock.side_effect = ex

        msg = ("An error occurred while performing SUM based firmware "
               "update, reason: Downloading image href http://1.1.1.1/spp "
               "failed, reason: Failed")
        exc = self.assertRaises(exception.SUMOperationError,
                                sum_controller.update_firmware, self.node)
        self.assertEqual(msg, str(exc))

    @mock.patch.object(utils, 'download_href')
    @mock.patch.object(utils, 'validate_href')
    @mock.patch.object(utils, 'verify_image_checksum')
    @mock.patch.object(os, 'listdir')
    @mock.patch.object(os.path, 'exists')
    def test_update_firmware_invalid_checksum(self, exists_mock,
                                              listdir_mock, verify_image_mock,
                                              validate_mock, download_mock):
        listdir_mock.return_value = ['SPP_LABEL']
        response = mock.Mock()
        download_mock.return_value = response
        rsp = b'abc'
        response.content = rsp

        value = ("Error verifying image checksum. Image "
                 "http://1.2.3.4/SPP.iso failed to verify against checksum "
                 "123456789. Actual checksum is: xxxxxxxx")

        verify_image_mock.side_effect = exception.ImageRefValidationFailed(
            reason=value, image_href='http://1.2.3.4/SPP.iso')

        self.assertRaisesRegex(exception.SUMOperationError, value,
                               sum_controller.update_firmware, self.node)

        verify_image_mock.assert_called_once_with(
            '/tmp/spp_iso', '1234567890')

    @mock.patch.object(utils, 'download_href')
    @mock.patch.object(utils, 'validate_href')
    @mock.patch.object(utils, 'verify_image_checksum')
    @mock.patch.object(processutils, 'execute')
    @mock.patch.object(tempfile, 'mkdtemp', autospec=True)
    @mock.patch.object(os, 'mkdir')
    @mock.patch.object(os.path, 'exists')
    @mock.patch.object(os, 'listdir')
    def test_update_firmware_mount_fails(self, listdir_mock,
                                         exists_mock, mkdir_mock,
                                         mkdtemp_mock, execute_mock,
                                         verify_image_mock, validate_mock,
                                         download_mock):
        listdir_mock.return_value = ['SPP_LABEL']
        mkdtemp_mock.return_value = "/tempdir"
        response = mock.Mock()
        download_mock.return_value = response
        rsp = b'abc'
        response.content = rsp
        execute_mock.side_effect = processutils.ProcessExecutionError

        msg = ("Unable to mount Custom ISO /tmp/spp_iso")
        exc = self.assertRaises(exception.SUMOperationError,
                                sum_controller.update_firmware, self.node)
        self.assertIn(msg, str(exc))

    @mock.patch.object(sum_controller,
                       '_get_log_file_data_as_encoded_content')
    @mock.patch.object(sum_controller, 'open',
                       mock.mock_open(read_data=constants.SUM_OUTPUT_DATA))
    @mock.patch.object(os.path, 'exists')
    def test__parse_sum_ouput(self, exists_mock, log_mock):
        exists_mock.return_value = True
        log_mock.return_value = "aaabbbcccdddd"
        expt_ret = {'Log Data': 'aaabbbcccdddd',
                    'Summary': ("The smart component was installed "
                                "successfully. Status of updated components: "
                                "Total: 2 Success: 2 Failed: 0.")}

        ret = sum_controller._parse_sum_ouput(0)

        exists_mock.assert_called_once_with(sum_controller.OUTPUT_FILES[0])
        self.assertEqual(expt_ret, ret)

    @mock.patch.object(sum_controller,
                       '_get_log_file_data_as_encoded_content')
    @mock.patch.object(
        sum_controller, 'open',
        mock.mock_open(read_data=constants.SUM_OUTPUT_DATA_FAILURE))
    @mock.patch.object(os.path, 'exists')
    def test__parse_sum_ouput_some_failed(self, exists_mock, log_mock):
        exists_mock.return_value = True
        log_mock.return_value = "aaabbbcccdddd"
        expt_ret = {'Log Data': 'aaabbbcccdddd',
                    'Summary': ("The installation of the component failed. "
                                "Status of updated components: Total: 2 "
                                "Success: 1 Failed: 1.")}

        ret = sum_controller._parse_sum_ouput(253)

        exists_mock.assert_called_once_with(sum_controller.OUTPUT_FILES[0])
        self.assertEqual(expt_ret, ret)

    @mock.patch.object(os.path, 'exists')
    def test__parse_sum_ouput_fails(self, exists_mock):
        exists_mock.return_value = False
        expt_ret = ("UPDATE STATUS: UNKNOWN")

        ret = sum_controller._parse_sum_ouput(1)

        exists_mock.assert_called_once_with(sum_controller.OUTPUT_FILES[0])
        self.assertEqual(expt_ret, ret)
