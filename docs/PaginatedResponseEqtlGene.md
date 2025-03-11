# PaginatedResponseEqtlGene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EqtlGene]**](EqtlGene.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_eqtl_gene import PaginatedResponseEqtlGene

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseEqtlGene from a JSON string
paginated_response_eqtl_gene_instance = PaginatedResponseEqtlGene.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseEqtlGene.to_json())

# convert the object into a dict
paginated_response_eqtl_gene_dict = paginated_response_eqtl_gene_instance.to_dict()
# create an instance of PaginatedResponseEqtlGene from a dict
paginated_response_eqtl_gene_from_dict = PaginatedResponseEqtlGene.from_dict(paginated_response_eqtl_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


