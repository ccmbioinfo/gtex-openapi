# PaginatedResponseSGene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SGene]**](SGene.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_s_gene import PaginatedResponseSGene

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseSGene from a JSON string
paginated_response_s_gene_instance = PaginatedResponseSGene.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseSGene.to_json())

# convert the object into a dict
paginated_response_s_gene_dict = paginated_response_s_gene_instance.to_dict()
# create an instance of PaginatedResponseSGene from a dict
paginated_response_s_gene_from_dict = PaginatedResponseSGene.from_dict(paginated_response_s_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


