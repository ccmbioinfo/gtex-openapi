# ClusteredMedianExonExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | **Dict[str, str]** |  | [optional] 
**median_exon_expression** | [**List[MedianExonExpression]**](MedianExonExpression.md) |  | 

## Example

```python
from gtex_openapi.models.clustered_median_exon_expression import ClusteredMedianExonExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ClusteredMedianExonExpression from a JSON string
clustered_median_exon_expression_instance = ClusteredMedianExonExpression.from_json(json)
# print the JSON string representation of the object
print(ClusteredMedianExonExpression.to_json())

# convert the object into a dict
clustered_median_exon_expression_dict = clustered_median_exon_expression_instance.to_dict()
# create an instance of ClusteredMedianExonExpression from a dict
clustered_median_exon_expression_from_dict = ClusteredMedianExonExpression.from_dict(clustered_median_exon_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


