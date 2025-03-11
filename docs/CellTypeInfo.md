# CellTypeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cell_type** | **str** |  | 
**count** | **int** |  | 
**mean_with_zeros** | **float** |  | 
**mean_without_zeros** | **float** |  | 
**median_with_zeros** | **float** |  | 
**median_without_zeros** | **float** |  | 
**num_zeros** | **int** |  | 
**data** | **List[float]** |  | [optional] 

## Example

```python
from gtex_openapi.models.cell_type_info import CellTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CellTypeInfo from a JSON string
cell_type_info_instance = CellTypeInfo.from_json(json)
# print the JSON string representation of the object
print(CellTypeInfo.to_json())

# convert the object into a dict
cell_type_info_dict = cell_type_info_instance.to_dict()
# create an instance of CellTypeInfo from a dict
cell_type_info_from_dict = CellTypeInfo.from_dict(cell_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


