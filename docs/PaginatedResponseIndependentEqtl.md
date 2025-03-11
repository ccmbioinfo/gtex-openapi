# PaginatedResponseIndependentEqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IndependentEqtl]**](IndependentEqtl.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_independent_eqtl import PaginatedResponseIndependentEqtl

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseIndependentEqtl from a JSON string
paginated_response_independent_eqtl_instance = PaginatedResponseIndependentEqtl.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseIndependentEqtl.to_json())

# convert the object into a dict
paginated_response_independent_eqtl_dict = paginated_response_independent_eqtl_instance.to_dict()
# create an instance of PaginatedResponseIndependentEqtl from a dict
paginated_response_independent_eqtl_from_dict = PaginatedResponseIndependentEqtl.from_dict(paginated_response_independent_eqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


