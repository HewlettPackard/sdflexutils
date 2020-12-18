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

__author__ = 'HPE'
import json

from sdflexutils import exception
from sdflexutils import log
from sdflexutils.redfish import common
import sushy
from sushy.resources import base


LOG = log.get_logger(__name__)


class ActionsField(base.CompositeField):

    pass


class HPEUpdateService(base.ResourceBase):
    """Class that extends the functionality of Base resource class

    This class extends the functionality of Base resource class
    from sushy
    """
    firmware_state = base.Field(['Oem', 'Hpe', 'State'])

    def _get_firmware_update_element(self):
        """Get the url for firmware update

        :returns: firmware update url
        :raises: Missing resource error on missing url
        """
        fw_update_action = self._actions.update_firmware
        if not fw_update_action:
            raise (sushy.exceptions.
                   MissingActionError(action='#SDFlexUpdateService.UpdateAll',
                                      resource=self._path))
        return fw_update_action

    def flash_firmware(self, redfish_inst,  file_url, reinstall=False,
                       exclude_npar_fw=False):
        """Perform firmware flashing on a redfish system

        :param file_url: url to firmware bundle.
        :param redfish_inst: redfish instance.
        :param: reinstall: to force re-install the firmware components
                though the same version is present in the system.
        :param: exclude_npar_fw: to exclude flashing npar firmware in case
                someone wants only mamageability firmware to be updated.
        :raises: SDFlexError, on an error from sdflex.
        """
        action_data = {
            'ImageURI': file_url,
            'Reinstall': reinstall,
            'ExcludeNparFw': exclude_npar_fw,
        }
        target_uri = self._get_firmware_update_element().target_uri
        try:
            post_resp = self._conn.post(target_uri, data=action_data)
            post_resp = json.loads(post_resp.content.decode('utf-8'))
            task_id = post_resp.get('@odata.id')
            self.wait_for_redfish_firmware_update_to_complete(
                redfish_inst, task_id, file_url)

        except sushy.exceptions.SushyError as e:
            msg = (('The Redfish controller failed to update firmware '
                    'with file %(file)s Error %(error)s') %
                   {'file': file_url, 'error': str(e)})
            LOG.debug(msg)
            raise exception.SDFlexError(msg)

    def wait_for_redfish_firmware_update_to_complete(self, redfish_object,
                                                     task_id, file_url):
        """Continuously polls for sdflex firmware update to complete.

        :param: redfish_object: redfish instance.
        :param: task_id: task id of the firmware update task.
        :param: file_url: url to firmware bundle.
        """

        def has_firmware_flash_completed():
            """Checks for completion status of firmware update operation

            The below table shows the conditions for which the firmware update
            will be considered as DONE (be it success or error)::

            :returns: True upon firmware update completion otherwise False
            """
            # Firmware update success: if task_state is Completed and
            # task_status is OK. msg has no value in this case.
            # Firmware update fail: if task_state is Completed and
            # task_status is not OK (Warning). msg has msge contains
            # the resson for faile and the resulution for the same. Some
            # of the failure cases are FirmwareUpdateDownloadFailure.
            # FirmwareUpdateConflictError, FirmwareIncompatibleError,
            # FirmwareUpdateInternalError, FirmwareUpdateCancelledPowerOff
            # etc.,
            task_state, task_status, msg = (
                self.get_firmware_update_progress(task_id))
            if task_state == 'Completed':
                if task_status == 'OK':
                    msg1 = ("Flashing firmware bundle: %(file_url)s ... done"
                            % {'file_url': file_url})
                    LOG.info(msg1)
                else:
                    msg1 = (
                        "Flashing firmware bundle: %(file_url)s ... FAILED "
                        "due to %(msg)s" % {'file_url': file_url, 'msg': msg})
                    LOG.error(msg1)
                return True
            return False

        common.wait_for_operation_to_complete(
            has_firmware_flash_completed,
            delay_bw_retries=15,
            failover_msg='sdflex firmware update has failed.'
        )

    def get_firmware_update_progress(self, task_id):
        """Get the progress of the firmware update.

        :param: task_id: task id of the firmware update task.
        :returns: firmware update state, one of the following values
                  "New","Running","Completed".
        :returns: firmware update status.
        :returns: firmware update messages.
        """
        try:
            get_task_data = self._conn.get(task_id)
            get_task_data = json.loads(get_task_data.content.decode('utf-8'))
            task_state = get_task_data.get('TaskState')
            task_status = get_task_data.get('TaskStatus')
            msg = ''
            if (task_state == 'Completed') and (task_status != 'OK'):
                task_messages = get_task_data.get('Messages')
                resolution = task_messages[0].get('Resolution')
                msg = task_messages[0].get('Message')
                msg = msg + ' Resolution: ' + resolution
            return (task_state, task_status, msg)
        except Exception:
            LOG.debug("sdflex-rmc reset initiated waiting for it come up")
            return ('Running', 'OK', '')
