# SingleTissueSqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snp_id** | **str** |  | [optional] 
**pos** | **int** |  | 
**snp_id_upper** | **str** |  | [optional] 
**variant_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**p_value** | **float** |  | 
**gene_symbol_upper** | **str** |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**chromosome** | [**Chromosome**](Chromosome.md) |  | 
**gencode_id** | **str** |  | 
**nes** | **float** |  | 
**phenotype_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.single_tissue_sqtl import SingleTissueSqtl

# TODO update the JSON string below
json = "{}"
# create an instance of SingleTissueSqtl from a JSON string
single_tissue_sqtl_instance = SingleTissueSqtl.from_json(json)
# print the JSON string representation of the object
print(SingleTissueSqtl.to_json())

# convert the object into a dict
single_tissue_sqtl_dict = single_tissue_sqtl_instance.to_dict()
# create an instance of SingleTissueSqtl from a dict
single_tissue_sqtl_from_dict = SingleTissueSqtl.from_dict(single_tissue_sqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


