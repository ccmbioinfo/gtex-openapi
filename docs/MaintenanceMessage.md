# MaintenanceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**date_created** | [**Datecreated**](Datecreated.md) |  | 
**release** | **str** |  | 

## Example

```python
from gtex_openapi.models.maintenance_message import MaintenanceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceMessage from a JSON string
maintenance_message_instance = MaintenanceMessage.from_json(json)
# print the JSON string representation of the object
print(MaintenanceMessage.to_json())

# convert the object into a dict
maintenance_message_dict = maintenance_message_instance.to_dict()
# create an instance of MaintenanceMessage from a dict
maintenance_message_from_dict = MaintenanceMessage.from_dict(maintenance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


