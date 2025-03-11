# SingleTissueISqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snp_id** | **str** |  | [optional] 
**b_gise** | **float** |  | 
**pos** | **int** |  | 
**snp_id_upper** | **str** |  | [optional] 
**p_value_g** | **float** |  | 
**p_value_gi** | **float** |  | 
**gene_symbol** | **str** |  | 
**gene_symbol_upper** | **str** |  | 
**p_value_i** | **float** |  | 
**b_gi** | **float** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**chromosome** | [**Chromosome**](Chromosome.md) |  | 
**tissue_cell_type** | [**CellType**](CellType.md) |  | 
**tss_distance** | **int** |  | 
**b_gse** | **float** |  | 
**variant_id** | **str** |  | 
**maf** | **float** |  | 
**b_ise** | **float** |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**b_g** | **float** |  | 
**p_value_adjusted_bh** | **float** |  | 
**b_i** | **float** |  | 
**gencode_id** | **str** |  | 
**phenotype_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.single_tissue_i_sqtl import SingleTissueISqtl

# TODO update the JSON string below
json = "{}"
# create an instance of SingleTissueISqtl from a JSON string
single_tissue_i_sqtl_instance = SingleTissueISqtl.from_json(json)
# print the JSON string representation of the object
print(SingleTissueISqtl.to_json())

# convert the object into a dict
single_tissue_i_sqtl_dict = single_tissue_i_sqtl_instance.to_dict()
# create an instance of SingleTissueISqtl from a dict
single_tissue_i_sqtl_from_dict = SingleTissueISqtl.from_dict(single_tissue_i_sqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


