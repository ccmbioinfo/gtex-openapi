# CollapsedGeneModelExon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_type** | **str** |  | 
**end** | **int** |  | 
**genome_build** | [**AppModelsResponsesGenomeBuild**](AppModelsResponsesGenomeBuild.md) |  | 
**chromosome** | [**Chromosome**](Chromosome.md) |  | 
**exon_number** | **str** |  | 
**gene_symbol_upper** | **str** |  | 
**exon_id** | **str** |  | 
**dataset_id** | **str** |  | 
**start** | **int** |  | 
**data_source** | **str** |  | 
**gencode_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**gencode_version** | [**AppModelsResponsesGencodeVersion**](AppModelsResponsesGencodeVersion.md) |  | 
**strand** | [**Strand**](Strand.md) |  | 

## Example

```python
from gtex_openapi.models.collapsed_gene_model_exon import CollapsedGeneModelExon

# TODO update the JSON string below
json = "{}"
# create an instance of CollapsedGeneModelExon from a JSON string
collapsed_gene_model_exon_instance = CollapsedGeneModelExon.from_json(json)
# print the JSON string representation of the object
print(CollapsedGeneModelExon.to_json())

# convert the object into a dict
collapsed_gene_model_exon_dict = collapsed_gene_model_exon_instance.to_dict()
# create an instance of CollapsedGeneModelExon from a dict
collapsed_gene_model_exon_from_dict = CollapsedGeneModelExon.from_dict(collapsed_gene_model_exon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


