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


class V1EndpointAddress(object):
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
            'ip': 'str',
            'hostname': 'str',
            'target_ref': 'V1ObjectReference'
        }

        self.attribute_map = {
            'ip': 'ip',
            'hostname': 'hostname',
            'target_ref': 'targetRef'
        }

        self._ip = None
        self._hostname = None
        self._target_ref = None

    @property
    def ip(self):
        """
        Gets the ip of this V1EndpointAddress.
        The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready.

        :return: The ip of this V1EndpointAddress.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this V1EndpointAddress.
        The IP of this endpoint. May not be loopback (127.0.0.0/8), link-local (169.254.0.0/16), or link-local multicast ((224.0.0.0/24). IPv6 is also accepted but not fully supported on all platforms. Also, certain kubernetes components, like kube-proxy, are not IPv6 ready.

        :param ip: The ip of this V1EndpointAddress.
        :type: str
        """
        self._ip = ip

    @property
    def hostname(self):
        """
        Gets the hostname of this V1EndpointAddress.
        The Hostname of this endpoint

        :return: The hostname of this V1EndpointAddress.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this V1EndpointAddress.
        The Hostname of this endpoint

        :param hostname: The hostname of this V1EndpointAddress.
        :type: str
        """
        self._hostname = hostname

    @property
    def target_ref(self):
        """
        Gets the target_ref of this V1EndpointAddress.
        Reference to object providing the endpoint.

        :return: The target_ref of this V1EndpointAddress.
        :rtype: V1ObjectReference
        """
        return self._target_ref

    @target_ref.setter
    def target_ref(self, target_ref):
        """
        Sets the target_ref of this V1EndpointAddress.
        Reference to object providing the endpoint.

        :param target_ref: The target_ref of this V1EndpointAddress.
        :type: V1ObjectReference
        """
        self._target_ref = target_ref

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
