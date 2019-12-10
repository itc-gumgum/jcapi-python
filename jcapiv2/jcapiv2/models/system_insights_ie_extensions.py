# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SystemInsightsIeExtensions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'collection_time': 'str',
        'name': 'str',
        'path': 'str',
        'registry_path': 'str',
        'system_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'collection_time': 'collection_time',
        'name': 'name',
        'path': 'path',
        'registry_path': 'registry_path',
        'system_id': 'system_id',
        'version': 'version'
    }

    def __init__(self, collection_time=None, name=None, path=None, registry_path=None, system_id=None, version=None):  # noqa: E501
        """SystemInsightsIeExtensions - a model defined in Swagger"""  # noqa: E501

        self._collection_time = None
        self._name = None
        self._path = None
        self._registry_path = None
        self._system_id = None
        self._version = None
        self.discriminator = None

        if collection_time is not None:
            self.collection_time = collection_time
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if registry_path is not None:
            self.registry_path = registry_path
        if system_id is not None:
            self.system_id = system_id
        if version is not None:
            self.version = version

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsIeExtensions.  # noqa: E501


        :return: The collection_time of this SystemInsightsIeExtensions.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsIeExtensions.


        :param collection_time: The collection_time of this SystemInsightsIeExtensions.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def name(self):
        """Gets the name of this SystemInsightsIeExtensions.  # noqa: E501


        :return: The name of this SystemInsightsIeExtensions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInsightsIeExtensions.


        :param name: The name of this SystemInsightsIeExtensions.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this SystemInsightsIeExtensions.  # noqa: E501


        :return: The path of this SystemInsightsIeExtensions.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SystemInsightsIeExtensions.


        :param path: The path of this SystemInsightsIeExtensions.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def registry_path(self):
        """Gets the registry_path of this SystemInsightsIeExtensions.  # noqa: E501


        :return: The registry_path of this SystemInsightsIeExtensions.  # noqa: E501
        :rtype: str
        """
        return self._registry_path

    @registry_path.setter
    def registry_path(self, registry_path):
        """Sets the registry_path of this SystemInsightsIeExtensions.


        :param registry_path: The registry_path of this SystemInsightsIeExtensions.  # noqa: E501
        :type: str
        """

        self._registry_path = registry_path

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsIeExtensions.  # noqa: E501


        :return: The system_id of this SystemInsightsIeExtensions.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsIeExtensions.


        :param system_id: The system_id of this SystemInsightsIeExtensions.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def version(self):
        """Gets the version of this SystemInsightsIeExtensions.  # noqa: E501


        :return: The version of this SystemInsightsIeExtensions.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SystemInsightsIeExtensions.


        :param version: The version of this SystemInsightsIeExtensions.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SystemInsightsIeExtensions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SystemInsightsIeExtensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other