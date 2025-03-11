# PostEqtlError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | 
**variant_id** | **str** |  | [optional] 
**gencode_id** | **str** |  | [optional] 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | [optional] 

## Example

```python
from gtex_openapi.models.post_eqtl_error import PostEqtlError

# TODO update the JSON string below
json = "{}"
# create an instance of PostEqtlError from a JSON string
post_eqtl_error_instance = PostEqtlError.from_json(json)
# print the JSON string representation of the object
print(PostEqtlError.to_json())

# convert the object into a dict
post_eqtl_error_dict = post_eqtl_error_instance.to_dict()
# create an instance of PostEqtlError from a dict
post_eqtl_error_from_dict = PostEqtlError.from_dict(post_eqtl_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


