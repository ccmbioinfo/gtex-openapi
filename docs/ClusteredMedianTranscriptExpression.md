# ClusteredMedianTranscriptExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | **Dict[str, str]** |  | [optional] 
**median_transcript_expression** | [**List[MedianTranscriptExpression]**](MedianTranscriptExpression.md) |  | 

## Example

```python
from gtex_openapi.models.clustered_median_transcript_expression import ClusteredMedianTranscriptExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ClusteredMedianTranscriptExpression from a JSON string
clustered_median_transcript_expression_instance = ClusteredMedianTranscriptExpression.from_json(json)
# print the JSON string representation of the object
print(ClusteredMedianTranscriptExpression.to_json())

# convert the object into a dict
clustered_median_transcript_expression_dict = clustered_median_transcript_expression_instance.to_dict()
# create an instance of ClusteredMedianTranscriptExpression from a dict
clustered_median_transcript_expression_from_dict = ClusteredMedianTranscriptExpression.from_dict(clustered_median_transcript_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


