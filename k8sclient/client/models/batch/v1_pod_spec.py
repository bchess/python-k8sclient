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


class V1PodSpec(object):
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
            'volumes': 'list[V1Volume]',
            'containers': 'list[V1Container]',
            'restart_policy': 'str',
            'termination_grace_period_seconds': 'int',
            'active_deadline_seconds': 'int',
            'dns_policy': 'str',
            'node_selector': 'object',
            'service_account_name': 'str',
            'service_account': 'str',
            'node_name': 'str',
            'host_network': 'bool',
            'host_pid': 'bool',
            'host_ipc': 'bool',
            'security_context': 'V1PodSecurityContext',
            'image_pull_secrets': 'list[V1LocalObjectReference]',
            'hostname': 'str',
            'subdomain': 'str'
        }

        self.attribute_map = {
            'volumes': 'volumes',
            'containers': 'containers',
            'restart_policy': 'restartPolicy',
            'termination_grace_period_seconds': 'terminationGracePeriodSeconds',
            'active_deadline_seconds': 'activeDeadlineSeconds',
            'dns_policy': 'dnsPolicy',
            'node_selector': 'nodeSelector',
            'service_account_name': 'serviceAccountName',
            'service_account': 'serviceAccount',
            'node_name': 'nodeName',
            'host_network': 'hostNetwork',
            'host_pid': 'hostPID',
            'host_ipc': 'hostIPC',
            'security_context': 'securityContext',
            'image_pull_secrets': 'imagePullSecrets',
            'hostname': 'hostname',
            'subdomain': 'subdomain'
        }

        self._volumes = None
        self._containers = None
        self._restart_policy = None
        self._termination_grace_period_seconds = None
        self._active_deadline_seconds = None
        self._dns_policy = None
        self._node_selector = None
        self._service_account_name = None
        self._service_account = None
        self._node_name = None
        self._host_network = None
        self._host_pid = None
        self._host_ipc = None
        self._security_context = None
        self._image_pull_secrets = None
        self._hostname = None
        self._subdomain = None

    @property
    def volumes(self):
        """
        Gets the volumes of this V1PodSpec.
        List of volumes that can be mounted by containers belonging to the pod. More info: http://releases.k8s.io/release-1.3/docs/user-guide/volumes.md

        :return: The volumes of this V1PodSpec.
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this V1PodSpec.
        List of volumes that can be mounted by containers belonging to the pod. More info: http://releases.k8s.io/release-1.3/docs/user-guide/volumes.md

        :param volumes: The volumes of this V1PodSpec.
        :type: list[V1Volume]
        """
        self._volumes = volumes

    @property
    def containers(self):
        """
        Gets the containers of this V1PodSpec.
        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. More info: http://releases.k8s.io/release-1.3/docs/user-guide/containers.md

        :return: The containers of this V1PodSpec.
        :rtype: list[V1Container]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """
        Sets the containers of this V1PodSpec.
        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. More info: http://releases.k8s.io/release-1.3/docs/user-guide/containers.md

        :param containers: The containers of this V1PodSpec.
        :type: list[V1Container]
        """
        self._containers = containers

    @property
    def restart_policy(self):
        """
        Gets the restart_policy of this V1PodSpec.
        Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: http://releases.k8s.io/release-1.3/docs/user-guide/pod-states.md#restartpolicy

        :return: The restart_policy of this V1PodSpec.
        :rtype: str
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        """
        Sets the restart_policy of this V1PodSpec.
        Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: http://releases.k8s.io/release-1.3/docs/user-guide/pod-states.md#restartpolicy

        :param restart_policy: The restart_policy of this V1PodSpec.
        :type: str
        """
        self._restart_policy = restart_policy

    @property
    def termination_grace_period_seconds(self):
        """
        Gets the termination_grace_period_seconds of this V1PodSpec.
        Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.

        :return: The termination_grace_period_seconds of this V1PodSpec.
        :rtype: int
        """
        return self._termination_grace_period_seconds

    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, termination_grace_period_seconds):
        """
        Sets the termination_grace_period_seconds of this V1PodSpec.
        Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.

        :param termination_grace_period_seconds: The termination_grace_period_seconds of this V1PodSpec.
        :type: int
        """
        self._termination_grace_period_seconds = termination_grace_period_seconds

    @property
    def active_deadline_seconds(self):
        """
        Gets the active_deadline_seconds of this V1PodSpec.
        Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.

        :return: The active_deadline_seconds of this V1PodSpec.
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """
        Sets the active_deadline_seconds of this V1PodSpec.
        Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.

        :param active_deadline_seconds: The active_deadline_seconds of this V1PodSpec.
        :type: int
        """
        self._active_deadline_seconds = active_deadline_seconds

    @property
    def dns_policy(self):
        """
        Gets the dns_policy of this V1PodSpec.
        Set DNS policy for containers within the pod. One of 'ClusterFirst' or 'Default'. Defaults to \"ClusterFirst\".

        :return: The dns_policy of this V1PodSpec.
        :rtype: str
        """
        return self._dns_policy

    @dns_policy.setter
    def dns_policy(self, dns_policy):
        """
        Sets the dns_policy of this V1PodSpec.
        Set DNS policy for containers within the pod. One of 'ClusterFirst' or 'Default'. Defaults to \"ClusterFirst\".

        :param dns_policy: The dns_policy of this V1PodSpec.
        :type: str
        """
        self._dns_policy = dns_policy

    @property
    def node_selector(self):
        """
        Gets the node_selector of this V1PodSpec.
        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: http://releases.k8s.io/release-1.3/docs/user-guide/node-selection/README.md

        :return: The node_selector of this V1PodSpec.
        :rtype: object
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """
        Sets the node_selector of this V1PodSpec.
        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: http://releases.k8s.io/release-1.3/docs/user-guide/node-selection/README.md

        :param node_selector: The node_selector of this V1PodSpec.
        :type: object
        """
        self._node_selector = node_selector

    @property
    def service_account_name(self):
        """
        Gets the service_account_name of this V1PodSpec.
        ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: http://releases.k8s.io/release-1.3/docs/design/service_accounts.md

        :return: The service_account_name of this V1PodSpec.
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """
        Sets the service_account_name of this V1PodSpec.
        ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: http://releases.k8s.io/release-1.3/docs/design/service_accounts.md

        :param service_account_name: The service_account_name of this V1PodSpec.
        :type: str
        """
        self._service_account_name = service_account_name

    @property
    def service_account(self):
        """
        Gets the service_account of this V1PodSpec.
        DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.

        :return: The service_account of this V1PodSpec.
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """
        Sets the service_account of this V1PodSpec.
        DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.

        :param service_account: The service_account of this V1PodSpec.
        :type: str
        """
        self._service_account = service_account

    @property
    def node_name(self):
        """
        Gets the node_name of this V1PodSpec.
        NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.

        :return: The node_name of this V1PodSpec.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """
        Sets the node_name of this V1PodSpec.
        NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.

        :param node_name: The node_name of this V1PodSpec.
        :type: str
        """
        self._node_name = node_name

    @property
    def host_network(self):
        """
        Gets the host_network of this V1PodSpec.
        Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.

        :return: The host_network of this V1PodSpec.
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """
        Sets the host_network of this V1PodSpec.
        Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.

        :param host_network: The host_network of this V1PodSpec.
        :type: bool
        """
        self._host_network = host_network

    @property
    def host_pid(self):
        """
        Gets the host_pid of this V1PodSpec.
        Use the host's pid namespace. Optional: Default to false.

        :return: The host_pid of this V1PodSpec.
        :rtype: bool
        """
        return self._host_pid

    @host_pid.setter
    def host_pid(self, host_pid):
        """
        Sets the host_pid of this V1PodSpec.
        Use the host's pid namespace. Optional: Default to false.

        :param host_pid: The host_pid of this V1PodSpec.
        :type: bool
        """
        self._host_pid = host_pid

    @property
    def host_ipc(self):
        """
        Gets the host_ipc of this V1PodSpec.
        Use the host's ipc namespace. Optional: Default to false.

        :return: The host_ipc of this V1PodSpec.
        :rtype: bool
        """
        return self._host_ipc

    @host_ipc.setter
    def host_ipc(self, host_ipc):
        """
        Sets the host_ipc of this V1PodSpec.
        Use the host's ipc namespace. Optional: Default to false.

        :param host_ipc: The host_ipc of this V1PodSpec.
        :type: bool
        """
        self._host_ipc = host_ipc

    @property
    def security_context(self):
        """
        Gets the security_context of this V1PodSpec.
        SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.

        :return: The security_context of this V1PodSpec.
        :rtype: V1PodSecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """
        Sets the security_context of this V1PodSpec.
        SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.

        :param security_context: The security_context of this V1PodSpec.
        :type: V1PodSecurityContext
        """
        self._security_context = security_context

    @property
    def image_pull_secrets(self):
        """
        Gets the image_pull_secrets of this V1PodSpec.
        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: http://releases.k8s.io/release-1.3/docs/user-guide/images.md#specifying-imagepullsecrets-on-a-pod

        :return: The image_pull_secrets of this V1PodSpec.
        :rtype: list[V1LocalObjectReference]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """
        Sets the image_pull_secrets of this V1PodSpec.
        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: http://releases.k8s.io/release-1.3/docs/user-guide/images.md#specifying-imagepullsecrets-on-a-pod

        :param image_pull_secrets: The image_pull_secrets of this V1PodSpec.
        :type: list[V1LocalObjectReference]
        """
        self._image_pull_secrets = image_pull_secrets

    @property
    def hostname(self):
        """
        Gets the hostname of this V1PodSpec.
        Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.

        :return: The hostname of this V1PodSpec.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this V1PodSpec.
        Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.

        :param hostname: The hostname of this V1PodSpec.
        :type: str
        """
        self._hostname = hostname

    @property
    def subdomain(self):
        """
        Gets the subdomain of this V1PodSpec.
        If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.

        :return: The subdomain of this V1PodSpec.
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """
        Sets the subdomain of this V1PodSpec.
        If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.

        :param subdomain: The subdomain of this V1PodSpec.
        :type: str
        """
        self._subdomain = subdomain

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
