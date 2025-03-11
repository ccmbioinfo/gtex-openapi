# HistologySample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_bracket** | [**DonorAgeBracket**](DonorAgeBracket.md) |  | 
**hardy_scale** | [**AppModelsResponsesHardyScale**](AppModelsResponsesHardyScale.md) |  | 
**hide** | **bool** |  | 
**histology_image_id** | **str** |  | 
**pathology_notes** | **str** |  | [optional] 
**pathology_notes_categories** | **Dict[str, bool]** |  | 
**sample_id** | **str** |  | [optional] 
**sex** | [**Sex**](Sex.md) |  | 
**subject_id** | **str** |  | 
**tissue_sample_id** | **str** |  | [optional] 
**tissue_site_detail** | **str** |  | 

## Example

```python
from gtex_openapi.models.histology_sample import HistologySample

# TODO update the JSON string below
json = "{}"
# create an instance of HistologySample from a JSON string
histology_sample_instance = HistologySample.from_json(json)
# print the JSON string representation of the object
print(HistologySample.to_json())

# convert the object into a dict
histology_sample_dict = histology_sample_instance.to_dict()
# create an instance of HistologySample from a dict
histology_sample_from_dict = HistologySample.from_dict(histology_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


