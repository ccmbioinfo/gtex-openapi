# TopExpressedGenes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**gencode_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**median** | **float** |  | 
**unit** | [**Units**](Units.md) |  | 

## Example

```python
from gtex_openapi.models.top_expressed_genes import TopExpressedGenes

# TODO update the JSON string below
json = "{}"
# create an instance of TopExpressedGenes from a JSON string
top_expressed_genes_instance = TopExpressedGenes.from_json(json)
# print the JSON string representation of the object
print(TopExpressedGenes.to_json())

# convert the object into a dict
top_expressed_genes_dict = top_expressed_genes_instance.to_dict()
# create an instance of TopExpressedGenes from a dict
top_expressed_genes_from_dict = TopExpressedGenes.from_dict(top_expressed_genes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


