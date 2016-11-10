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


class V1AttachedVolume(object):
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
            'name': 'str',
            'device_path': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'device_path': 'devicePath'
        }

        self._name = None
        self._device_path = None

    @property
    def name(self):
        """
        Gets the name of this V1AttachedVolume.
        Name of the attached volume

        :return: The name of this V1AttachedVolume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1AttachedVolume.
        Name of the attached volume

        :param name: The name of this V1AttachedVolume.
        :type: str
        """
        self._name = name

    @property
    def device_path(self):
        """
        Gets the device_path of this V1AttachedVolume.
        DevicePath represents the device path where the volume should be avilable

        :return: The device_path of this V1AttachedVolume.
        :rtype: str
        """
        return self._device_path

    @device_path.setter
    def device_path(self, device_path):
        """
        Sets the device_path of this V1AttachedVolume.
        DevicePath represents the device path where the volume should be avilable

        :param device_path: The device_path of this V1AttachedVolume.
        :type: str
        """
        self._device_path = device_path

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