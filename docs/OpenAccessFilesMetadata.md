# OpenAccessFilesMetadata

Project Level Open Access Files Metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OpenAccessFolder]**](OpenAccessFolder.md) |  | 

## Example

```python
from gtex_openapi.models.open_access_files_metadata import OpenAccessFilesMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAccessFilesMetadata from a JSON string
open_access_files_metadata_instance = OpenAccessFilesMetadata.from_json(json)
# print the JSON string representation of the object
print(OpenAccessFilesMetadata.to_json())

# convert the object into a dict
open_access_files_metadata_dict = open_access_files_metadata_instance.to_dict()
# create an instance of OpenAccessFilesMetadata from a dict
open_access_files_metadata_from_dict = OpenAccessFilesMetadata.from_dict(open_access_files_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


