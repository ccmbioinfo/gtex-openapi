# PaginatedResponseMetaSoft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MetaSoft]**](MetaSoft.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_meta_soft import PaginatedResponseMetaSoft

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseMetaSoft from a JSON string
paginated_response_meta_soft_instance = PaginatedResponseMetaSoft.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseMetaSoft.to_json())

# convert the object into a dict
paginated_response_meta_soft_dict = paginated_response_meta_soft_instance.to_dict()
# create an instance of PaginatedResponseMetaSoft from a dict
paginated_response_meta_soft_from_dict = PaginatedResponseMetaSoft.from_dict(paginated_response_meta_soft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


