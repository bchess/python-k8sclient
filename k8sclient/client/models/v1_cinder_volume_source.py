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


class V1CinderVolumeSource(object):
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
            'volume_id': 'str',
            'fs_type': 'str',
            'read_only': 'bool'
        }

        self.attribute_map = {
            'volume_id': 'volumeID',
            'fs_type': 'fsType',
            'read_only': 'readOnly'
        }

        self._volume_id = None
        self._fs_type = None
        self._read_only = None

    @property
    def volume_id(self):
        """
        Gets the volume_id of this V1CinderVolumeSource.
        volume id used to identify the volume in cinder More info: http://releases.k8s.io/release-1.3/examples/mysql-cinder-pd/README.md

        :return: The volume_id of this V1CinderVolumeSource.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this V1CinderVolumeSource.
        volume id used to identify the volume in cinder More info: http://releases.k8s.io/release-1.3/examples/mysql-cinder-pd/README.md

        :param volume_id: The volume_id of this V1CinderVolumeSource.
        :type: str
        """
        self._volume_id = volume_id

    @property
    def fs_type(self):
        """
        Gets the fs_type of this V1CinderVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://releases.k8s.io/release-1.3/examples/mysql-cinder-pd/README.md

        :return: The fs_type of this V1CinderVolumeSource.
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """
        Sets the fs_type of this V1CinderVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://releases.k8s.io/release-1.3/examples/mysql-cinder-pd/README.md

        :param fs_type: The fs_type of this V1CinderVolumeSource.
        :type: str
        """
        self._fs_type = fs_type

    @property
    def read_only(self):
        """
        Gets the read_only of this V1CinderVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: http://releases.k8s.io/release-1.3/examples/mysql-cinder-pd/README.md

        :return: The read_only of this V1CinderVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1CinderVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: http://releases.k8s.io/release-1.3/examples/mysql-cinder-pd/README.md

        :param read_only: The read_only of this V1CinderVolumeSource.
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
