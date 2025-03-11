# EqtlGene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**empirical_p_value** | **float** |  | 
**gencode_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**log2_allelic_fold_change** | **float** |  | [optional] 
**p_value** | **float** |  | 
**p_value_threshold** | **float** |  | 
**q_value** | **float** |  | 

## Example

```python
from gtex_openapi.models.eqtl_gene import EqtlGene

# TODO update the JSON string below
json = "{}"
# create an instance of EqtlGene from a JSON string
eqtl_gene_instance = EqtlGene.from_json(json)
# print the JSON string representation of the object
print(EqtlGene.to_json())

# convert the object into a dict
eqtl_gene_dict = eqtl_gene_instance.to_dict()
# create an instance of EqtlGene from a dict
eqtl_gene_from_dict = EqtlGene.from_dict(eqtl_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


