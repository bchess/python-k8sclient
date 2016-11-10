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


class V1RBDVolumeSource(object):
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
            'monitors': 'list[str]',
            'image': 'str',
            'fs_type': 'str',
            'pool': 'str',
            'user': 'str',
            'keyring': 'str',
            'secret_ref': 'V1LocalObjectReference',
            'read_only': 'bool'
        }

        self.attribute_map = {
            'monitors': 'monitors',
            'image': 'image',
            'fs_type': 'fsType',
            'pool': 'pool',
            'user': 'user',
            'keyring': 'keyring',
            'secret_ref': 'secretRef',
            'read_only': 'readOnly'
        }

        self._monitors = None
        self._image = None
        self._fs_type = None
        self._pool = None
        self._user = None
        self._keyring = None
        self._secret_ref = None
        self._read_only = None

    @property
    def monitors(self):
        """
        Gets the monitors of this V1RBDVolumeSource.
        A collection of Ceph monitors. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :return: The monitors of this V1RBDVolumeSource.
        :rtype: list[str]
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors):
        """
        Sets the monitors of this V1RBDVolumeSource.
        A collection of Ceph monitors. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :param monitors: The monitors of this V1RBDVolumeSource.
        :type: list[str]
        """
        self._monitors = monitors

    @property
    def image(self):
        """
        Gets the image of this V1RBDVolumeSource.
        The rados image name. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :return: The image of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1RBDVolumeSource.
        The rados image name. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :param image: The image of this V1RBDVolumeSource.
        :type: str
        """
        self._image = image

    @property
    def fs_type(self):
        """
        Gets the fs_type of this V1RBDVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://releases.k8s.io/release-1.3/docs/user-guide/volumes.md#rbd

        :return: The fs_type of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """
        Sets the fs_type of this V1RBDVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://releases.k8s.io/release-1.3/docs/user-guide/volumes.md#rbd

        :param fs_type: The fs_type of this V1RBDVolumeSource.
        :type: str
        """
        self._fs_type = fs_type

    @property
    def pool(self):
        """
        Gets the pool of this V1RBDVolumeSource.
        The rados pool name. Default is rbd. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it.

        :return: The pool of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """
        Sets the pool of this V1RBDVolumeSource.
        The rados pool name. Default is rbd. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it.

        :param pool: The pool of this V1RBDVolumeSource.
        :type: str
        """
        self._pool = pool

    @property
    def user(self):
        """
        Gets the user of this V1RBDVolumeSource.
        The rados user name. Default is admin. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :return: The user of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this V1RBDVolumeSource.
        The rados user name. Default is admin. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :param user: The user of this V1RBDVolumeSource.
        :type: str
        """
        self._user = user

    @property
    def keyring(self):
        """
        Gets the keyring of this V1RBDVolumeSource.
        Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :return: The keyring of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._keyring

    @keyring.setter
    def keyring(self, keyring):
        """
        Sets the keyring of this V1RBDVolumeSource.
        Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :param keyring: The keyring of this V1RBDVolumeSource.
        :type: str
        """
        self._keyring = keyring

    @property
    def secret_ref(self):
        """
        Gets the secret_ref of this V1RBDVolumeSource.
        SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :return: The secret_ref of this V1RBDVolumeSource.
        :rtype: V1LocalObjectReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """
        Sets the secret_ref of this V1RBDVolumeSource.
        SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :param secret_ref: The secret_ref of this V1RBDVolumeSource.
        :type: V1LocalObjectReference
        """
        self._secret_ref = secret_ref

    @property
    def read_only(self):
        """
        Gets the read_only of this V1RBDVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :return: The read_only of this V1RBDVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1RBDVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/release-1.3/examples/rbd/README.md#how-to-use-it

        :param read_only: The read_only of this V1RBDVolumeSource.
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
