# Exon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_type** | **str** |  | 
**end** | **int** |  | 
**genome_build** | [**AppModelsResponsesGenomeBuild**](AppModelsResponsesGenomeBuild.md) |  | 
**start** | **int** |  | 
**exon_id** | **str** |  | 
**source** | **str** |  | 
**chromosome** | [**Chromosome**](Chromosome.md) |  | 
**gencode_id** | **str** |  | 
**transcript_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**gencode_version** | [**AppModelsResponsesGencodeVersion**](AppModelsResponsesGencodeVersion.md) |  | 
**strand** | [**Strand**](Strand.md) |  | 
**exon_number** | **str** |  | 

## Example

```python
from gtex_openapi.models.exon import Exon

# TODO update the JSON string below
json = "{}"
# create an instance of Exon from a JSON string
exon_instance = Exon.from_json(json)
# print the JSON string representation of the object
print(Exon.to_json())

# convert the object into a dict
exon_dict = exon_instance.to_dict()
# create an instance of Exon from a dict
exon_from_dict = Exon.from_dict(exon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


