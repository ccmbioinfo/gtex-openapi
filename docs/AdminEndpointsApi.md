# gtex_openapi.AdminEndpointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_maintenance_message_api_v2_admin_maintenance_message_get**](AdminEndpointsApi.md#get_maintenance_message_api_v2_admin_maintenance_message_get) | **GET** /api/v2/admin/maintenanceMessage | Get Maintenance Message
[**get_news_item_api_v2_admin_news_item_get**](AdminEndpointsApi.md#get_news_item_api_v2_admin_news_item_get) | **GET** /api/v2/admin/newsItem | Get News Item


# **get_maintenance_message_api_v2_admin_maintenance_message_get**
> PaginatedResponseMaintenanceMessage get_maintenance_message_api_v2_admin_maintenance_message_get(page=page, items_per_page=items_per_page)

Get Maintenance Message

Getting all the maintenance messages from the database that are enabled

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_maintenance_message import PaginatedResponseMaintenanceMessage
from gtex_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gtex_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with gtex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gtex_openapi.AdminEndpointsApi(api_client)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Maintenance Message
        api_response = api_instance.get_maintenance_message_api_v2_admin_maintenance_message_get(page=page, items_per_page=items_per_page)
        print("The response of AdminEndpointsApi->get_maintenance_message_api_v2_admin_maintenance_message_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEndpointsApi->get_maintenance_message_api_v2_admin_maintenance_message_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseMaintenanceMessage**](PaginatedResponseMaintenanceMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_item_api_v2_admin_news_item_get**
> PaginatedResponseNewsItem get_news_item_api_v2_admin_news_item_get(page=page, items_per_page=items_per_page)

Get News Item

Getting all the news items from the database that are current

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_news_item import PaginatedResponseNewsItem
from gtex_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gtex_openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with gtex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gtex_openapi.AdminEndpointsApi(api_client)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get News Item
        api_response = api_instance.get_news_item_api_v2_admin_news_item_get(page=page, items_per_page=items_per_page)
        print("The response of AdminEndpointsApi->get_news_item_api_v2_admin_news_item_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEndpointsApi->get_news_item_api_v2_admin_news_item_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseNewsItem**](PaginatedResponseNewsItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

