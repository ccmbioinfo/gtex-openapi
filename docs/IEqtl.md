# IEqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_type** | [**CellType**](CellType.md) |  | 
**data** | **List[float]** |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**enrichment_scores** | **List[float]** |  | 
**gencode_id** | **str** |  | 
**genotypes** | **List[int]** |  | 
**regression_coord** | **object** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**variant_id** | **str** |  | 

## Example

```python
from gtex_openapi.models.i_eqtl import IEqtl

# TODO update the JSON string below
json = "{}"
# create an instance of IEqtl from a JSON string
i_eqtl_instance = IEqtl.from_json(json)
# print the JSON string representation of the object
print(IEqtl.to_json())

# convert the object into a dict
i_eqtl_dict = i_eqtl_instance.to_dict()
# create an instance of IEqtl from a dict
i_eqtl_from_dict = IEqtl.from_dict(i_eqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


