# coding: utf-8

"""
    Gabber API Reference

    The Gabber API is a set of APIs that allow you to interact with the Gabber platform.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber.models.webhook_message_tool_call_function import WebhookMessageToolCallFunction

class TestWebhookMessageToolCallFunction(unittest.TestCase):
    """WebhookMessageToolCallFunction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookMessageToolCallFunction:
        """Test WebhookMessageToolCallFunction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookMessageToolCallFunction`
        """
        model = WebhookMessageToolCallFunction()
        if include_optional:
            return WebhookMessageToolCallFunction(
                name = '',
                arguments = None
            )
        else:
            return WebhookMessageToolCallFunction(
                name = '',
                arguments = None,
        )
        """

    def testWebhookMessageToolCallFunction(self):
        """Test WebhookMessageToolCallFunction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
