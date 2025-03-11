# PaginatedResponseMedianTranscriptExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MedianTranscriptExpression]**](MedianTranscriptExpression.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_median_transcript_expression import PaginatedResponseMedianTranscriptExpression

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseMedianTranscriptExpression from a JSON string
paginated_response_median_transcript_expression_instance = PaginatedResponseMedianTranscriptExpression.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseMedianTranscriptExpression.to_json())

# convert the object into a dict
paginated_response_median_transcript_expression_dict = paginated_response_median_transcript_expression_instance.to_dict()
# create an instance of PaginatedResponseMedianTranscriptExpression from a dict
paginated_response_median_transcript_expression_from_dict = PaginatedResponseMedianTranscriptExpression.from_dict(paginated_response_median_transcript_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


