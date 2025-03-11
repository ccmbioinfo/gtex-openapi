# PaginatedResponseHistologySample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HistologySample]**](HistologySample.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_histology_sample import PaginatedResponseHistologySample

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseHistologySample from a JSON string
paginated_response_histology_sample_instance = PaginatedResponseHistologySample.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseHistologySample.to_json())

# convert the object into a dict
paginated_response_histology_sample_dict = paginated_response_histology_sample_instance.to_dict()
# create an instance of PaginatedResponseHistologySample from a dict
paginated_response_histology_sample_from_dict = PaginatedResponseHistologySample.from_dict(paginated_response_histology_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


