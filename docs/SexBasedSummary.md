# SexBasedSummary

Contains a summary of statistics for a collection of samples, broken down by sex.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**female** | [**AgeAndCountSummary**](AgeAndCountSummary.md) |  | 
**male** | [**AgeAndCountSummary**](AgeAndCountSummary.md) |  | 

## Example

```python
from gtex_openapi.models.sex_based_summary import SexBasedSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SexBasedSummary from a JSON string
sex_based_summary_instance = SexBasedSummary.from_json(json)
# print the JSON string representation of the object
print(SexBasedSummary.to_json())

# convert the object into a dict
sex_based_summary_dict = sex_based_summary_instance.to_dict()
# create an instance of SexBasedSummary from a dict
sex_based_summary_from_dict = SexBasedSummary.from_dict(sex_based_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


