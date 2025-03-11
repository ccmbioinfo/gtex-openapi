# AgeAndCountSummary

Holds summary statistics for a collection of samples.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_max** | **int** |  | [optional] 
**age_min** | **int** |  | [optional] 
**age_mean** | **float** |  | [optional] 
**count** | **int** |  | 

## Example

```python
from gtex_openapi.models.age_and_count_summary import AgeAndCountSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AgeAndCountSummary from a JSON string
age_and_count_summary_instance = AgeAndCountSummary.from_json(json)
# print the JSON string representation of the object
print(AgeAndCountSummary.to_json())

# convert the object into a dict
age_and_count_summary_dict = age_and_count_summary_instance.to_dict()
# create an instance of AgeAndCountSummary from a dict
age_and_count_summary_from_dict = AgeAndCountSummary.from_dict(age_and_count_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


