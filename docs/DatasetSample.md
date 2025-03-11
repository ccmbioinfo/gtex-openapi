# DatasetSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ischemic_time** | **int** |  | [optional] 
**aliquot_id** | **str** |  | 
**tissue_sample_id** | **str** |  | 
**tissue_site_detail** | **str** |  | 
**data_type** | **str** |  | [optional] 
**ischemic_time_group** | **str** |  | [optional] 
**pathology_notes_categories** | **Dict[str, bool]** |  | 
**freeze_type** | **str** |  | 
**pathology_notes** | **str** |  | [optional] 
**sample_id** | **str** |  | 
**sample_id_upper** | **str** |  | 
**age_bracket** | [**DonorAgeBracket**](DonorAgeBracket.md) |  | 
**rin** | **str** |  | [optional] 
**hardy_scale** | [**AppModelsResponsesHardyScale**](AppModelsResponsesHardyScale.md) |  | [optional] 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**subject_id** | **str** |  | 
**uberon_id** | **str** |  | 
**sex** | [**Sex**](Sex.md) |  | 
**autolysis_score** | **str** |  | [optional] 
**dataset_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.dataset_sample import DatasetSample

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetSample from a JSON string
dataset_sample_instance = DatasetSample.from_json(json)
# print the JSON string representation of the object
print(DatasetSample.to_json())

# convert the object into a dict
dataset_sample_dict = dataset_sample_instance.to_dict()
# create an instance of DatasetSample from a dict
dataset_sample_from_dict = DatasetSample.from_dict(dataset_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


