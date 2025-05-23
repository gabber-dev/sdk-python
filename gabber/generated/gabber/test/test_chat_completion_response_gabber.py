# coding: utf-8

"""
    Gabber API Reference

    The Gabber API is a set of APIs that allow you to interact with the Gabber platform.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber.models.chat_completion_response_gabber import ChatCompletionResponseGabber

class TestChatCompletionResponseGabber(unittest.TestCase):
    """ChatCompletionResponseGabber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatCompletionResponseGabber:
        """Test ChatCompletionResponseGabber
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChatCompletionResponseGabber`
        """
        model = ChatCompletionResponseGabber()
        if include_optional:
            return ChatCompletionResponseGabber(
                usage = [
                    gabber.generated.gabber.models.usage.Usage(
                        id = '', 
                        type = 'conversational_seconds', 
                        value = 1.337, 
                        human = '', 
                        project = '', 
                        metadata = gabber.generated.gabber.models.metadata.metadata(), )
                    ],
                message_data = [
                    gabber.generated.gabber.models.chat_completion_response_gabber_message_data.ChatCompletionResponseGabberMessageData(
                        message_index = 56, 
                        content_index = 56, 
                        type = 'audio_transcript', 
                        data = gabber.generated.gabber.models.chat_completion_response_gabber_message_data_data.ChatCompletionResponseGabberMessageData_data(
                            transcript = '', ), )
                    ],
                advanced_memory = gabber.generated.gabber.models.context_advanced_memory_query_result.ContextAdvancedMemoryQueryResult(
                    nodes = [
                        gabber.generated.gabber.models.context_advanced_memory_node.ContextAdvancedMemoryNode(
                            id = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '', 
                            summary = '', )
                        ], 
                    edges = [
                        gabber.generated.gabber.models.context_advanced_memory_edge.ContextAdvancedMemoryEdge(
                            id = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            invalidated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            source_node = '', 
                            target_node = '', 
                            fact = '', 
                            relation = '', )
                        ], )
            )
        else:
            return ChatCompletionResponseGabber(
                usage = [
                    gabber.generated.gabber.models.usage.Usage(
                        id = '', 
                        type = 'conversational_seconds', 
                        value = 1.337, 
                        human = '', 
                        project = '', 
                        metadata = gabber.generated.gabber.models.metadata.metadata(), )
                    ],
                message_data = [
                    gabber.generated.gabber.models.chat_completion_response_gabber_message_data.ChatCompletionResponseGabberMessageData(
                        message_index = 56, 
                        content_index = 56, 
                        type = 'audio_transcript', 
                        data = gabber.generated.gabber.models.chat_completion_response_gabber_message_data_data.ChatCompletionResponseGabberMessageData_data(
                            transcript = '', ), )
                    ],
        )
        """

    def testChatCompletionResponseGabber(self):
        """Test ChatCompletionResponseGabber"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
