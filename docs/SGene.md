# SGene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n_phenotypes** | **int** |  | 
**p_value_threshold** | **float** |  | 
**phenotype_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**p_value** | **float** |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**empirical_p_value** | **float** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**q_value** | **float** |  | 
**gencode_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.s_gene import SGene

# TODO update the JSON string below
json = "{}"
# create an instance of SGene from a JSON string
s_gene_instance = SGene.from_json(json)
# print the JSON string representation of the object
print(SGene.to_json())

# convert the object into a dict
s_gene_dict = s_gene_instance.to_dict()
# create an instance of SGene from a dict
s_gene_from_dict = SGene.from_dict(s_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


