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


class V1beta1DaemonSetSpec(object):
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
            'selector': 'V1beta1LabelSelector',
            'template': 'V1PodTemplateSpec'
        }

        self.attribute_map = {
            'selector': 'selector',
            'template': 'template'
        }

        self._selector = None
        self._template = None

    @property
    def selector(self):
        """
        Gets the selector of this V1beta1DaemonSetSpec.
        Selector is a label query over pods that are managed by the daemon set. Must match in order to be controlled. If empty, defaulted to labels on Pod template. More info: http://releases.k8s.io/release-1.3/docs/user-guide/labels.md#label-selectors

        :return: The selector of this V1beta1DaemonSetSpec.
        :rtype: V1beta1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1beta1DaemonSetSpec.
        Selector is a label query over pods that are managed by the daemon set. Must match in order to be controlled. If empty, defaulted to labels on Pod template. More info: http://releases.k8s.io/release-1.3/docs/user-guide/labels.md#label-selectors

        :param selector: The selector of this V1beta1DaemonSetSpec.
        :type: V1beta1LabelSelector
        """
        self._selector = selector

    @property
    def template(self):
        """
        Gets the template of this V1beta1DaemonSetSpec.
        Template is the object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). More info: http://releases.k8s.io/release-1.3/docs/user-guide/replication-controller.md#pod-template

        :return: The template of this V1beta1DaemonSetSpec.
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this V1beta1DaemonSetSpec.
        Template is the object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). More info: http://releases.k8s.io/release-1.3/docs/user-guide/replication-controller.md#pod-template

        :param template: The template of this V1beta1DaemonSetSpec.
        :type: V1PodTemplateSpec
        """
        self._template = template

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
