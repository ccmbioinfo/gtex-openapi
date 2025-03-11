# PaginatedResponseListUnionStrFloat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[List[DataInnerInner]]** |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_list_union_str_float import PaginatedResponseListUnionStrFloat

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseListUnionStrFloat from a JSON string
paginated_response_list_union_str_float_instance = PaginatedResponseListUnionStrFloat.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseListUnionStrFloat.to_json())

# convert the object into a dict
paginated_response_list_union_str_float_dict = paginated_response_list_union_str_float_instance.to_dict()
# create an instance of PaginatedResponseListUnionStrFloat from a dict
paginated_response_list_union_str_float_from_dict = PaginatedResponseListUnionStrFloat.from_dict(paginated_response_list_union_str_float_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


