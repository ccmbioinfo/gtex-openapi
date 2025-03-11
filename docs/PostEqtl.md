# PostEqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**error** | [**Error**](Error.md) |  | 
**gencode_id** | **str** |  | 
**gene_symbol** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**nes** | [**Nes**](Nes.md) |  | 
**p_value** | [**Pvalue**](Pvalue.md) |  | 
**p_value_threshold** | [**Pvaluethreshold**](Pvaluethreshold.md) |  | 
**snp_id** | **str** |  | [optional] 
**t_statistic** | [**Tstatistic**](Tstatistic.md) |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**variant_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.post_eqtl import PostEqtl

# TODO update the JSON string below
json = "{}"
# create an instance of PostEqtl from a JSON string
post_eqtl_instance = PostEqtl.from_json(json)
# print the JSON string representation of the object
print(PostEqtl.to_json())

# convert the object into a dict
post_eqtl_dict = post_eqtl_instance.to_dict()
# create an instance of PostEqtl from a dict
post_eqtl_from_dict = PostEqtl.from_dict(post_eqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


