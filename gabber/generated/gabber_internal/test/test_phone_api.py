# coding: utf-8

"""
    Session API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber_internal.api.phone_api import PhoneApi


class TestPhoneApi(unittest.IsolatedAsyncioTestCase):
    """PhoneApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = PhoneApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_get_phone_attachment(self) -> None:
        """Test case for get_phone_attachment

        Get phone attachment
        """
        pass


if __name__ == '__main__':
    unittest.main()
