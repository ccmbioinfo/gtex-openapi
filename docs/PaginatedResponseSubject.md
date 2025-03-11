# PaginatedResponseSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Subject]**](Subject.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_subject import PaginatedResponseSubject

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseSubject from a JSON string
paginated_response_subject_instance = PaginatedResponseSubject.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseSubject.to_json())

# convert the object into a dict
paginated_response_subject_dict = paginated_response_subject_instance.to_dict()
# create an instance of PaginatedResponseSubject from a dict
paginated_response_subject_from_dict = PaginatedResponseSubject.from_dict(paginated_response_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


