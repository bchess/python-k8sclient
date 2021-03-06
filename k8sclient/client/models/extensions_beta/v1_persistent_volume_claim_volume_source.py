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


class V1PersistentVolumeClaimVolumeSource(object):
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
            'claim_name': 'str',
            'read_only': 'bool'
        }

        self.attribute_map = {
            'claim_name': 'claimName',
            'read_only': 'readOnly'
        }

        self._claim_name = None
        self._read_only = None

    @property
    def claim_name(self):
        """
        Gets the claim_name of this V1PersistentVolumeClaimVolumeSource.
        ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: http://releases.k8s.io/release-1.3/docs/user-guide/persistent-volumes.md#persistentvolumeclaims

        :return: The claim_name of this V1PersistentVolumeClaimVolumeSource.
        :rtype: str
        """
        return self._claim_name

    @claim_name.setter
    def claim_name(self, claim_name):
        """
        Sets the claim_name of this V1PersistentVolumeClaimVolumeSource.
        ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: http://releases.k8s.io/release-1.3/docs/user-guide/persistent-volumes.md#persistentvolumeclaims

        :param claim_name: The claim_name of this V1PersistentVolumeClaimVolumeSource.
        :type: str
        """
        self._claim_name = claim_name

    @property
    def read_only(self):
        """
        Gets the read_only of this V1PersistentVolumeClaimVolumeSource.
        Will force the ReadOnly setting in VolumeMounts. Default false.

        :return: The read_only of this V1PersistentVolumeClaimVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1PersistentVolumeClaimVolumeSource.
        Will force the ReadOnly setting in VolumeMounts. Default false.

        :param read_only: The read_only of this V1PersistentVolumeClaimVolumeSource.
        :type: bool
        """
        self._read_only = read_only

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
