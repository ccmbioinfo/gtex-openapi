# coding: utf-8

"""
    GTEx Portal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gtex_openapi.models.eqtl_gene import EqtlGene

class TestEqtlGene(unittest.TestCase):
    """EqtlGene unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EqtlGene:
        """Test EqtlGene
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EqtlGene`
        """
        model = EqtlGene()
        if include_optional:
            return EqtlGene(
                tissue_site_detail_id = 'Adipose_Subcutaneous',
                ontology_id = 'UBERON:EFO_0000572',
                dataset_id = 'gtex_v8',
                empirical_p_value = 1.337,
                gencode_id = '',
                gene_symbol = '',
                log2_allelic_fold_change = 1.337,
                p_value = 1.337,
                p_value_threshold = 1.337,
                q_value = 1.337
            )
        else:
            return EqtlGene(
                tissue_site_detail_id = 'Adipose_Subcutaneous',
                ontology_id = 'UBERON:EFO_0000572',
                dataset_id = 'gtex_v8',
                empirical_p_value = 1.337,
                gencode_id = '',
                gene_symbol = '',
                p_value = 1.337,
                p_value_threshold = 1.337,
                q_value = 1.337,
        )
        """

    def testEqtlGene(self):
        """Test EqtlGene"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
