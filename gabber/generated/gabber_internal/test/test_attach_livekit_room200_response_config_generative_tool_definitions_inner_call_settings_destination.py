# coding: utf-8

"""
    Session API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber_internal.models.attach_livekit_room200_response_config_generative_tool_definitions_inner_call_settings_destination import AttachLivekitRoom200ResponseConfigGenerativeToolDefinitionsInnerCallSettingsDestination

class TestAttachLivekitRoom200ResponseConfigGenerativeToolDefinitionsInnerCallSettingsDestination(unittest.TestCase):
    """AttachLivekitRoom200ResponseConfigGenerativeToolDefinitionsInnerCallSettingsDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttachLivekitRoom200ResponseConfigGenerativeToolDefinitionsInnerCallSettingsDestination:
        """Test AttachLivekitRoom200ResponseConfigGenerativeToolDefinitionsInnerCallSettingsDestination
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttachLivekitRoom200ResponseConfigGenerativeToolDefinitionsInnerCallSettingsDestination`
        """
        model = AttachLivekitRoom200ResponseConfigGenerativeToolDefinitionsInnerCallSettingsDestination()
        if include_optional:
            return AttachLivekitRoom200ResponseConfigGenerativeToolDefinitionsInnerCallSettingsDestination(
                type = 'web_request',
                url = ''
            )
        else:
            return AttachLivekitRoom200ResponseConfigGenerativeToolDefinitionsInnerCallSettingsDestination(
                type = 'web_request',
                url = '',
        )
        """

    def testAttachLivekitRoom200ResponseConfigGenerativeToolDefinitionsInnerCallSettingsDestination(self):
        """Test AttachLivekitRoom200ResponseConfigGenerativeToolDefinitionsInnerCallSettingsDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
