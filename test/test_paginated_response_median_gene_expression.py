# coding: utf-8

"""
    GTEx Portal API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gtex_openapi.models.paginated_response_median_gene_expression import PaginatedResponseMedianGeneExpression

class TestPaginatedResponseMedianGeneExpression(unittest.TestCase):
    """PaginatedResponseMedianGeneExpression unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedResponseMedianGeneExpression:
        """Test PaginatedResponseMedianGeneExpression
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedResponseMedianGeneExpression`
        """
        model = PaginatedResponseMedianGeneExpression()
        if include_optional:
            return PaginatedResponseMedianGeneExpression(
                data = [
                    gtex_openapi.models.median_gene_expression.MedianGeneExpression(
                        median = 1.337, 
                        tissue_site_detail_id = 'Adipose_Subcutaneous', 
                        ontology_id = 'UBERON:EFO_0000572', 
                        dataset_id = 'gtex_v8', 
                        gencode_id = '', 
                        gene_symbol = '', 
                        unit = 'TPM', )
                    ],
                paging_info = gtex_openapi.models.pagination_info.PaginationInfo(
                    number_of_pages = 56, 
                    page = 56, 
                    max_items_per_page = 56, 
                    total_number_of_items = 56, )
            )
        else:
            return PaginatedResponseMedianGeneExpression(
                data = [
                    gtex_openapi.models.median_gene_expression.MedianGeneExpression(
                        median = 1.337, 
                        tissue_site_detail_id = 'Adipose_Subcutaneous', 
                        ontology_id = 'UBERON:EFO_0000572', 
                        dataset_id = 'gtex_v8', 
                        gencode_id = '', 
                        gene_symbol = '', 
                        unit = 'TPM', )
                    ],
                paging_info = gtex_openapi.models.pagination_info.PaginationInfo(
                    number_of_pages = 56, 
                    page = 56, 
                    max_items_per_page = 56, 
                    total_number_of_items = 56, ),
        )
        """

    def testPaginatedResponseMedianGeneExpression(self):
        """Test PaginatedResponseMedianGeneExpression"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
