# coding: utf-8

"""
    Gabber API Reference

    The Gabber API is a set of APIs that allow you to interact with the Gabber platform.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber.models.session_start_request import SessionStartRequest

class TestSessionStartRequest(unittest.TestCase):
    """SessionStartRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SessionStartRequest:
        """Test SessionStartRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SessionStartRequest`
        """
        model = SessionStartRequest()
        if include_optional:
            return SessionStartRequest(
                history = [
                    gabber.generated.gabber.models.history_message.HistoryMessage(
                        content = '', 
                        import_id = '', 
                        role = 'assistant', )
                    ],
                time_limit_s = 56,
                voice_override = '',
                llm = '',
                persona = '',
                save_messages = True,
                extra = gabber.generated.gabber.models._extra._extra(),
                scenario = ''
            )
        else:
            return SessionStartRequest(
        )
        """

    def testSessionStartRequest(self):
        """Test SessionStartRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
