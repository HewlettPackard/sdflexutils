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

import mock
from oslo_concurrency import processutils
from sdflexutils import exception
from sdflexutils.storcli import storcli
import testtools


class PrivateMethodsTestCase(testtools.TestCase):

    @mock.patch('os.path.exists')
    @mock.patch('os.chdir')
    @mock.patch.object(processutils, 'execute')
    def test__storcli(self, execute_mock, dir_mock, path_mock):
        execute_mock.return_value = ("stdout", "stderr")
        dir_mock.return_value = None
        path_mock.return_value = True
        stdout = storcli._storcli("foo", "bar")
        execute_mock.assert_called_once_with(
            "./storcli64", "foo", "bar")
        self.assertEqual("stdout", stdout)

    @mock.patch('os.path.exists')
    @mock.patch('os.chdir')
    @mock.patch.object(processutils, 'execute')
    def test__storcli_raises_os_error(self, execute_mock, dir_mock, path_mock):
        path_mock.return_value = True
        dir_mock.return_value = None
        execute_mock.side_effect = OSError
        self.assertRaises(exception.StorcliOperationError,
                          storcli._storcli, "foo", "bar")

    @mock.patch('os.path.exists')
    @mock.patch('os.chdir')
    @mock.patch.object(processutils, 'execute')
    def test__storcli_raises_process_exec_error(
            self, execute_mock, dir_mock, path_mock):
        path_mock.return_value = True
        dir_mock.return_value = None
        execute_mock.side_effect = processutils.ProcessExecutionError
        self.assertRaises(exception.StorcliOperationError,
                          storcli._storcli, "foo", "bar")
