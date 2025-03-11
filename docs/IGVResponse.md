# IGVResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** |  | 
**single_tissue_eqtl** | [**List[SingleTissueEqtl]**](SingleTissueEqtl.md) |  | 

## Example

```python
from gtex_openapi.models.igv_response import IGVResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IGVResponse from a JSON string
igv_response_instance = IGVResponse.from_json(json)
# print the JSON string representation of the object
print(IGVResponse.to_json())

# convert the object into a dict
igv_response_dict = igv_response_instance.to_dict()
# create an instance of IGVResponse from a dict
igv_response_from_dict = IGVResponse.from_dict(igv_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


