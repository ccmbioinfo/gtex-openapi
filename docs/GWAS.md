# GWAS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chromosome** | [**Chromosome**](Chromosome.md) |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**phenotype** | **str** |  | 
**p_value** | **float** |  | [optional] 
**beta** | **float** |  | [optional] 
**pubmed_id** | **int** |  | 
**snp_id** | **str** |  | 
**risk_allele** | **str** |  | [optional] 
**genome_build** | [**AppModelsResponsesGenomeBuild**](AppModelsResponsesGenomeBuild.md) |  | 

## Example

```python
from gtex_openapi.models.gwas import GWAS

# TODO update the JSON string below
json = "{}"
# create an instance of GWAS from a JSON string
gwas_instance = GWAS.from_json(json)
# print the JSON string representation of the object
print(GWAS.to_json())

# convert the object into a dict
gwas_dict = gwas_instance.to_dict()
# create an instance of GWAS from a dict
gwas_from_dict = GWAS.from_dict(gwas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


