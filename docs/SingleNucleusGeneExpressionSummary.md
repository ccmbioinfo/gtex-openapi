# SingleNucleusGeneExpressionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**cell_type** | **str** |  | 
**num_cells** | **int** |  | 

## Example

```python
from gtex_openapi.models.single_nucleus_gene_expression_summary import SingleNucleusGeneExpressionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SingleNucleusGeneExpressionSummary from a JSON string
single_nucleus_gene_expression_summary_instance = SingleNucleusGeneExpressionSummary.from_json(json)
# print the JSON string representation of the object
print(SingleNucleusGeneExpressionSummary.to_json())

# convert the object into a dict
single_nucleus_gene_expression_summary_dict = single_nucleus_gene_expression_summary_instance.to_dict()
# create an instance of SingleNucleusGeneExpressionSummary from a dict
single_nucleus_gene_expression_summary_from_dict = SingleNucleusGeneExpressionSummary.from_dict(single_nucleus_gene_expression_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


