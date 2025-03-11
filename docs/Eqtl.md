# Eqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[float]** |  | 
**error** | **float** |  | 
**gencode_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**genotypes** | **List[int]** |  | 
**het_count** | **int** |  | 
**homo_alt_count** | **int** |  | 
**homo_ref_count** | **int** |  | 
**maf** | **float** |  | 
**nes** | **float** |  | 
**p_value** | **float** |  | 
**p_value_threshold** | **float** |  | [optional] 
**t_statistic** | **float** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**variant_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.eqtl import Eqtl

# TODO update the JSON string below
json = "{}"
# create an instance of Eqtl from a JSON string
eqtl_instance = Eqtl.from_json(json)
# print the JSON string representation of the object
print(Eqtl.to_json())

# convert the object into a dict
eqtl_dict = eqtl_instance.to_dict()
# create an instance of Eqtl from a dict
eqtl_from_dict = Eqtl.from_dict(eqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


