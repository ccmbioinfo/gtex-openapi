# PaginatedResponseSingleTissueIEqtl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SingleTissueIEqtl]**](SingleTissueIEqtl.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_single_tissue_i_eqtl import PaginatedResponseSingleTissueIEqtl

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseSingleTissueIEqtl from a JSON string
paginated_response_single_tissue_i_eqtl_instance = PaginatedResponseSingleTissueIEqtl.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseSingleTissueIEqtl.to_json())

# convert the object into a dict
paginated_response_single_tissue_i_eqtl_dict = paginated_response_single_tissue_i_eqtl_instance.to_dict()
# create an instance of PaginatedResponseSingleTissueIEqtl from a dict
paginated_response_single_tissue_i_eqtl_from_dict = PaginatedResponseSingleTissueIEqtl.from_dict(paginated_response_single_tissue_i_eqtl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


