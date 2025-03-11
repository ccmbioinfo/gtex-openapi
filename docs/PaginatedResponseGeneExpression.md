# PaginatedResponseGeneExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GeneExpression]**](GeneExpression.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_gene_expression import PaginatedResponseGeneExpression

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseGeneExpression from a JSON string
paginated_response_gene_expression_instance = PaginatedResponseGeneExpression.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseGeneExpression.to_json())

# convert the object into a dict
paginated_response_gene_expression_dict = paginated_response_gene_expression_instance.to_dict()
# create an instance of PaginatedResponseGeneExpression from a dict
paginated_response_gene_expression_from_dict = PaginatedResponseGeneExpression.from_dict(paginated_response_gene_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


