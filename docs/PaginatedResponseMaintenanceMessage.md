# PaginatedResponseMaintenanceMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MaintenanceMessage]**](MaintenanceMessage.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_maintenance_message import PaginatedResponseMaintenanceMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseMaintenanceMessage from a JSON string
paginated_response_maintenance_message_instance = PaginatedResponseMaintenanceMessage.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseMaintenanceMessage.to_json())

# convert the object into a dict
paginated_response_maintenance_message_dict = paginated_response_maintenance_message_instance.to_dict()
# create an instance of PaginatedResponseMaintenanceMessage from a dict
paginated_response_maintenance_message_from_dict = PaginatedResponseMaintenanceMessage.from_dict(paginated_response_maintenance_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


