# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.scan_api import ScanApi  # noqa: E501
from swagger_client.rest import ApiException


class TestScanApi(unittest.TestCase):
    """ScanApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.scan_api.ScanApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_scan(self):
        """Test case for get_scan

        Scan  # noqa: E501
        """
        pass

    def test_get_scans(self):
        """Test case for get_scans

        Scans  # noqa: E501
        """
        pass

    def test_get_site_scans(self):
        """Test case for get_site_scans

        Site Scans  # noqa: E501
        """
        pass

    def test_set_scan_status(self):
        """Test case for set_scan_status

        Scan Status  # noqa: E501
        """
        pass

    def test_start_scan(self):
        """Test case for start_scan

        Site Scans  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
