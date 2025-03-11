# GeneExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[float]** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**gencode_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**unit** | [**Units**](Units.md) |  | 
**subset_group** | [**Subsetgroup**](Subsetgroup.md) |  | [optional] 

## Example

```python
from gtex_openapi.models.gene_expression import GeneExpression

# TODO update the JSON string below
json = "{}"
# create an instance of GeneExpression from a JSON string
gene_expression_instance = GeneExpression.from_json(json)
# print the JSON string representation of the object
print(GeneExpression.to_json())

# convert the object into a dict
gene_expression_dict = gene_expression_instance.to_dict()
# create an instance of GeneExpression from a dict
gene_expression_from_dict = GeneExpression.from_dict(gene_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


