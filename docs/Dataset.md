# Dataset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** |  | 
**db_snp_build** | **int** |  | 
**dbgap_id** | **str** |  | [optional] 
**description** | **str** |  | 
**display_name** | **str** |  | 
**eqtl_subject_count** | **int** |  | 
**eqtl_tissues_count** | **int** |  | 
**gencode_version** | [**AppModelsResponsesGencodeVersion**](AppModelsResponsesGencodeVersion.md) |  | 
**genome_build** | [**AppModelsResponsesGenomeBuild**](AppModelsResponsesGenomeBuild.md) |  | 
**organization** | **str** |  | 
**rna_seq_and_genotype_sample_count** | **int** |  | 
**rna_seq_sample_count** | **int** |  | 
**subject_count** | **int** |  | 
**tissue_count** | **int** |  | 

## Example

```python
from gtex_openapi.models.dataset import Dataset

# TODO update the JSON string below
json = "{}"
# create an instance of Dataset from a JSON string
dataset_instance = Dataset.from_json(json)
# print the JSON string representation of the object
print(Dataset.to_json())

# convert the object into a dict
dataset_dict = dataset_instance.to_dict()
# create an instance of Dataset from a dict
dataset_from_dict = Dataset.from_dict(dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


