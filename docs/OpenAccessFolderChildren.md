# OpenAccessFolderChildren

Each folder can contain both files and folders. Both fields are required but they can be empty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[OpenAccessFile]**](OpenAccessFile.md) |  | 
**folders** | [**List[OpenAccessFolder]**](OpenAccessFolder.md) |  | 

## Example

```python
from gtex_openapi.models.open_access_folder_children import OpenAccessFolderChildren

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAccessFolderChildren from a JSON string
open_access_folder_children_instance = OpenAccessFolderChildren.from_json(json)
# print the JSON string representation of the object
print(OpenAccessFolderChildren.to_json())

# convert the object into a dict
open_access_folder_children_dict = open_access_folder_children_instance.to_dict()
# create an instance of OpenAccessFolderChildren from a dict
open_access_folder_children_from_dict = OpenAccessFolderChildren.from_dict(open_access_folder_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


