# PaginatedResponseSingleNucleusGeneExpressionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SingleNucleusGeneExpressionResult]**](SingleNucleusGeneExpressionResult.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_single_nucleus_gene_expression_result import PaginatedResponseSingleNucleusGeneExpressionResult

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseSingleNucleusGeneExpressionResult from a JSON string
paginated_response_single_nucleus_gene_expression_result_instance = PaginatedResponseSingleNucleusGeneExpressionResult.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseSingleNucleusGeneExpressionResult.to_json())

# convert the object into a dict
paginated_response_single_nucleus_gene_expression_result_dict = paginated_response_single_nucleus_gene_expression_result_instance.to_dict()
# create an instance of PaginatedResponseSingleNucleusGeneExpressionResult from a dict
paginated_response_single_nucleus_gene_expression_result_from_dict = PaginatedResponseSingleNucleusGeneExpressionResult.from_dict(paginated_response_single_nucleus_gene_expression_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


