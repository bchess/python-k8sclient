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


class V1Handler(object):
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
            '_exec': 'V1ExecAction',
            'http_get': 'V1HTTPGetAction',
            'tcp_socket': 'V1TCPSocketAction'
        }

        self.attribute_map = {
            '_exec': 'exec',
            'http_get': 'httpGet',
            'tcp_socket': 'tcpSocket'
        }

        self.__exec = None
        self._http_get = None
        self._tcp_socket = None

    @property
    def _exec(self):
        """
        Gets the _exec of this V1Handler.
        One and only one of the following should be specified. Exec specifies the action to take.

        :return: The _exec of this V1Handler.
        :rtype: V1ExecAction
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        """
        Sets the _exec of this V1Handler.
        One and only one of the following should be specified. Exec specifies the action to take.

        :param _exec: The _exec of this V1Handler.
        :type: V1ExecAction
        """
        self.__exec = _exec

    @property
    def http_get(self):
        """
        Gets the http_get of this V1Handler.
        HTTPGet specifies the http request to perform.

        :return: The http_get of this V1Handler.
        :rtype: V1HTTPGetAction
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        """
        Sets the http_get of this V1Handler.
        HTTPGet specifies the http request to perform.

        :param http_get: The http_get of this V1Handler.
        :type: V1HTTPGetAction
        """
        self._http_get = http_get

    @property
    def tcp_socket(self):
        """
        Gets the tcp_socket of this V1Handler.
        TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported

        :return: The tcp_socket of this V1Handler.
        :rtype: V1TCPSocketAction
        """
        return self._tcp_socket

    @tcp_socket.setter
    def tcp_socket(self, tcp_socket):
        """
        Sets the tcp_socket of this V1Handler.
        TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported

        :param tcp_socket: The tcp_socket of this V1Handler.
        :type: V1TCPSocketAction
        """
        self._tcp_socket = tcp_socket

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
