# coding: utf-8

"""
    Gabber API Reference

    The Gabber API is a set of APIs that allow you to interact with the Gabber platform.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber.models.chat_completion_stream_response_delta import ChatCompletionStreamResponseDelta

class TestChatCompletionStreamResponseDelta(unittest.TestCase):
    """ChatCompletionStreamResponseDelta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatCompletionStreamResponseDelta:
        """Test ChatCompletionStreamResponseDelta
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChatCompletionStreamResponseDelta`
        """
        model = ChatCompletionStreamResponseDelta()
        if include_optional:
            return ChatCompletionStreamResponseDelta(
                content = '',
                role = 'system',
                tool_calls = [
                    gabber.generated.gabber.models.chat_completion_message_tool_call_chunk.ChatCompletionMessageToolCallChunk(
                        index = 56, 
                        id = '', 
                        type = 'function', 
                        function = gabber.generated.gabber.models.chat_completion_message_tool_call_function.ChatCompletionMessageToolCallFunction(
                            name = '', 
                            arguments = '', ), )
                    ],
                refusal = '',
                gabber = gabber.generated.gabber.models.chat_completion_stream_response_delta_gabber.ChatCompletionStreamResponseDeltaGabber(
                    voice = gabber.generated.gabber.models.chat_completion_stream_response_delta_gabber_voice.ChatCompletionStreamResponseDeltaGabberVoice(
                        audio_url = '', 
                        expires_at = 56, ), )
            )
        else:
            return ChatCompletionStreamResponseDelta(
                content = '',
                role = 'system',
        )
        """

    def testChatCompletionStreamResponseDelta(self):
        """Test ChatCompletionStreamResponseDelta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
