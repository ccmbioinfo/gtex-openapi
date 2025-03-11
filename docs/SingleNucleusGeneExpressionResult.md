# SingleNucleusGeneExpressionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**gencode_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**cell_types** | [**List[CellTypeInfo]**](CellTypeInfo.md) |  | 
**unit** | [**Units**](Units.md) |  | 

## Example

```python
from gtex_openapi.models.single_nucleus_gene_expression_result import SingleNucleusGeneExpressionResult

# TODO update the JSON string below
json = "{}"
# create an instance of SingleNucleusGeneExpressionResult from a JSON string
single_nucleus_gene_expression_result_instance = SingleNucleusGeneExpressionResult.from_json(json)
# print the JSON string representation of the object
print(SingleNucleusGeneExpressionResult.to_json())

# convert the object into a dict
single_nucleus_gene_expression_result_dict = single_nucleus_gene_expression_result_instance.to_dict()
# create an instance of SingleNucleusGeneExpressionResult from a dict
single_nucleus_gene_expression_result_from_dict = SingleNucleusGeneExpressionResult.from_dict(single_nucleus_gene_expression_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


