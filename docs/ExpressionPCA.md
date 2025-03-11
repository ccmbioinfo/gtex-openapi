# ExpressionPCA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pc1** | **float** |  | 
**pc2** | **float** |  | 
**pc3** | **float** |  | 
**sample_id** | **str** |  | 
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 

## Example

```python
from gtex_openapi.models.expression_pca import ExpressionPCA

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionPCA from a JSON string
expression_pca_instance = ExpressionPCA.from_json(json)
# print the JSON string representation of the object
print(ExpressionPCA.to_json())

# convert the object into a dict
expression_pca_dict = expression_pca_instance.to_dict()
# create an instance of ExpressionPCA from a dict
expression_pca_from_dict = ExpressionPCA.from_dict(expression_pca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


