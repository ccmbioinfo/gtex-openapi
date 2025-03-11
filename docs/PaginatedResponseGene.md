# PaginatedResponseGene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Gene]**](Gene.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_gene import PaginatedResponseGene

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseGene from a JSON string
paginated_response_gene_instance = PaginatedResponseGene.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseGene.to_json())

# convert the object into a dict
paginated_response_gene_dict = paginated_response_gene_instance.to_dict()
# create an instance of PaginatedResponseGene from a dict
paginated_response_gene_from_dict = PaginatedResponseGene.from_dict(paginated_response_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


