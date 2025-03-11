# PaginatedResponseMedianJunctionExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MedianJunctionExpression]**](MedianJunctionExpression.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_median_junction_expression import PaginatedResponseMedianJunctionExpression

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseMedianJunctionExpression from a JSON string
paginated_response_median_junction_expression_instance = PaginatedResponseMedianJunctionExpression.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseMedianJunctionExpression.to_json())

# convert the object into a dict
paginated_response_median_junction_expression_dict = paginated_response_median_junction_expression_instance.to_dict()
# create an instance of PaginatedResponseMedianJunctionExpression from a dict
paginated_response_median_junction_expression_from_dict = PaginatedResponseMedianJunctionExpression.from_dict(paginated_response_median_junction_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


