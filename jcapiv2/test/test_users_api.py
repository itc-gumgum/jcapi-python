# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import jcapiv2
from jcapiv2.rest import ApiException
from jcapiv2.apis.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """ UsersApi unit test stubs """

    def setUp(self):
        self.api = jcapiv2.apis.users_api.UsersApi()

    def tearDown(self):
        pass

    def test_graph_user_associations_list(self):
        """
        Test case for graph_user_associations_list

        List the associations of a User
        """
        pass

    def test_graph_user_associations_post(self):
        """
        Test case for graph_user_associations_post

        Manage the associations of a User
        """
        pass

    def test_graph_user_member_of(self):
        """
        Test case for graph_user_member_of

        List the parent Groups of a User
        """
        pass

    def test_graph_user_traverse_application(self):
        """
        Test case for graph_user_traverse_application

        List the Applications associated with a User
        """
        pass

    def test_graph_user_traverse_directory(self):
        """
        Test case for graph_user_traverse_directory

        List the Directories associated with a User
        """
        pass

    def test_graph_user_traverse_g_suite(self):
        """
        Test case for graph_user_traverse_g_suite

        List the G Suite instances associated with a User
        """
        pass

    def test_graph_user_traverse_ldap_server(self):
        """
        Test case for graph_user_traverse_ldap_server

        List the LDAP servers associated with a User
        """
        pass

    def test_graph_user_traverse_office365(self):
        """
        Test case for graph_user_traverse_office365

        List the Office 365 instances associated with User
        """
        pass

    def test_graph_user_traverse_radius_server(self):
        """
        Test case for graph_user_traverse_radius_server

        List the RADIUS Servers associated with a User
        """
        pass

    def test_graph_user_traverse_system(self):
        """
        Test case for graph_user_traverse_system

        List the Systems associated with a User
        """
        pass


if __name__ == '__main__':
    unittest.main()