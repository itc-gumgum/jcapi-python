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
from jcapiv2.api.bulk_job_requests_api import BulkJobRequestsApi  # noqa: E501
from jcapiv2.rest import ApiException


class TestBulkJobRequestsApi(unittest.TestCase):
    """BulkJobRequestsApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv2.api.bulk_job_requests_api.BulkJobRequestsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bulk_users_create(self):
        """Test case for bulk_users_create

        Bulk Users Create  # noqa: E501
        """
        pass

    def test_bulk_users_create_results(self):
        """Test case for bulk_users_create_results

        List Bulk Users Create Results  # noqa: E501
        """
        pass

    def test_jobs_get(self):
        """Test case for jobs_get

        Get Job (incomplete)  # noqa: E501
        """
        pass

    def test_jobs_results(self):
        """Test case for jobs_results

        List Job Results  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
