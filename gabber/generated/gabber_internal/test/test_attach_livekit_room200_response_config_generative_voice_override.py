# coding: utf-8

"""
    Session API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber_internal.models.attach_livekit_room200_response_config_generative_voice_override import AttachLivekitRoom200ResponseConfigGenerativeVoiceOverride

class TestAttachLivekitRoom200ResponseConfigGenerativeVoiceOverride(unittest.TestCase):
    """AttachLivekitRoom200ResponseConfigGenerativeVoiceOverride unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttachLivekitRoom200ResponseConfigGenerativeVoiceOverride:
        """Test AttachLivekitRoom200ResponseConfigGenerativeVoiceOverride
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttachLivekitRoom200ResponseConfigGenerativeVoiceOverride`
        """
        model = AttachLivekitRoom200ResponseConfigGenerativeVoiceOverride()
        if include_optional:
            return AttachLivekitRoom200ResponseConfigGenerativeVoiceOverride(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                name = '',
                language = '',
                service = '',
                model = '',
                voice = '',
                embeddings = [
                    1.337
                    ],
                cartesia_voice_id = '',
                elevenlabs_voice_id = '',
                project = '',
                human = '',
                preview_url = '',
                pricing = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_voice_override_pricing.attachLivekitRoom_200_response_config_generative_voice_override_pricing(
                    price_per_second = '', 
                    currency = '', 
                    product_name = '', ),
                tags = [
                    gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_voice_override_tags_inner.attachLivekitRoom_200_response_config_generative_voice_override_tags_inner(
                        name = '', 
                        human_name = '', )
                    ],
                extra = { }
            )
        else:
            return AttachLivekitRoom200ResponseConfigGenerativeVoiceOverride(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                name = '',
                language = '',
                pricing = gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_voice_override_pricing.attachLivekitRoom_200_response_config_generative_voice_override_pricing(
                    price_per_second = '', 
                    currency = '', 
                    product_name = '', ),
                tags = [
                    gabber.generated.gabber_internal.models.attach_livekit_room_200_response_config_generative_voice_override_tags_inner.attachLivekitRoom_200_response_config_generative_voice_override_tags_inner(
                        name = '', 
                        human_name = '', )
                    ],
        )
        """

    def testAttachLivekitRoom200ResponseConfigGenerativeVoiceOverride(self):
        """Test AttachLivekitRoom200ResponseConfigGenerativeVoiceOverride"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
