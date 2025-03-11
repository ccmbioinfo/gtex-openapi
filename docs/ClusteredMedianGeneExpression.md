# ClusteredMedianGeneExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | **Dict[str, str]** |  | [optional] 
**median_gene_expression** | [**List[MedianGeneExpression]**](MedianGeneExpression.md) |  | 

## Example

```python
from gtex_openapi.models.clustered_median_gene_expression import ClusteredMedianGeneExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ClusteredMedianGeneExpression from a JSON string
clustered_median_gene_expression_instance = ClusteredMedianGeneExpression.from_json(json)
# print the JSON string representation of the object
print(ClusteredMedianGeneExpression.to_json())

# convert the object into a dict
clustered_median_gene_expression_dict = clustered_median_gene_expression_instance.to_dict()
# create an instance of ClusteredMedianGeneExpression from a dict
clustered_median_gene_expression_from_dict = ClusteredMedianGeneExpression.from_dict(clustered_median_gene_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


