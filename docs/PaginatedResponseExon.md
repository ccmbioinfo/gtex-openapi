# PaginatedResponseExon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Exon]**](Exon.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_exon import PaginatedResponseExon

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseExon from a JSON string
paginated_response_exon_instance = PaginatedResponseExon.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseExon.to_json())

# convert the object into a dict
paginated_response_exon_dict = paginated_response_exon_instance.to_dict()
# create an instance of PaginatedResponseExon from a dict
paginated_response_exon_from_dict = PaginatedResponseExon.from_dict(paginated_response_exon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


