# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import jcapiv2
from jcapiv2.api.commands_api import CommandsApi  # noqa: E501
from jcapiv2.rest import ApiException


class TestCommandsApi(unittest.TestCase):
    """CommandsApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv2.api.commands_api.CommandsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_graph_command_associations_list(self):
        """Test case for graph_command_associations_list

        List the associations of a Command  # noqa: E501
        """
        pass

    def test_graph_command_associations_post(self):
        """Test case for graph_command_associations_post

        Manage the associations of a Command  # noqa: E501
        """
        pass

    def test_graph_command_traverse_system(self):
        """Test case for graph_command_traverse_system

        List the Systems bound to a Command  # noqa: E501
        """
        pass

    def test_graph_command_traverse_system_group(self):
        """Test case for graph_command_traverse_system_group

        List the System Groups bound to a Command  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
