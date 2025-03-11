# PaginatedResponseFunctionalAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FunctionalAnnotation]**](FunctionalAnnotation.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_functional_annotation import PaginatedResponseFunctionalAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseFunctionalAnnotation from a JSON string
paginated_response_functional_annotation_instance = PaginatedResponseFunctionalAnnotation.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseFunctionalAnnotation.to_json())

# convert the object into a dict
paginated_response_functional_annotation_dict = paginated_response_functional_annotation_instance.to_dict()
# create an instance of PaginatedResponseFunctionalAnnotation from a dict
paginated_response_functional_annotation_from_dict = PaginatedResponseFunctionalAnnotation.from_dict(paginated_response_functional_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


