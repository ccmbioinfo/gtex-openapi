# PaginatedResponseAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Annotation]**](Annotation.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_annotation import PaginatedResponseAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseAnnotation from a JSON string
paginated_response_annotation_instance = PaginatedResponseAnnotation.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseAnnotation.to_json())

# convert the object into a dict
paginated_response_annotation_dict = paginated_response_annotation_instance.to_dict()
# create an instance of PaginatedResponseAnnotation from a dict
paginated_response_annotation_from_dict = PaginatedResponseAnnotation.from_dict(paginated_response_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


