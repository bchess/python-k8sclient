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


class V1PersistentVolumeClaimList(object):
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
            'kind': 'str',
            'api_version': 'str',
            'metadata': 'UnversionedListMeta',
            'items': 'list[V1PersistentVolumeClaim]'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'metadata': 'metadata',
            'items': 'items'
        }

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._items = None

    @property
    def kind(self):
        """
        Gets the kind of this V1PersistentVolumeClaimList.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.3/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1PersistentVolumeClaimList.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1PersistentVolumeClaimList.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.3/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1PersistentVolumeClaimList.
        :type: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1PersistentVolumeClaimList.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.3/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1PersistentVolumeClaimList.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1PersistentVolumeClaimList.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.3/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1PersistentVolumeClaimList.
        :type: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1PersistentVolumeClaimList.
        Standard list metadata. More info: http://releases.k8s.io/release-1.3/docs/devel/api-conventions.md#types-kinds

        :return: The metadata of this V1PersistentVolumeClaimList.
        :rtype: UnversionedListMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1PersistentVolumeClaimList.
        Standard list metadata. More info: http://releases.k8s.io/release-1.3/docs/devel/api-conventions.md#types-kinds

        :param metadata: The metadata of this V1PersistentVolumeClaimList.
        :type: UnversionedListMeta
        """
        self._metadata = metadata

    @property
    def items(self):
        """
        Gets the items of this V1PersistentVolumeClaimList.
        A list of persistent volume claims. More info: http://releases.k8s.io/release-1.3/docs/user-guide/persistent-volumes.md#persistentvolumeclaims

        :return: The items of this V1PersistentVolumeClaimList.
        :rtype: list[V1PersistentVolumeClaim]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this V1PersistentVolumeClaimList.
        A list of persistent volume claims. More info: http://releases.k8s.io/release-1.3/docs/user-guide/persistent-volumes.md#persistentvolumeclaims

        :param items: The items of this V1PersistentVolumeClaimList.
        :type: list[V1PersistentVolumeClaim]
        """
        self._items = items

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
