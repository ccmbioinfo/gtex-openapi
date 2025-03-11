# ServiceInfo

The `ServiceInfo` object provides a structured format for describing web services implementing GA4GH API specifications. RNA-get implements service info through the standard `/service-info` API endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**version** | **str** |  | 
**organization** | [**Organization**](Organization.md) |  | 
**description** | **str** |  | [optional] 
**contact_url** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 

## Example

```python
from gtex_openapi.models.service_info import ServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceInfo from a JSON string
service_info_instance = ServiceInfo.from_json(json)
# print the JSON string representation of the object
print(ServiceInfo.to_json())

# convert the object into a dict
service_info_dict = service_info_instance.to_dict()
# create an instance of ServiceInfo from a dict
service_info_from_dict = ServiceInfo.from_dict(service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


