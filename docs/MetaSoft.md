# MetaSoft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gencode_id** | **str** |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**meta_p** | **float** |  | 
**variant_id** | **str** |  | 
**tissues** | [**Dict[str, TissueLevelMetasoftInfo]**](TissueLevelMetasoftInfo.md) |  | 

## Example

```python
from gtex_openapi.models.meta_soft import MetaSoft

# TODO update the JSON string below
json = "{}"
# create an instance of MetaSoft from a JSON string
meta_soft_instance = MetaSoft.from_json(json)
# print the JSON string representation of the object
print(MetaSoft.to_json())

# convert the object into a dict
meta_soft_dict = meta_soft_instance.to_dict()
# create an instance of MetaSoft from a dict
meta_soft_from_dict = MetaSoft.from_dict(meta_soft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


