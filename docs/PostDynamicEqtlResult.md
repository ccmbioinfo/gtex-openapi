# PostDynamicEqtlResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PostEqtl]**](PostEqtl.md) |  | 
**errors** | [**List[PostEqtlError]**](PostEqtlError.md) |  | 

## Example

```python
from gtex_openapi.models.post_dynamic_eqtl_result import PostDynamicEqtlResult

# TODO update the JSON string below
json = "{}"
# create an instance of PostDynamicEqtlResult from a JSON string
post_dynamic_eqtl_result_instance = PostDynamicEqtlResult.from_json(json)
# print the JSON string representation of the object
print(PostDynamicEqtlResult.to_json())

# convert the object into a dict
post_dynamic_eqtl_result_dict = post_dynamic_eqtl_result_instance.to_dict()
# create an instance of PostDynamicEqtlResult from a dict
post_dynamic_eqtl_result_from_dict = PostDynamicEqtlResult.from_dict(post_dynamic_eqtl_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


