# TissueLevelMetasoftInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_value** | **float** |  | [optional] 
**p_value** | **float** |  | [optional] 
**se** | **float** |  | [optional] 
**nes** | **float** |  | [optional] 

## Example

```python
from gtex_openapi.models.tissue_level_metasoft_info import TissueLevelMetasoftInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TissueLevelMetasoftInfo from a JSON string
tissue_level_metasoft_info_instance = TissueLevelMetasoftInfo.from_json(json)
# print the JSON string representation of the object
print(TissueLevelMetasoftInfo.to_json())

# convert the object into a dict
tissue_level_metasoft_info_dict = tissue_level_metasoft_info_instance.to_dict()
# create an instance of TissueLevelMetasoftInfo from a dict
tissue_level_metasoft_info_from_dict = TissueLevelMetasoftInfo.from_dict(tissue_level_metasoft_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


