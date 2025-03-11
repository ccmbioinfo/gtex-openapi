# Variant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snp_id** | **str** |  | 
**b37_variant_id** | **str** |  | 
**pos** | **int** |  | 
**maf01** | **bool** |  | 
**variant_id** | **str** |  | 
**alt** | **str** |  | 
**chromosome** | [**Chromosome**](Chromosome.md) |  | 
**snp_id_upper** | **str** |  | 
**dataset_id** | **str** |  | 
**ref** | **str** |  | 
**shorthand** | **str** |  | [optional] 

## Example

```python
from gtex_openapi.models.variant import Variant

# TODO update the JSON string below
json = "{}"
# create an instance of Variant from a JSON string
variant_instance = Variant.from_json(json)
# print the JSON string representation of the object
print(Variant.to_json())

# convert the object into a dict
variant_dict = variant_instance.to_dict()
# create an instance of Variant from a dict
variant_from_dict = Variant.from_dict(variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


