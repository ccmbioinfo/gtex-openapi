# ClusteredMedianJunctionExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | **Dict[str, str]** |  | [optional] 
**median_junction_expression** | [**List[MedianJunctionExpression]**](MedianJunctionExpression.md) |  | 

## Example

```python
from gtex_openapi.models.clustered_median_junction_expression import ClusteredMedianJunctionExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ClusteredMedianJunctionExpression from a JSON string
clustered_median_junction_expression_instance = ClusteredMedianJunctionExpression.from_json(json)
# print the JSON string representation of the object
print(ClusteredMedianJunctionExpression.to_json())

# convert the object into a dict
clustered_median_junction_expression_dict = clustered_median_junction_expression_instance.to_dict()
# create an instance of ClusteredMedianJunctionExpression from a dict
clustered_median_junction_expression_from_dict = ClusteredMedianJunctionExpression.from_dict(clustered_median_junction_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


