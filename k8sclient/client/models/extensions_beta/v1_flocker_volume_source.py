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


class V1FlockerVolumeSource(object):
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
            'dataset_name': 'str'
        }

        self.attribute_map = {
            'dataset_name': 'datasetName'
        }

        self._dataset_name = None

    @property
    def dataset_name(self):
        """
        Gets the dataset_name of this V1FlockerVolumeSource.
        Required: the volume name. This is going to be store on metadata -> name on the payload for Flocker

        :return: The dataset_name of this V1FlockerVolumeSource.
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        """
        Sets the dataset_name of this V1FlockerVolumeSource.
        Required: the volume name. This is going to be store on metadata -> name on the payload for Flocker

        :param dataset_name: The dataset_name of this V1FlockerVolumeSource.
        :type: str
        """
        self._dataset_name = dataset_name

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
