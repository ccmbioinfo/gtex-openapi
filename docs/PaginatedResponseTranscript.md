# PaginatedResponseTranscript


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Transcript]**](Transcript.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_transcript import PaginatedResponseTranscript

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseTranscript from a JSON string
paginated_response_transcript_instance = PaginatedResponseTranscript.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseTranscript.to_json())

# convert the object into a dict
paginated_response_transcript_dict = paginated_response_transcript_instance.to_dict()
# create an instance of PaginatedResponseTranscript from a dict
paginated_response_transcript_from_dict = PaginatedResponseTranscript.from_dict(paginated_response_transcript_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


