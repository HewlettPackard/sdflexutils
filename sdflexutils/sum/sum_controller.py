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


import io
import os
import re
import shutil
import tarfile
import tempfile

from oslo_concurrency import processutils
from oslo_serialization import base64
from sdflexutils import exception
from sdflexutils import utils


SUM_LOCATION = 'packages/smartupdate'


# List of log files created by SUM based firmware update.
OUTPUT_FILES = ['/var/log/sum/localhost/sum_log.txt',
                '/var/log/sum/localhost/sum_detail_log.txt']

EXIT_CODE_TO_STRING = {
    0: "The smart component was installed successfully.",
    1: ("The smart component was installed successfully, but the system "
        "must be restarted."),
    3: ("The smart component was not installed. Node is already "
        "up-to-date."),
    253: "The installation of the component failed."
}


def _execute_sum(sum_file_path, mount_point):
    """Executes the SUM based firmware update command.

    This method executes the SUM based firmware update command to update
    all the IO firmware components in the server.

    :param sum_file_path: A string with the path to the SUM binary to be
        executed
    :param mount_point: Location in which SPP iso is mounted.
    :returns: A string with the statistics of the updated/failed components.
    :raises: SUMOperationError, when the SUM based firmware update operation
        on the node fails.
    """

    try:
        location = os.path.join(mount_point, 'packages')

        # NOTE: 'packages/smartupdate' is part of the SPP ISO and is
        # available in the SPP mount point (eg:'/mount/packages/smartupdate').
        processutils.execute(sum_file_path, '--s', '--romonly',
                             '--use_location', location, '--ignore_tpm',
                             cwd=mount_point)
        exit_code = 0
        result = _parse_sum_ouput(exit_code)
        return result
    except processutils.ProcessExecutionError as e:
        result = _parse_sum_ouput(e.exit_code)
        if result:
            return result
        else:
            raise exception.SUMOperationError(reason=str(e))


def _get_log_file_data_as_encoded_content():
    """Gzip and base64 encode files and BytesIO buffers.

    This method gets the log files created by SUM based
    firmware update and tar zip the files.
    :returns: A gzipped and base64 encoded string as text.
    """
    with io.BytesIO() as fp:
        with tarfile.open(fileobj=fp, mode='w:gz') as tar:
            for f in OUTPUT_FILES:
                if os.path.isfile(f):
                    tar.add(f)

        fp.seek(0)
        return base64.encode_as_text(fp.getvalue())


def _parse_sum_ouput(exit_code):
    """Parse the SUM output log file.

    This method parses through the SUM log file in the
    default location to return the SUM update status. Sample return
    string:

    "Summary: The installation of the component failed. Status of updated
     components: Total: 5 Success: 4 Failed: 1"

    :param exit_code: A integer returned by the SUM after command execution.
    :returns: A string with the statistics of the updated/failed
        components and 'None' when the exit_code is not 0, 1, 3 or 253.
    """
    log_data = _get_log_file_data_as_encoded_content()
    if exit_code == 3:
        return {"Summary": EXIT_CODE_TO_STRING.get(exit_code),
                "Log Data": log_data}

    if exit_code in (0, 1, 2, 253):
        if os.path.exists(OUTPUT_FILES[0]):
            with open(OUTPUT_FILES[0], 'r') as f:
                output_data = f.read()

            ret_data = output_data[(output_data.find('Deployed Components:')
                                    + len('Deployed Components:')):
                                   output_data.find('Exit status:')]

            failed = 0
            success = 0
            for line in re.split('\n\n', ret_data):
                if line:
                    if 'Success' not in line:
                        failed += 1
                    else:
                        success += 1

            return {
                "Summary": (
                    "%(return_string)s Status of updated components: Total: "
                    "%(total)s Success: %(success)s Failed: %(failed)s." %
                    {"return_string": EXIT_CODE_TO_STRING.get(exit_code),
                     "total": (success + failed), "success": success,
                     "failed": failed}),
                "Log Data": log_data}

        return "UPDATE STATUS: UNKNOWN"


def update_firmware(node):
    """Performs SUM based firmware update on the node.

    This method performs SUM firmware update by mounting the
    SPP ISO on the node. It performs firmware update on all or
    some of the firmware components.

    :param node: A dictionary of the node object.
    :param url: URL of Custom ISO (SPP for SDFlex) ISO.
    :param checksum: SHA256 checksum of SPP ISO to verify the image.
    :returns: Operation Status string.
    :raises: SUMOperationError, when the mount operation fails
        or when the image validation fails.
    """
    # Validates the http image reference for SUM update ISO.
    url = node['clean_step']['args'].get('url')
    checksum = node['clean_step']['args'].get('checksum')
    try:
        utils.validate_href(url)
        rsp = utils.download_href(url)
        custom_iso_path = "/tmp/spp_iso"
        open(custom_iso_path, 'wb').write(rsp.content)
        utils.verify_image_checksum(custom_iso_path, checksum)
    except exception.ImageRefValidationFailed as e:
        raise exception.SUMOperationError(reason=e)
    except exception.ImageRefDownloadFailed as e:
        raise exception.SUMOperationError(reason=e)

    # Mounts SPP ISO on a temporary directory.
    mount_dir = tempfile.mkdtemp()
    try:
        try:
            processutils.execute("mount", custom_iso_path,
                                 mount_dir)
        except processutils.ProcessExecutionError as e:
            msg = ("Unable to mount Custom ISO %(device)s: "
                   "%(error)s" % {'device': custom_iso_path, 'error': e})
            raise exception.SUMOperationError(reason=msg)

        # Executes the SUM based firmware update by passing the 'smartupdate'
        # executable path.
        sum_file_path = os.path.join(mount_dir, SUM_LOCATION)

        result = _execute_sum(sum_file_path, mount_dir)

        processutils.trycmd("umount", mount_dir)
    finally:
        shutil.rmtree(mount_dir, ignore_errors=True)

    return result
