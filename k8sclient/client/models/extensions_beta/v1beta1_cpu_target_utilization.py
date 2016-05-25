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


class V1beta1CPUTargetUtilization(object):
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
            'target_percentage': 'int'
        }

        self.attribute_map = {
            'target_percentage': 'targetPercentage'
        }

        self._target_percentage = None

    @property
    def target_percentage(self):
        """
        Gets the target_percentage of this V1beta1CPUTargetUtilization.
        fraction of the requested CPU that should be utilized/used, e.g. 70 means that 70% of the requested CPU should be in use.

        :return: The target_percentage of this V1beta1CPUTargetUtilization.
        :rtype: int
        """
        return self._target_percentage

    @target_percentage.setter
    def target_percentage(self, target_percentage):
        """
        Sets the target_percentage of this V1beta1CPUTargetUtilization.
        fraction of the requested CPU that should be utilized/used, e.g. 70 means that 70% of the requested CPU should be in use.

        :param target_percentage: The target_percentage of this V1beta1CPUTargetUtilization.
        :type: int
        """
        self._target_percentage = target_percentage

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
