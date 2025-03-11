# PaginatedResponseGWAS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GWAS]**](GWAS.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_gwas import PaginatedResponseGWAS

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseGWAS from a JSON string
paginated_response_gwas_instance = PaginatedResponseGWAS.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseGWAS.to_json())

# convert the object into a dict
paginated_response_gwas_dict = paginated_response_gwas_instance.to_dict()
# create an instance of PaginatedResponseGWAS from a dict
paginated_response_gwas_from_dict = PaginatedResponseGWAS.from_dict(paginated_response_gwas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


