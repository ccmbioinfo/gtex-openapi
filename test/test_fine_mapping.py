# coding: utf-8

"""
    GTEx Portal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gtex_openapi.models.fine_mapping import FineMapping

class TestFineMapping(unittest.TestCase):
    """FineMapping unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FineMapping:
        """Test FineMapping
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FineMapping`
        """
        model = FineMapping()
        if include_optional:
            return FineMapping(
                dataset_id = 'gtex_v8',
                gencode_id = '',
                method = '',
                pip = 1.337,
                set_id = 56,
                set_size = 56,
                tissue_site_detail_id = 'Adipose_Subcutaneous',
                ontology_id = 'UBERON:EFO_0000572',
                variant_id = ''
            )
        else:
            return FineMapping(
                dataset_id = 'gtex_v8',
                gencode_id = '',
                method = '',
                pip = 1.337,
                set_id = 56,
                set_size = 56,
                tissue_site_detail_id = 'Adipose_Subcutaneous',
                ontology_id = 'UBERON:EFO_0000572',
                variant_id = '',
        )
        """

    def testFineMapping(self):
        """Test FineMapping"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
