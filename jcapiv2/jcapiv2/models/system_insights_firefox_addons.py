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


class SystemInsightsFirefoxAddons(object):
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
        'active': 'int',
        'autoupdate': 'int',
        'collection_time': 'str',
        'creator': 'str',
        'description': 'str',
        'disabled': 'int',
        'identifier': 'str',
        'location': 'str',
        'name': 'str',
        'path': 'str',
        'source_url': 'str',
        'system_id': 'str',
        'type': 'str',
        'uid': 'str',
        'version': 'str',
        'visible': 'int'
    }

    attribute_map = {
        'active': 'active',
        'autoupdate': 'autoupdate',
        'collection_time': 'collection_time',
        'creator': 'creator',
        'description': 'description',
        'disabled': 'disabled',
        'identifier': 'identifier',
        'location': 'location',
        'name': 'name',
        'path': 'path',
        'source_url': 'source_url',
        'system_id': 'system_id',
        'type': 'type',
        'uid': 'uid',
        'version': 'version',
        'visible': 'visible'
    }

    def __init__(self, active=None, autoupdate=None, collection_time=None, creator=None, description=None, disabled=None, identifier=None, location=None, name=None, path=None, source_url=None, system_id=None, type=None, uid=None, version=None, visible=None):  # noqa: E501
        """SystemInsightsFirefoxAddons - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._autoupdate = None
        self._collection_time = None
        self._creator = None
        self._description = None
        self._disabled = None
        self._identifier = None
        self._location = None
        self._name = None
        self._path = None
        self._source_url = None
        self._system_id = None
        self._type = None
        self._uid = None
        self._version = None
        self._visible = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if autoupdate is not None:
            self.autoupdate = autoupdate
        if collection_time is not None:
            self.collection_time = collection_time
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if disabled is not None:
            self.disabled = disabled
        if identifier is not None:
            self.identifier = identifier
        if location is not None:
            self.location = location
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if source_url is not None:
            self.source_url = source_url
        if system_id is not None:
            self.system_id = system_id
        if type is not None:
            self.type = type
        if uid is not None:
            self.uid = uid
        if version is not None:
            self.version = version
        if visible is not None:
            self.visible = visible

    @property
    def active(self):
        """Gets the active of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The active of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SystemInsightsFirefoxAddons.


        :param active: The active of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: int
        """

        self._active = active

    @property
    def autoupdate(self):
        """Gets the autoupdate of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The autoupdate of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: int
        """
        return self._autoupdate

    @autoupdate.setter
    def autoupdate(self, autoupdate):
        """Sets the autoupdate of this SystemInsightsFirefoxAddons.


        :param autoupdate: The autoupdate of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: int
        """

        self._autoupdate = autoupdate

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The collection_time of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsFirefoxAddons.


        :param collection_time: The collection_time of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def creator(self):
        """Gets the creator of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The creator of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this SystemInsightsFirefoxAddons.


        :param creator: The creator of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The description of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SystemInsightsFirefoxAddons.


        :param description: The description of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disabled(self):
        """Gets the disabled of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The disabled of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: int
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this SystemInsightsFirefoxAddons.


        :param disabled: The disabled of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: int
        """

        self._disabled = disabled

    @property
    def identifier(self):
        """Gets the identifier of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The identifier of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this SystemInsightsFirefoxAddons.


        :param identifier: The identifier of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def location(self):
        """Gets the location of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The location of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SystemInsightsFirefoxAddons.


        :param location: The location of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def name(self):
        """Gets the name of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The name of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInsightsFirefoxAddons.


        :param name: The name of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The path of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SystemInsightsFirefoxAddons.


        :param path: The path of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def source_url(self):
        """Gets the source_url of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The source_url of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """Sets the source_url of this SystemInsightsFirefoxAddons.


        :param source_url: The source_url of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._source_url = source_url

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The system_id of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsFirefoxAddons.


        :param system_id: The system_id of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def type(self):
        """Gets the type of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The type of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemInsightsFirefoxAddons.


        :param type: The type of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The uid of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this SystemInsightsFirefoxAddons.


        :param uid: The uid of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def version(self):
        """Gets the version of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The version of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SystemInsightsFirefoxAddons.


        :param version: The version of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def visible(self):
        """Gets the visible of this SystemInsightsFirefoxAddons.  # noqa: E501


        :return: The visible of this SystemInsightsFirefoxAddons.  # noqa: E501
        :rtype: int
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this SystemInsightsFirefoxAddons.


        :param visible: The visible of this SystemInsightsFirefoxAddons.  # noqa: E501
        :type: int
        """

        self._visible = visible

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
        if issubclass(SystemInsightsFirefoxAddons, dict):
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
        if not isinstance(other, SystemInsightsFirefoxAddons):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
