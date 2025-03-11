# SingleTissueEqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chromosome** | [**Chromosome**](Chromosome.md) |  | 
**dataset_id** | **str** |  | 
**gencode_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**gene_symbol_upper** | **str** |  | 
**nes** | **float** |  | 
**p_value** | **float** |  | 
**pos** | **int** |  | 
**snp_id** | **str** |  | [optional] 
**tissue_site_detail_id** | **str** |  | 
**variant_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.single_tissue_eqtl import SingleTissueEqtl

# TODO update the JSON string below
json = "{}"
# create an instance of SingleTissueEqtl from a JSON string
single_tissue_eqtl_instance = SingleTissueEqtl.from_json(json)
# print the JSON string representation of the object
print(SingleTissueEqtl.to_json())

# convert the object into a dict
single_tissue_eqtl_dict = single_tissue_eqtl_instance.to_dict()
# create an instance of SingleTissueEqtl from a dict
single_tissue_eqtl_from_dict = SingleTissueEqtl.from_dict(single_tissue_eqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


