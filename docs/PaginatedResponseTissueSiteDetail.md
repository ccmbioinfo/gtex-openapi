# PaginatedResponseTissueSiteDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TissueSiteDetail]**](TissueSiteDetail.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_tissue_site_detail import PaginatedResponseTissueSiteDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseTissueSiteDetail from a JSON string
paginated_response_tissue_site_detail_instance = PaginatedResponseTissueSiteDetail.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseTissueSiteDetail.to_json())

# convert the object into a dict
paginated_response_tissue_site_detail_dict = paginated_response_tissue_site_detail_instance.to_dict()
# create an instance of PaginatedResponseTissueSiteDetail from a dict
paginated_response_tissue_site_detail_from_dict = PaginatedResponseTissueSiteDetail.from_dict(paginated_response_tissue_site_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


