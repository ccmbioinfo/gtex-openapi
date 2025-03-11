# OpenAccessFile

Encapsulates the information about a single downloadable file displayed on the downloads page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**description** | **str** |  | 
**file_size** | **int** |  | 
**url** | **str** |  | 
**order** | **int** |  | 
**parent** | **str** |  | 

## Example

```python
from gtex_openapi.models.open_access_file import OpenAccessFile

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAccessFile from a JSON string
open_access_file_instance = OpenAccessFile.from_json(json)
# print the JSON string representation of the object
print(OpenAccessFile.to_json())

# convert the object into a dict
open_access_file_dict = open_access_file_instance.to_dict()
# create an instance of OpenAccessFile from a dict
open_access_file_from_dict = OpenAccessFile.from_dict(open_access_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


