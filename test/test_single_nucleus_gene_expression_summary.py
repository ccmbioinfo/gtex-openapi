# coding: utf-8

"""
    GTEx Portal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gtex_openapi.models.single_nucleus_gene_expression_summary import SingleNucleusGeneExpressionSummary

class TestSingleNucleusGeneExpressionSummary(unittest.TestCase):
    """SingleNucleusGeneExpressionSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SingleNucleusGeneExpressionSummary:
        """Test SingleNucleusGeneExpressionSummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SingleNucleusGeneExpressionSummary`
        """
        model = SingleNucleusGeneExpressionSummary()
        if include_optional:
            return SingleNucleusGeneExpressionSummary(
                tissue_site_detail_id = 'Adipose_Subcutaneous',
                ontology_id = 'UBERON:EFO_0000572',
                dataset_id = 'gtex_v8',
                cell_type = '',
                num_cells = 56
            )
        else:
            return SingleNucleusGeneExpressionSummary(
                tissue_site_detail_id = 'Adipose_Subcutaneous',
                ontology_id = 'UBERON:EFO_0000572',
                dataset_id = 'gtex_v8',
                cell_type = '',
                num_cells = 56,
        )
        """

    def testSingleNucleusGeneExpressionSummary(self):
        """Test SingleNucleusGeneExpressionSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
