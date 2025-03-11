# gtex_openapi.HistologyEndpointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image_api_v2_histology_image_get**](HistologyEndpointsApi.md#get_image_api_v2_histology_image_get) | **GET** /api/v2/histology/image | Get Image


# **get_image_api_v2_histology_image_get**
> PaginatedResponseHistologySample get_image_api_v2_histology_image_get(tissue_sample_id=tissue_sample_id, page=page, items_per_page=items_per_page)

Get Image

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_histology_sample import PaginatedResponseHistologySample
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
    api_instance = gtex_openapi.HistologyEndpointsApi(api_client)
    tissue_sample_id = ['tissue_sample_id_example'] # List[str] | A list of Tissue Sample ID(s) (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Image
        api_response = api_instance.get_image_api_v2_histology_image_get(tissue_sample_id=tissue_sample_id, page=page, items_per_page=items_per_page)
        print("The response of HistologyEndpointsApi->get_image_api_v2_histology_image_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistologyEndpointsApi->get_image_api_v2_histology_image_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tissue_sample_id** | [**List[str]**](str.md)| A list of Tissue Sample ID(s) | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseHistologySample**](PaginatedResponseHistologySample.md)

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

