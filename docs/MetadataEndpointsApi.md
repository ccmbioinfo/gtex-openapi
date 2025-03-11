# gtex_openapi.MetadataEndpointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset_info_api_v2_metadata_dataset_get**](MetadataEndpointsApi.md#get_dataset_info_api_v2_metadata_dataset_get) | **GET** /api/v2/metadata/dataset | Get Dataset Info


# **get_dataset_info_api_v2_metadata_dataset_get**
> List[Dataset] get_dataset_info_api_v2_metadata_dataset_get(dataset_id=dataset_id, organization_name=organization_name)

Get Dataset Info

### Example


```python
import gtex_openapi
from gtex_openapi.models.dataset import Dataset
from gtex_openapi.models.dataset_id import DatasetId
from gtex_openapi.models.organization_names import OrganizationNames
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
    api_instance = gtex_openapi.MetadataEndpointsApi(api_client)
    dataset_id = gtex_openapi.DatasetId() # DatasetId |  (optional)
    organization_name = gtex_openapi.OrganizationNames() # OrganizationNames |  (optional)

    try:
        # Get Dataset Info
        api_response = api_instance.get_dataset_info_api_v2_metadata_dataset_get(dataset_id=dataset_id, organization_name=organization_name)
        print("The response of MetadataEndpointsApi->get_dataset_info_api_v2_metadata_dataset_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataEndpointsApi->get_dataset_info_api_v2_metadata_dataset_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | [**DatasetId**](.md)|  | [optional] 
 **organization_name** | [**OrganizationNames**](.md)|  | [optional] 

### Return type

[**List[Dataset]**](Dataset.md)

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

