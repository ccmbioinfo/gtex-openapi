# OpenAccessFolder

Encapsulates the information about a single grouping of files on the downloads page. Folders include front-end artefacts such as Tabs, Releases, File Groups, e.t.c

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**display_name** | **str** |  | 
**description** | **str** |  | 
**order** | **int** |  | 
**parent** | **str** |  | 
**children** | [**OpenAccessFolderChildren**](OpenAccessFolderChildren.md) |  | 

## Example

```python
from gtex_openapi.models.open_access_folder import OpenAccessFolder

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAccessFolder from a JSON string
open_access_folder_instance = OpenAccessFolder.from_json(json)
# print the JSON string representation of the object
print(OpenAccessFolder.to_json())

# convert the object into a dict
open_access_folder_dict = open_access_folder_instance.to_dict()
# create an instance of OpenAccessFolder from a dict
open_access_folder_from_dict = OpenAccessFolder.from_dict(open_access_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


