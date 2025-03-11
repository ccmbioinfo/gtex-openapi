# FunctionalAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant_id** | **str** |  | 
**enhancer** | **bool** |  | 
**promoter** | **bool** |  | 
**open_chromatin_region** | **bool** |  | 
**promoter_flanking_region** | **bool** |  | 
**ctcf_binding_site** | **bool** |  | 
**tf_binding_site** | **bool** |  | 
**var_3_prime_utr_variant** | **bool** |  | 
**var_5_prime_utr_variant** | **bool** |  | 
**frameshift_variant** | **bool** |  | 
**intron_variant** | **bool** |  | 
**missense_variant** | **bool** |  | 
**non_coding_transcript_exon_variant** | **bool** |  | 
**splice_acceptor_variant** | **bool** |  | 
**splice_donor_variant** | **bool** |  | 
**splice_region_variant** | **bool** |  | 
**stop_gained** | **bool** |  | 
**synonymous_variant** | **bool** |  | 
**chromosome** | [**Chromosome**](Chromosome.md) |  | 
**pos** | **int** |  | 
**ref** | **str** |  | 
**alt** | **str** |  | 
**dataset_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.functional_annotation import FunctionalAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionalAnnotation from a JSON string
functional_annotation_instance = FunctionalAnnotation.from_json(json)
# print the JSON string representation of the object
print(FunctionalAnnotation.to_json())

# convert the object into a dict
functional_annotation_dict = functional_annotation_instance.to_dict()
# create an instance of FunctionalAnnotation from a dict
functional_annotation_from_dict = FunctionalAnnotation.from_dict(functional_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


