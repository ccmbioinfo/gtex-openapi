# PaginatedResponseMedianExonExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MedianExonExpression]**](MedianExonExpression.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_median_exon_expression import PaginatedResponseMedianExonExpression

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseMedianExonExpression from a JSON string
paginated_response_median_exon_expression_instance = PaginatedResponseMedianExonExpression.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseMedianExonExpression.to_json())

# convert the object into a dict
paginated_response_median_exon_expression_dict = paginated_response_median_exon_expression_instance.to_dict()
# create an instance of PaginatedResponseMedianExonExpression from a dict
paginated_response_median_exon_expression_from_dict = PaginatedResponseMedianExonExpression.from_dict(paginated_response_median_exon_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


