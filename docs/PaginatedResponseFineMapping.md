# PaginatedResponseFineMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FineMapping]**](FineMapping.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_fine_mapping import PaginatedResponseFineMapping

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseFineMapping from a JSON string
paginated_response_fine_mapping_instance = PaginatedResponseFineMapping.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseFineMapping.to_json())

# convert the object into a dict
paginated_response_fine_mapping_dict = paginated_response_fine_mapping_instance.to_dict()
# create an instance of PaginatedResponseFineMapping from a dict
paginated_response_fine_mapping_from_dict = PaginatedResponseFineMapping.from_dict(paginated_response_fine_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


