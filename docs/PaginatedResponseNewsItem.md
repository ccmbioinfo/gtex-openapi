# PaginatedResponseNewsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NewsItem]**](NewsItem.md) |  | 
**paging_info** | [**PaginationInfo**](PaginationInfo.md) |  | 

## Example

```python
from gtex_openapi.models.paginated_response_news_item import PaginatedResponseNewsItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseNewsItem from a JSON string
paginated_response_news_item_instance = PaginatedResponseNewsItem.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseNewsItem.to_json())

# convert the object into a dict
paginated_response_news_item_dict = paginated_response_news_item_instance.to_dict()
# create an instance of PaginatedResponseNewsItem from a dict
paginated_response_news_item_from_dict = PaginatedResponseNewsItem.from_dict(paginated_response_news_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


