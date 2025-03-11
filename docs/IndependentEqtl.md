# IndependentEqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gencode_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**variant_id** | **str** |  | 
**snp_id** | **str** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**rank** | **int** |  | 
**tss_distance** | **int** |  | 
**maf** | **float** |  | 
**p_value** | **float** |  | 
**nes** | **float** |  | 
**chromosome** | [**Chromosome**](Chromosome.md) |  | 
**pos** | **int** |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 

## Example

```python
from gtex_openapi.models.independent_eqtl import IndependentEqtl

# TODO update the JSON string below
json = "{}"
# create an instance of IndependentEqtl from a JSON string
independent_eqtl_instance = IndependentEqtl.from_json(json)
# print the JSON string representation of the object
print(IndependentEqtl.to_json())

# convert the object into a dict
independent_eqtl_dict = independent_eqtl_instance.to_dict()
# create an instance of IndependentEqtl from a dict
independent_eqtl_from_dict = IndependentEqtl.from_dict(independent_eqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


