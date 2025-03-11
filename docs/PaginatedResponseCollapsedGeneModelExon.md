# PaginatedResponseCollapsedGeneModelExon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CollapsedGeneModelExon]**](CollapsedGeneModelExon.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_collapsed_gene_model_exon import PaginatedResponseCollapsedGeneModelExon

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseCollapsedGeneModelExon from a JSON string
paginated_response_collapsed_gene_model_exon_instance = PaginatedResponseCollapsedGeneModelExon.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseCollapsedGeneModelExon.to_json())

# convert the object into a dict
paginated_response_collapsed_gene_model_exon_dict = paginated_response_collapsed_gene_model_exon_instance.to_dict()
# create an instance of PaginatedResponseCollapsedGeneModelExon from a dict
paginated_response_collapsed_gene_model_exon_from_dict = PaginatedResponseCollapsedGeneModelExon.from_dict(paginated_response_collapsed_gene_model_exon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


