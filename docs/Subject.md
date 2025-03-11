# Subject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardy_scale** | [**AppModelsResponsesHardyScale**](AppModelsResponsesHardyScale.md) |  | [optional] 
**age_bracket** | [**DonorAgeBracket**](DonorAgeBracket.md) |  | 
**subject_id** | **str** |  | 
**sex** | [**Sex**](Sex.md) |  | 
**dataset_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.subject import Subject

# TODO update the JSON string below
json = "{}"
# create an instance of Subject from a JSON string
subject_instance = Subject.from_json(json)
# print the JSON string representation of the object
print(Subject.to_json())

# convert the object into a dict
subject_dict = subject_instance.to_dict()
# create an instance of Subject from a dict
subject_from_dict = Subject.from_dict(subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


