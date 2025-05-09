# coding: utf-8

"""
    Gabber API Reference

    The Gabber API is a set of APIs that allow you to interact with the Gabber platform.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber.models.check_usage_token200_response import CheckUsageToken200Response

class TestCheckUsageToken200Response(unittest.TestCase):
    """CheckUsageToken200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckUsageToken200Response:
        """Test CheckUsageToken200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckUsageToken200Response`
        """
        model = CheckUsageToken200Response()
        if include_optional:
            return CheckUsageToken200Response(
                ttl_seconds = 56
            )
        else:
            return CheckUsageToken200Response(
                ttl_seconds = 56,
        )
        """

    def testCheckUsageToken200Response(self):
        """Test CheckUsageToken200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
