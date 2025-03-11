# PaginatedResponseDatasetSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DatasetSample]**](DatasetSample.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_dataset_sample import PaginatedResponseDatasetSample

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseDatasetSample from a JSON string
paginated_response_dataset_sample_instance = PaginatedResponseDatasetSample.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseDatasetSample.to_json())

# convert the object into a dict
paginated_response_dataset_sample_dict = paginated_response_dataset_sample_instance.to_dict()
# create an instance of PaginatedResponseDatasetSample from a dict
paginated_response_dataset_sample_from_dict = PaginatedResponseDatasetSample.from_dict(paginated_response_dataset_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


