# coding: utf-8

"""
    Gabber API Reference

    The Gabber API is a set of APIs that allow you to interact with the Gabber platform.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber.models.chat_completion_response_message_gabber_voice import ChatCompletionResponseMessageGabberVoice

class TestChatCompletionResponseMessageGabberVoice(unittest.TestCase):
    """ChatCompletionResponseMessageGabberVoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatCompletionResponseMessageGabberVoice:
        """Test ChatCompletionResponseMessageGabberVoice
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChatCompletionResponseMessageGabberVoice`
        """
        model = ChatCompletionResponseMessageGabberVoice()
        if include_optional:
            return ChatCompletionResponseMessageGabberVoice(
                audio_url = '',
                expires_at = 56
            )
        else:
            return ChatCompletionResponseMessageGabberVoice(
                audio_url = '',
                expires_at = 56,
        )
        """

    def testChatCompletionResponseMessageGabberVoice(self):
        """Test ChatCompletionResponseMessageGabberVoice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
