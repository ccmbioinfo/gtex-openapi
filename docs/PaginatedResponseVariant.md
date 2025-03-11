# PaginatedResponseVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Variant]**](Variant.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_variant import PaginatedResponseVariant

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseVariant from a JSON string
paginated_response_variant_instance = PaginatedResponseVariant.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseVariant.to_json())

# convert the object into a dict
paginated_response_variant_dict = paginated_response_variant_instance.to_dict()
# create an instance of PaginatedResponseVariant from a dict
paginated_response_variant_from_dict = PaginatedResponseVariant.from_dict(paginated_response_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


