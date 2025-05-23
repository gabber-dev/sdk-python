# coding: utf-8

"""
    Gabber API Reference

    The Gabber API is a set of APIs that allow you to interact with the Gabber platform.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber.models.chat_completion_request_message_content_part_text import ChatCompletionRequestMessageContentPartText

class TestChatCompletionRequestMessageContentPartText(unittest.TestCase):
    """ChatCompletionRequestMessageContentPartText unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatCompletionRequestMessageContentPartText:
        """Test ChatCompletionRequestMessageContentPartText
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChatCompletionRequestMessageContentPartText`
        """
        model = ChatCompletionRequestMessageContentPartText()
        if include_optional:
            return ChatCompletionRequestMessageContentPartText(
                type = 'text',
                text = ''
            )
        else:
            return ChatCompletionRequestMessageContentPartText(
                type = 'text',
                text = '',
        )
        """

    def testChatCompletionRequestMessageContentPartText(self):
        """Test ChatCompletionRequestMessageContentPartText"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
