# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems


class V1DownwardAPIVolumeFile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'path': 'str',
            'field_ref': 'V1ObjectFieldSelector',
            'resource_field_ref': 'V1ResourceFieldSelector'
        }

        self.attribute_map = {
            'path': 'path',
            'field_ref': 'fieldRef',
            'resource_field_ref': 'resourceFieldRef'
        }

        self._path = None
        self._field_ref = None
        self._resource_field_ref = None

    @property
    def path(self):
        """
        Gets the path of this V1DownwardAPIVolumeFile.
        Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'

        :return: The path of this V1DownwardAPIVolumeFile.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1DownwardAPIVolumeFile.
        Required: Path is  the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'

        :param path: The path of this V1DownwardAPIVolumeFile.
        :type: str
        """
        self._path = path

    @property
    def field_ref(self):
        """
        Gets the field_ref of this V1DownwardAPIVolumeFile.
        Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.

        :return: The field_ref of this V1DownwardAPIVolumeFile.
        :rtype: V1ObjectFieldSelector
        """
        return self._field_ref

    @field_ref.setter
    def field_ref(self, field_ref):
        """
        Sets the field_ref of this V1DownwardAPIVolumeFile.
        Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.

        :param field_ref: The field_ref of this V1DownwardAPIVolumeFile.
        :type: V1ObjectFieldSelector
        """
        self._field_ref = field_ref

    @property
    def resource_field_ref(self):
        """
        Gets the resource_field_ref of this V1DownwardAPIVolumeFile.
        Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.

        :return: The resource_field_ref of this V1DownwardAPIVolumeFile.
        :rtype: V1ResourceFieldSelector
        """
        return self._resource_field_ref

    @resource_field_ref.setter
    def resource_field_ref(self, resource_field_ref):
        """
        Sets the resource_field_ref of this V1DownwardAPIVolumeFile.
        Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.

        :param resource_field_ref: The resource_field_ref of this V1DownwardAPIVolumeFile.
        :type: V1ResourceFieldSelector
        """
        self._resource_field_ref = resource_field_ref

    def to_dict(self):
        """
        Return model properties dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Return model properties str
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
