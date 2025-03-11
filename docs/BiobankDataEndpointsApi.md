# gtex_openapi.BiobankDataEndpointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_api_v2_biobank_download_get**](BiobankDataEndpointsApi.md#download_api_v2_biobank_download_get) | **GET** /api/v2/biobank/download | Download
[**get_sample_api_v2_biobank_sample_get**](BiobankDataEndpointsApi.md#get_sample_api_v2_biobank_sample_get) | **GET** /api/v2/biobank/sample | Get Sample


# **download_api_v2_biobank_download_get**
> List[BiobankSample] download_api_v2_biobank_download_get(material_type=material_type, tissue_site_detail_id=tissue_site_detail_id, path_category=path_category, tissue_sample_id=tissue_sample_id, sex=sex, sort_by=sort_by, sort_direction=sort_direction, search_term=search_term, sample_id=sample_id, subject_id=subject_id, age_bracket=age_bracket, hardy_scale=hardy_scale, has_expression_data=has_expression_data, has_genotype=has_genotype)

Download

### Example


```python
import gtex_openapi
from gtex_openapi.models.app_models_request_parameters_hardy_scale import AppModelsRequestParametersHardyScale
from gtex_openapi.models.app_models_request_parameters_material_type import AppModelsRequestParametersMaterialType
from gtex_openapi.models.biobank_sample import BiobankSample
from gtex_openapi.models.donor_age_bracket import DonorAgeBracket
from gtex_openapi.models.donor_sex import DonorSex
from gtex_openapi.models.path_category import PathCategory
from gtex_openapi.models.tissuesitedetailid_inner import TissuesitedetailidInner
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
    api_instance = gtex_openapi.BiobankDataEndpointsApi(api_client)
    material_type = [gtex_openapi.AppModelsRequestParametersMaterialType()] # List[AppModelsRequestParametersMaterialType] |  (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | Tissues of interest (optional)
    path_category = [gtex_openapi.PathCategory()] # List[PathCategory] | A list of Pathology Category(s) (optional)
    tissue_sample_id = ['tissue_sample_id_example'] # List[str] | A list of Tissue Sample ID(s) (optional)
    sex = gtex_openapi.DonorSex() # DonorSex |  (optional)
    sort_by = gtex_openapi.SortBy() # SortBy |  (optional)
    sort_direction = gtex_openapi.SortDirection() # SortDirection |  (optional)
    search_term = 'search_term_example' # str |  (optional)
    sample_id = ['sample_id_example'] # List[str] | GTEx sample ID (optional)
    subject_id = ['subject_id_example'] # List[str] | GTEx subject ID (optional)
    age_bracket = [gtex_openapi.DonorAgeBracket()] # List[DonorAgeBracket] | The age bracket(s) of the donors of interest (optional)
    hardy_scale = [gtex_openapi.AppModelsRequestParametersHardyScale()] # List[AppModelsRequestParametersHardyScale] | A list of Hardy Scale(s) of interest (optional)
    has_expression_data = True # bool |  (optional)
    has_genotype = True # bool |  (optional)

    try:
        # Download
        api_response = api_instance.download_api_v2_biobank_download_get(material_type=material_type, tissue_site_detail_id=tissue_site_detail_id, path_category=path_category, tissue_sample_id=tissue_sample_id, sex=sex, sort_by=sort_by, sort_direction=sort_direction, search_term=search_term, sample_id=sample_id, subject_id=subject_id, age_bracket=age_bracket, hardy_scale=hardy_scale, has_expression_data=has_expression_data, has_genotype=has_genotype)
        print("The response of BiobankDataEndpointsApi->download_api_v2_biobank_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BiobankDataEndpointsApi->download_api_v2_biobank_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_type** | [**List[AppModelsRequestParametersMaterialType]**](AppModelsRequestParametersMaterialType.md)|  | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| Tissues of interest | [optional] 
 **path_category** | [**List[PathCategory]**](PathCategory.md)| A list of Pathology Category(s) | [optional] 
 **tissue_sample_id** | [**List[str]**](str.md)| A list of Tissue Sample ID(s) | [optional] 
 **sex** | [**DonorSex**](.md)|  | [optional] 
 **sort_by** | [**SortBy**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **search_term** | **str**|  | [optional] 
 **sample_id** | [**List[str]**](str.md)| GTEx sample ID | [optional] 
 **subject_id** | [**List[str]**](str.md)| GTEx subject ID | [optional] 
 **age_bracket** | [**List[DonorAgeBracket]**](DonorAgeBracket.md)| The age bracket(s) of the donors of interest | [optional] 
 **hardy_scale** | [**List[AppModelsRequestParametersHardyScale]**](AppModelsRequestParametersHardyScale.md)| A list of Hardy Scale(s) of interest | [optional] 
 **has_expression_data** | **bool**|  | [optional] 
 **has_genotype** | **bool**|  | [optional] 

### Return type

[**List[BiobankSample]**](BiobankSample.md)

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

# **get_sample_api_v2_biobank_sample_get**
> BiobankResponse get_sample_api_v2_biobank_sample_get(draw=draw, material_type=material_type, tissue_site_detail_id=tissue_site_detail_id, path_category=path_category, tissue_sample_id=tissue_sample_id, sex=sex, sort_by=sort_by, sort_direction=sort_direction, search_term=search_term, sample_id=sample_id, subject_id=subject_id, age_bracket=age_bracket, hardy_scale=hardy_scale, has_expression_data=has_expression_data, has_genotype=has_genotype, page=page, items_per_page=items_per_page)

Get Sample

### Example


```python
import gtex_openapi
from gtex_openapi.models.app_models_request_parameters_hardy_scale import AppModelsRequestParametersHardyScale
from gtex_openapi.models.app_models_request_parameters_material_type import AppModelsRequestParametersMaterialType
from gtex_openapi.models.biobank_response import BiobankResponse
from gtex_openapi.models.donor_age_bracket import DonorAgeBracket
from gtex_openapi.models.donor_sex import DonorSex
from gtex_openapi.models.path_category import PathCategory
from gtex_openapi.models.tissuesitedetailid_inner import TissuesitedetailidInner
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
    api_instance = gtex_openapi.BiobankDataEndpointsApi(api_client)
    draw = 56 # int |  (optional)
    material_type = [gtex_openapi.AppModelsRequestParametersMaterialType()] # List[AppModelsRequestParametersMaterialType] |  (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | Tissues of interest (optional)
    path_category = [gtex_openapi.PathCategory()] # List[PathCategory] | A list of Pathology Category(s) (optional)
    tissue_sample_id = ['tissue_sample_id_example'] # List[str] | A list of Tissue Sample ID(s) (optional)
    sex = gtex_openapi.DonorSex() # DonorSex |  (optional)
    sort_by = gtex_openapi.SortBy() # SortBy |  (optional)
    sort_direction = gtex_openapi.SortDirection() # SortDirection |  (optional)
    search_term = 'search_term_example' # str |  (optional)
    sample_id = ['sample_id_example'] # List[str] | GTEx sample ID (optional)
    subject_id = ['subject_id_example'] # List[str] | GTEx subject ID (optional)
    age_bracket = [gtex_openapi.DonorAgeBracket()] # List[DonorAgeBracket] | The age bracket(s) of the donors of interest (optional)
    hardy_scale = [gtex_openapi.AppModelsRequestParametersHardyScale()] # List[AppModelsRequestParametersHardyScale] | A list of Hardy Scale(s) of interest (optional)
    has_expression_data = True # bool |  (optional)
    has_genotype = True # bool |  (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Sample
        api_response = api_instance.get_sample_api_v2_biobank_sample_get(draw=draw, material_type=material_type, tissue_site_detail_id=tissue_site_detail_id, path_category=path_category, tissue_sample_id=tissue_sample_id, sex=sex, sort_by=sort_by, sort_direction=sort_direction, search_term=search_term, sample_id=sample_id, subject_id=subject_id, age_bracket=age_bracket, hardy_scale=hardy_scale, has_expression_data=has_expression_data, has_genotype=has_genotype, page=page, items_per_page=items_per_page)
        print("The response of BiobankDataEndpointsApi->get_sample_api_v2_biobank_sample_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BiobankDataEndpointsApi->get_sample_api_v2_biobank_sample_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draw** | **int**|  | [optional] 
 **material_type** | [**List[AppModelsRequestParametersMaterialType]**](AppModelsRequestParametersMaterialType.md)|  | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| Tissues of interest | [optional] 
 **path_category** | [**List[PathCategory]**](PathCategory.md)| A list of Pathology Category(s) | [optional] 
 **tissue_sample_id** | [**List[str]**](str.md)| A list of Tissue Sample ID(s) | [optional] 
 **sex** | [**DonorSex**](.md)|  | [optional] 
 **sort_by** | [**SortBy**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **search_term** | **str**|  | [optional] 
 **sample_id** | [**List[str]**](str.md)| GTEx sample ID | [optional] 
 **subject_id** | [**List[str]**](str.md)| GTEx subject ID | [optional] 
 **age_bracket** | [**List[DonorAgeBracket]**](DonorAgeBracket.md)| The age bracket(s) of the donors of interest | [optional] 
 **hardy_scale** | [**List[AppModelsRequestParametersHardyScale]**](AppModelsRequestParametersHardyScale.md)| A list of Hardy Scale(s) of interest | [optional] 
 **has_expression_data** | **bool**|  | [optional] 
 **has_genotype** | **bool**|  | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**BiobankResponse**](BiobankResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Illegal query input |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

