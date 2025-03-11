# gtex_openapi.GTExPortalAPIInfoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_info_api_v2_get**](GTExPortalAPIInfoApi.md#get_service_info_api_v2_get) | **GET** /api/v2/ | Get Service Info


# **get_service_info_api_v2_get**
> ServiceInfo get_service_info_api_v2_get()

Get Service Info

General information about the GTEx service.

### Example


```python
import gtex_openapi
from gtex_openapi.models.service_info import ServiceInfo
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
    api_instance = gtex_openapi.GTExPortalAPIInfoApi(api_client)

    try:
        # Get Service Info
        api_response = api_instance.get_service_info_api_v2_get()
        print("The response of GTExPortalAPIInfoApi->get_service_info_api_v2_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GTExPortalAPIInfoApi->get_service_info_api_v2_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceInfo**](ServiceInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

