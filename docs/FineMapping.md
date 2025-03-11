# FineMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**gencode_id** | **str** |  | 
**method** | **str** |  | 
**pip** | **float** |  | 
**set_id** | **int** |  | 
**set_size** | **int** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**variant_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.fine_mapping import FineMapping

# TODO update the JSON string below
json = "{}"
# create an instance of FineMapping from a JSON string
fine_mapping_instance = FineMapping.from_json(json)
# print the JSON string representation of the object
print(FineMapping.to_json())

# convert the object into a dict
fine_mapping_dict = fine_mapping_instance.to_dict()
# create an instance of FineMapping from a dict
fine_mapping_from_dict = FineMapping.from_dict(fine_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


