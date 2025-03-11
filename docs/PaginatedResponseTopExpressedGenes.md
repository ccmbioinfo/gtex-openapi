# PaginatedResponseTopExpressedGenes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TopExpressedGenes]**](TopExpressedGenes.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_top_expressed_genes import PaginatedResponseTopExpressedGenes

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseTopExpressedGenes from a JSON string
paginated_response_top_expressed_genes_instance = PaginatedResponseTopExpressedGenes.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseTopExpressedGenes.to_json())

# convert the object into a dict
paginated_response_top_expressed_genes_dict = paginated_response_top_expressed_genes_instance.to_dict()
# create an instance of PaginatedResponseTopExpressedGenes from a dict
paginated_response_top_expressed_genes_from_dict = PaginatedResponseTopExpressedGenes.from_dict(paginated_response_top_expressed_genes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


