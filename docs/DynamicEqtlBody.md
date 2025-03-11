# DynamicEqtlBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant_id** | **str** |  | 
**gencode_id** | **str** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 

## Example

```python
from gtex_openapi.models.dynamic_eqtl_body import DynamicEqtlBody

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicEqtlBody from a JSON string
dynamic_eqtl_body_instance = DynamicEqtlBody.from_json(json)
# print the JSON string representation of the object
print(DynamicEqtlBody.to_json())

# convert the object into a dict
dynamic_eqtl_body_dict = dynamic_eqtl_body_instance.to_dict()
# create an instance of DynamicEqtlBody from a dict
dynamic_eqtl_body_from_dict = DynamicEqtlBody.from_dict(dynamic_eqtl_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


