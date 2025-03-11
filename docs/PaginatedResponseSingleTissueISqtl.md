# PaginatedResponseSingleTissueISqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SingleTissueISqtl]**](SingleTissueISqtl.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_single_tissue_i_sqtl import PaginatedResponseSingleTissueISqtl

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseSingleTissueISqtl from a JSON string
paginated_response_single_tissue_i_sqtl_instance = PaginatedResponseSingleTissueISqtl.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseSingleTissueISqtl.to_json())

# convert the object into a dict
paginated_response_single_tissue_i_sqtl_dict = paginated_response_single_tissue_i_sqtl_instance.to_dict()
# create an instance of PaginatedResponseSingleTissueISqtl from a dict
paginated_response_single_tissue_i_sqtl_from_dict = PaginatedResponseSingleTissueISqtl.from_dict(paginated_response_single_tissue_i_sqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


