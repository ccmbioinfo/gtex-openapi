# coding: utf-8

"""
    GTEx Portal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gtex_openapi.models.i_eqtl import IEqtl

class TestIEqtl(unittest.TestCase):
    """IEqtl unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IEqtl:
        """Test IEqtl
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IEqtl`
        """
        model = IEqtl()
        if include_optional:
            return IEqtl(
                cell_type = 'Adipocytes',
                data = [
                    1.337
                    ],
                dataset_id = 'gtex_v8',
                enrichment_scores = [
                    1.337
                    ],
                gencode_id = '',
                genotypes = [
                    56
                    ],
                regression_coord = gtex_openapi.models.regressioncoord.Regressioncoord(),
                tissue_site_detail_id = 'Adipose_Subcutaneous',
                variant_id = ''
            )
        else:
            return IEqtl(
                cell_type = 'Adipocytes',
                data = [
                    1.337
                    ],
                dataset_id = 'gtex_v8',
                enrichment_scores = [
                    1.337
                    ],
                gencode_id = '',
                genotypes = [
                    56
                    ],
                regression_coord = gtex_openapi.models.regressioncoord.Regressioncoord(),
                tissue_site_detail_id = 'Adipose_Subcutaneous',
                variant_id = '',
        )
        """

    def testIEqtl(self):
        """Test IEqtl"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
