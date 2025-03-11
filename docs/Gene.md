# Gene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chromosome** | [**Chromosome**](Chromosome.md) |  | 
**data_source** | **str** |  | 
**description** | **str** |  | [optional] 
**end** | **int** |  | 
**entrez_gene_id** | **str** |  | [optional] 
**gencode_id** | **str** |  | 
**gencode_version** | [**AppModelsResponsesGencodeVersion**](AppModelsResponsesGencodeVersion.md) |  | 
**gene_status** | **str** |  | 
**gene_symbol** | **str** |  | 
**gene_symbol_upper** | **str** |  | 
**gene_type** | **str** |  | 
**genome_build** | [**AppModelsResponsesGenomeBuild**](AppModelsResponsesGenomeBuild.md) |  | 
**start** | **int** |  | 
**strand** | [**Strand**](Strand.md) |  | 
**tss** | **int** |  | 

## Example

```python
from gtex_openapi.models.gene import Gene

# TODO update the JSON string below
json = "{}"
# create an instance of Gene from a JSON string
gene_instance = Gene.from_json(json)
# print the JSON string representation of the object
print(Gene.to_json())

# convert the object into a dict
gene_dict = gene_instance.to_dict()
# create an instance of Gene from a dict
gene_from_dict = Gene.from_dict(gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


