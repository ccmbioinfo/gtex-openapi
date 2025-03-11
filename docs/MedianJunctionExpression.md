# MedianJunctionExpression


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**median** | **float** |  | 
**junction_id** | **str** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**gencode_id** | **str** |  | 
**gene_symbol** | **str** |  | 
**unit** | [**Units**](Units.md) |  | 

## Example

```python
from gtex_openapi.models.median_junction_expression import MedianJunctionExpression

# TODO update the JSON string below
json = "{}"
# create an instance of MedianJunctionExpression from a JSON string
median_junction_expression_instance = MedianJunctionExpression.from_json(json)
# print the JSON string representation of the object
print(MedianJunctionExpression.to_json())

# convert the object into a dict
median_junction_expression_dict = median_junction_expression_instance.to_dict()
# create an instance of MedianJunctionExpression from a dict
median_junction_expression_from_dict = MedianJunctionExpression.from_dict(median_junction_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


