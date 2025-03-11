# PaginatedResponseMedianGeneExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MedianGeneExpression]**](MedianGeneExpression.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_median_gene_expression import PaginatedResponseMedianGeneExpression

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseMedianGeneExpression from a JSON string
paginated_response_median_gene_expression_instance = PaginatedResponseMedianGeneExpression.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseMedianGeneExpression.to_json())

# convert the object into a dict
paginated_response_median_gene_expression_dict = paginated_response_median_gene_expression_instance.to_dict()
# create an instance of PaginatedResponseMedianGeneExpression from a dict
paginated_response_median_gene_expression_from_dict = PaginatedResponseMedianGeneExpression.from_dict(paginated_response_median_gene_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


