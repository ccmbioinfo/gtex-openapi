# ISqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_type** | [**CellType**](CellType.md) |  | 
**data** | **List[float]** |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**enrichment_scores** | **List[float]** |  | 
**phenotype_id** | **str** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**variant_id** | **str** |  | 
**genotypes** | **List[int]** |  | 
**regression_coord** | **object** |  | 

## Example

```python
from gtex_openapi.models.i_sqtl import ISqtl

# TODO update the JSON string below
json = "{}"
# create an instance of ISqtl from a JSON string
i_sqtl_instance = ISqtl.from_json(json)
# print the JSON string representation of the object
print(ISqtl.to_json())

# convert the object into a dict
i_sqtl_dict = i_sqtl_instance.to_dict()
# create an instance of ISqtl from a dict
i_sqtl_from_dict = ISqtl.from_dict(i_sqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


