# Sqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[float]** |  | 
**error** | **float** |  | 
**genotypes** | **List[int]** |  | 
**het_count** | **int** |  | 
**homo_alt_count** | **int** |  | 
**homo_ref_count** | **int** |  | 
**maf** | **float** |  | 
**nes** | **float** |  | 
**p_value** | **float** |  | 
**p_value_threshold** | **float** |  | 
**phenotype_id** | **str** |  | 
**t_statistic** | **float** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**variant_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.sqtl import Sqtl

# TODO update the JSON string below
json = "{}"
# create an instance of Sqtl from a JSON string
sqtl_instance = Sqtl.from_json(json)
# print the JSON string representation of the object
print(Sqtl.to_json())

# convert the object into a dict
sqtl_dict = sqtl_instance.to_dict()
# create an instance of Sqtl from a dict
sqtl_from_dict = Sqtl.from_dict(sqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


