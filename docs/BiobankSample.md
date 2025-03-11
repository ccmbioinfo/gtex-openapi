# BiobankSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**material_type** | [**AppModelsResponsesMaterialType**](AppModelsResponsesMaterialType.md) |  | 
**sample_id** | **str** |  | 
**sample_id_upper** | **str** |  | 
**sex** | [**Sex**](Sex.md) |  | 
**rin** | **float** |  | [optional] 
**has_gtex_image** | **bool** |  | 
**concentration** | **float** |  | [optional] 
**autolysis_score** | **str** |  | [optional] 
**analysis_release** | **str** |  | [optional] 
**genotype** | **str** |  | [optional] 
**hardy_scale** | [**AppModelsResponsesHardyScale**](AppModelsResponsesHardyScale.md) |  | [optional] 
**pathology_notes** | **str** |  | 
**subject_id** | **str** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**has_genotype** | **bool** |  | 
**original_material_type** | [**OriginalMaterialType**](OriginalMaterialType.md) |  | 
**aliquot_id** | **str** |  | 
**tissue_sample_id** | **str** |  | 
**age_bracket** | [**DonorAgeBracket**](DonorAgeBracket.md) |  | 
**brain_tissue_donor** | **bool** |  | 
**volume** | **float** |  | [optional] 
**has_expression_data** | **bool** |  | 
**has_brd_image** | **bool** |  | 
**tissue_site_detail** | **str** |  | 
**pathology_notes_categories** | **Dict[str, bool]** |  | 
**amount** | **float** |  | [optional] 
**mass** | **float** |  | [optional] 
**tissue_site** | **str** |  | 
**expression** | **str** |  | [optional] 

## Example

```python
from gtex_openapi.models.biobank_sample import BiobankSample

# TODO update the JSON string below
json = "{}"
# create an instance of BiobankSample from a JSON string
biobank_sample_instance = BiobankSample.from_json(json)
# print the JSON string representation of the object
print(BiobankSample.to_json())

# convert the object into a dict
biobank_sample_dict = biobank_sample_instance.to_dict()
# create an instance of BiobankSample from a dict
biobank_sample_from_dict = BiobankSample.from_dict(biobank_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


