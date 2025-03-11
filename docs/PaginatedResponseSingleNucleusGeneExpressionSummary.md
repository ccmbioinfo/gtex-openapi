# PaginatedResponseSingleNucleusGeneExpressionSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SingleNucleusGeneExpressionSummary]**](SingleNucleusGeneExpressionSummary.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_single_nucleus_gene_expression_summary import PaginatedResponseSingleNucleusGeneExpressionSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseSingleNucleusGeneExpressionSummary from a JSON string
paginated_response_single_nucleus_gene_expression_summary_instance = PaginatedResponseSingleNucleusGeneExpressionSummary.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseSingleNucleusGeneExpressionSummary.to_json())

# convert the object into a dict
paginated_response_single_nucleus_gene_expression_summary_dict = paginated_response_single_nucleus_gene_expression_summary_instance.to_dict()
# create an instance of PaginatedResponseSingleNucleusGeneExpressionSummary from a dict
paginated_response_single_nucleus_gene_expression_summary_from_dict = PaginatedResponseSingleNucleusGeneExpressionSummary.from_dict(paginated_response_single_nucleus_gene_expression_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


