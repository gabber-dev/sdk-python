# coding: utf-8

"""
    Gabber API Reference

    The Gabber API is a set of APIs that allow you to interact with the Gabber platform.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gabber.generated.gabber.models.context_advanced_memory_query_result import ContextAdvancedMemoryQueryResult

class TestContextAdvancedMemoryQueryResult(unittest.TestCase):
    """ContextAdvancedMemoryQueryResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContextAdvancedMemoryQueryResult:
        """Test ContextAdvancedMemoryQueryResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContextAdvancedMemoryQueryResult`
        """
        model = ContextAdvancedMemoryQueryResult()
        if include_optional:
            return ContextAdvancedMemoryQueryResult(
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
                    ]
            )
        else:
            return ContextAdvancedMemoryQueryResult(
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
                    ],
        )
        """

    def testContextAdvancedMemoryQueryResult(self):
        """Test ContextAdvancedMemoryQueryResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
