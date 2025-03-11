# MedianGeneExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**median** | **float** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**gencode_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**unit** | [**Units**](Units.md) |  | 

## Example

```python
from gtex_openapi.models.median_gene_expression import MedianGeneExpression

# TODO update the JSON string below
json = "{}"
# create an instance of MedianGeneExpression from a JSON string
median_gene_expression_instance = MedianGeneExpression.from_json(json)
# print the JSON string representation of the object
print(MedianGeneExpression.to_json())

# convert the object into a dict
median_gene_expression_dict = median_gene_expression_instance.to_dict()
# create an instance of MedianGeneExpression from a dict
median_gene_expression_from_dict = MedianGeneExpression.from_dict(median_gene_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


