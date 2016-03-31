# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TaskAddResult(Model):
    """
    Result for a single task added as part of an add task collection operation.

    :param status: The status of the add task request. Possible values
     include: 'success', 'clienterror', 'servererror', 'unmapped'
    :type status: str
    :param task_id: The id of the task for which this is the result.
    :type task_id: str
    :param e_tag: The ETag of the task, if the task was successfully added.
    :type e_tag: str
    :param last_modified: The last modified time of the task.
    :type last_modified: datetime
    :param location: The URL of the task, if the task was successfully added.
    :type location: str
    :param error: The error encountered while attempting to add the task.
    :type error: :class:`BatchError <azure.batch.models.BatchError>`
    """ 

    _validation = {
        'status': {'required': True},
        'task_id': {'required': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'TaskAddStatus'},
        'task_id': {'key': 'taskId', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'location': {'key': 'location', 'type': 'str'},
        'error': {'key': 'error', 'type': 'BatchError'},
    }

    def __init__(self, status, task_id, e_tag=None, last_modified=None, location=None, error=None, **kwargs):
        self.status = status
        self.task_id = task_id
        self.e_tag = e_tag
        self.last_modified = last_modified
        self.location = location
        self.error = error
