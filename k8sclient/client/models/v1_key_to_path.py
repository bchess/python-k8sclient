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


class V1KeyToPath(object):
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
            'key': 'str',
            'path': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'path': 'path'
        }

        self._key = None
        self._path = None

    @property
    def key(self):
        """
        Gets the key of this V1KeyToPath.
        The key to project.

        :return: The key of this V1KeyToPath.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this V1KeyToPath.
        The key to project.

        :param key: The key of this V1KeyToPath.
        :type: str
        """
        self._key = key

    @property
    def path(self):
        """
        Gets the path of this V1KeyToPath.
        The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.

        :return: The path of this V1KeyToPath.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1KeyToPath.
        The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.

        :param path: The path of this V1KeyToPath.
        :type: str
        """
        self._path = path

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