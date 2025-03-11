# PaginatedResponseExpressionPCA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ExpressionPCA]**](ExpressionPCA.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_expression_pca import PaginatedResponseExpressionPCA

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseExpressionPCA from a JSON string
paginated_response_expression_pca_instance = PaginatedResponseExpressionPCA.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseExpressionPCA.to_json())

# convert the object into a dict
paginated_response_expression_pca_dict = paginated_response_expression_pca_instance.to_dict()
# create an instance of PaginatedResponseExpressionPCA from a dict
paginated_response_expression_pca_from_dict = PaginatedResponseExpressionPCA.from_dict(paginated_response_expression_pca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


