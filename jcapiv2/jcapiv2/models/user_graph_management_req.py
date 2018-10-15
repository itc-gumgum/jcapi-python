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

from jcapiv2.models.system_graph_management_req_attributes import SystemGraphManagementReqAttributes  # noqa: F401,E501


class UserGraphManagementReq(object):
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
        'attributes': 'SystemGraphManagementReqAttributes',
        'op': 'str',
        'type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'attributes': 'attributes',
        'op': 'op',
        'type': 'type',
        'id': 'id'
    }

    def __init__(self, attributes=None, op=None, type=None, id=None):  # noqa: E501
        """UserGraphManagementReq - a model defined in Swagger"""  # noqa: E501

        self._attributes = None
        self._op = None
        self._type = None
        self._id = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        self.op = op
        self.type = type
        self.id = id

    @property
    def attributes(self):
        """Gets the attributes of this UserGraphManagementReq.  # noqa: E501


        :return: The attributes of this UserGraphManagementReq.  # noqa: E501
        :rtype: SystemGraphManagementReqAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this UserGraphManagementReq.


        :param attributes: The attributes of this UserGraphManagementReq.  # noqa: E501
        :type: SystemGraphManagementReqAttributes
        """

        self._attributes = attributes

    @property
    def op(self):
        """Gets the op of this UserGraphManagementReq.  # noqa: E501

        How to modify the graph connection.  # noqa: E501

        :return: The op of this UserGraphManagementReq.  # noqa: E501
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """Sets the op of this UserGraphManagementReq.

        How to modify the graph connection.  # noqa: E501

        :param op: The op of this UserGraphManagementReq.  # noqa: E501
        :type: str
        """
        if op is None:
            raise ValueError("Invalid value for `op`, must not be `None`")  # noqa: E501
        allowed_values = ["add", "remove", "update"]  # noqa: E501
        if op not in allowed_values:
            raise ValueError(
                "Invalid value for `op` ({0}), must be one of {1}"  # noqa: E501
                .format(op, allowed_values)
            )

        self._op = op

    @property
    def type(self):
        """Gets the type of this UserGraphManagementReq.  # noqa: E501


        :return: The type of this UserGraphManagementReq.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserGraphManagementReq.


        :param type: The type of this UserGraphManagementReq.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["active_directory", "application", "command", "g_suite", "ldap_server", "office_365", "policy", "radius_server", "system", "system_group"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def id(self):
        """Gets the id of this UserGraphManagementReq.  # noqa: E501

        The ObjectID of graph object being added or removed as an association.  # noqa: E501

        :return: The id of this UserGraphManagementReq.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserGraphManagementReq.

        The ObjectID of graph object being added or removed as an association.  # noqa: E501

        :param id: The id of this UserGraphManagementReq.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserGraphManagementReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
