# gtex_openapi.DatasetsEndpointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_annotation_api_v2_dataset_annotation_get**](DatasetsEndpointsApi.md#get_annotation_api_v2_dataset_annotation_get) | **GET** /api/v2/dataset/annotation | Get Annotation
[**get_collapsed_gene_model_exon_api_v2_dataset_collapsed_gene_model_exon_get**](DatasetsEndpointsApi.md#get_collapsed_gene_model_exon_api_v2_dataset_collapsed_gene_model_exon_get) | **GET** /api/v2/dataset/collapsedGeneModelExon | Get Collapsed Gene Model Exon
[**get_downloads_page_data_api_v2_dataset_open_access_files_metadata_get**](DatasetsEndpointsApi.md#get_downloads_page_data_api_v2_dataset_open_access_files_metadata_get) | **GET** /api/v2/dataset/openAccessFilesMetadata | Get Downloads Page Data
[**get_file_list_api_v2_dataset_file_list_get**](DatasetsEndpointsApi.md#get_file_list_api_v2_dataset_file_list_get) | **GET** /api/v2/dataset/fileList | Get File List
[**get_full_get_collapsed_gene_model_exon_api_v2_dataset_full_collapsed_gene_model_exon_get**](DatasetsEndpointsApi.md#get_full_get_collapsed_gene_model_exon_api_v2_dataset_full_collapsed_gene_model_exon_get) | **GET** /api/v2/dataset/fullCollapsedGeneModelExon | Get Full Get Collapsed Gene Model Exon
[**get_functional_annotation_api_v2_dataset_functional_annotation_get**](DatasetsEndpointsApi.md#get_functional_annotation_api_v2_dataset_functional_annotation_get) | **GET** /api/v2/dataset/functionalAnnotation | Get Functional Annotation
[**get_linkage_disequilibrium_by_variant_data_api_v2_dataset_ld_by_variant_get**](DatasetsEndpointsApi.md#get_linkage_disequilibrium_by_variant_data_api_v2_dataset_ld_by_variant_get) | **GET** /api/v2/dataset/ldByVariant | Get Linkage Disequilibrium By Variant Data
[**get_linkage_disequilibrium_data_api_v2_dataset_ld_get**](DatasetsEndpointsApi.md#get_linkage_disequilibrium_data_api_v2_dataset_ld_get) | **GET** /api/v2/dataset/ld | Get Linkage Disequilibrium Data
[**get_sample_api_v2_dataset_sample_get**](DatasetsEndpointsApi.md#get_sample_api_v2_dataset_sample_get) | **GET** /api/v2/dataset/sample | Get Sample
[**get_subject_api_v2_dataset_subject_get**](DatasetsEndpointsApi.md#get_subject_api_v2_dataset_subject_get) | **GET** /api/v2/dataset/subject | Get Subject
[**get_tissue_site_detail_api_v2_dataset_tissue_site_detail_get**](DatasetsEndpointsApi.md#get_tissue_site_detail_api_v2_dataset_tissue_site_detail_get) | **GET** /api/v2/dataset/tissueSiteDetail | Get Tissue Site Detail
[**get_variant_api_v2_dataset_variant_get**](DatasetsEndpointsApi.md#get_variant_api_v2_dataset_variant_get) | **GET** /api/v2/dataset/variant | Get Variant
[**get_variant_by_location_api_v2_dataset_variant_by_location_get**](DatasetsEndpointsApi.md#get_variant_by_location_api_v2_dataset_variant_by_location_get) | **GET** /api/v2/dataset/variantByLocation | Get Variant By Location


# **get_annotation_api_v2_dataset_annotation_get**
> PaginatedResponseAnnotation get_annotation_api_v2_dataset_annotation_get(dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Annotation

This service returns the list of annotations and allowed values by which a particular dataset can be subsetted.
Results may be filtered by dataset.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_annotation import PaginatedResponseAnnotation
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Annotation
        api_response = api_instance.get_annotation_api_v2_dataset_annotation_get(dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of DatasetsEndpointsApi->get_annotation_api_v2_dataset_annotation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_annotation_api_v2_dataset_annotation_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseAnnotation**](PaginatedResponseAnnotation.md)

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

# **get_collapsed_gene_model_exon_api_v2_dataset_collapsed_gene_model_exon_get**
> PaginatedResponseCollapsedGeneModelExon get_collapsed_gene_model_exon_api_v2_dataset_collapsed_gene_model_exon_get(gencode_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Collapsed Gene Model Exon

This service returns the collapsed exons in the gene model of the given gene. Gene-level and exon-level expression
quantification were based on the GENCODE annotation, collapsed to a single transcript model for each gene using an
algorithm developed by the GTEx analysis team.

By default, this service queries the models used by the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_collapsed_gene_model_exon import PaginatedResponseCollapsedGeneModelExon
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    gencode_id = 'gencode_id_example' # str | A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Collapsed Gene Model Exon
        api_response = api_instance.get_collapsed_gene_model_exon_api_v2_dataset_collapsed_gene_model_exon_get(gencode_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of DatasetsEndpointsApi->get_collapsed_gene_model_exon_api_v2_dataset_collapsed_gene_model_exon_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_collapsed_gene_model_exon_api_v2_dataset_collapsed_gene_model_exon_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | **str**| A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseCollapsedGeneModelExon**](PaginatedResponseCollapsedGeneModelExon.md)

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

# **get_downloads_page_data_api_v2_dataset_open_access_files_metadata_get**
> OpenAccessFilesMetadata get_downloads_page_data_api_v2_dataset_open_access_files_metadata_get(project_id)

Get Downloads Page Data

Retrieves all the files belonging to the given `project_id` for display on the `Downloads Page`

### Example


```python
import gtex_openapi
from gtex_openapi.models.available_projects import AvailableProjects
from gtex_openapi.models.open_access_files_metadata import OpenAccessFilesMetadata
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    project_id = gtex_openapi.AvailableProjects() # AvailableProjects | 

    try:
        # Get Downloads Page Data
        api_response = api_instance.get_downloads_page_data_api_v2_dataset_open_access_files_metadata_get(project_id)
        print("The response of DatasetsEndpointsApi->get_downloads_page_data_api_v2_dataset_open_access_files_metadata_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_downloads_page_data_api_v2_dataset_open_access_files_metadata_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**AvailableProjects**](.md)|  | 

### Return type

[**OpenAccessFilesMetadata**](OpenAccessFilesMetadata.md)

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

# **get_file_list_api_v2_dataset_file_list_get**
> List[File] get_file_list_api_v2_dataset_file_list_get()

Get File List

Get all the files in GTEx dataset for Download page

### Example


```python
import gtex_openapi
from gtex_openapi.models.file import File
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)

    try:
        # Get File List
        api_response = api_instance.get_file_list_api_v2_dataset_file_list_get()
        print("The response of DatasetsEndpointsApi->get_file_list_api_v2_dataset_file_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_file_list_api_v2_dataset_file_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[File]**](File.md)

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

# **get_full_get_collapsed_gene_model_exon_api_v2_dataset_full_collapsed_gene_model_exon_get**
> PaginatedResponseCollapsedGeneModelExon get_full_get_collapsed_gene_model_exon_api_v2_dataset_full_collapsed_gene_model_exon_get(gencode_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Full Get Collapsed Gene Model Exon

This service allows the user to query the full Collapsed Gene Model Exon of a specific gene by gencode ID

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_collapsed_gene_model_exon import PaginatedResponseCollapsedGeneModelExon
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    gencode_id = 'gencode_id_example' # str | A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Full Get Collapsed Gene Model Exon
        api_response = api_instance.get_full_get_collapsed_gene_model_exon_api_v2_dataset_full_collapsed_gene_model_exon_get(gencode_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of DatasetsEndpointsApi->get_full_get_collapsed_gene_model_exon_api_v2_dataset_full_collapsed_gene_model_exon_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_full_get_collapsed_gene_model_exon_api_v2_dataset_full_collapsed_gene_model_exon_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | **str**| A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseCollapsedGeneModelExon**](PaginatedResponseCollapsedGeneModelExon.md)

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

# **get_functional_annotation_api_v2_dataset_functional_annotation_get**
> PaginatedResponseFunctionalAnnotation get_functional_annotation_api_v2_dataset_functional_annotation_get(chromosome, start, end, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Functional Annotation

This endpoint retrieves the functional annotation of a certain chromosome location. Default to most recent dataset
release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.chromosome import Chromosome
from gtex_openapi.models.paginated_response_functional_annotation import PaginatedResponseFunctionalAnnotation
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    chromosome = gtex_openapi.Chromosome() # Chromosome | 
    start = 56 # int | 
    end = 56 # int | 
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Functional Annotation
        api_response = api_instance.get_functional_annotation_api_v2_dataset_functional_annotation_get(chromosome, start, end, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of DatasetsEndpointsApi->get_functional_annotation_api_v2_dataset_functional_annotation_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_functional_annotation_api_v2_dataset_functional_annotation_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chromosome** | [**Chromosome**](.md)|  | 
 **start** | **int**|  | 
 **end** | **int**|  | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseFunctionalAnnotation**](PaginatedResponseFunctionalAnnotation.md)

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

# **get_linkage_disequilibrium_by_variant_data_api_v2_dataset_ld_by_variant_get**
> PaginatedResponseListUnionStrFloat get_linkage_disequilibrium_by_variant_data_api_v2_dataset_ld_by_variant_get(variant_id=variant_id, page=page, items_per_page=items_per_page)

Get Linkage Disequilibrium By Variant Data

Find linkage disequilibrium (LD) data for a given variant

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_list_union_str_float import PaginatedResponseListUnionStrFloat
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    variant_id = 'variant_id_example' # str | A gtex variant ID (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Linkage Disequilibrium By Variant Data
        api_response = api_instance.get_linkage_disequilibrium_by_variant_data_api_v2_dataset_ld_by_variant_get(variant_id=variant_id, page=page, items_per_page=items_per_page)
        print("The response of DatasetsEndpointsApi->get_linkage_disequilibrium_by_variant_data_api_v2_dataset_ld_by_variant_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_linkage_disequilibrium_by_variant_data_api_v2_dataset_ld_by_variant_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variant_id** | **str**| A gtex variant ID | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseListUnionStrFloat**](PaginatedResponseListUnionStrFloat.md)

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

# **get_linkage_disequilibrium_data_api_v2_dataset_ld_get**
> PaginatedResponseListUnionStrFloat get_linkage_disequilibrium_data_api_v2_dataset_ld_get(gencode_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Linkage Disequilibrium Data

Find linkage disequilibrium (LD) data for a given gene.

This endpoint returns linkage disequilibrium data for the cis-eQTLs found associated with the provided
gene in a specified dataset. Results are queried by gencode ID.
By default, the service queries the latest GTEx release.
Specify a dataset ID to fetch results from a different dataset.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_list_union_str_float import PaginatedResponseListUnionStrFloat
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    gencode_id = 'gencode_id_example' # str | A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Linkage Disequilibrium Data
        api_response = api_instance.get_linkage_disequilibrium_data_api_v2_dataset_ld_get(gencode_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of DatasetsEndpointsApi->get_linkage_disequilibrium_data_api_v2_dataset_ld_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_linkage_disequilibrium_data_api_v2_dataset_ld_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | **str**| A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseListUnionStrFloat**](PaginatedResponseListUnionStrFloat.md)

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

# **get_sample_api_v2_dataset_sample_get**
> PaginatedResponseDatasetSample get_sample_api_v2_dataset_sample_get(dataset_id=dataset_id, sample_id=sample_id, tissue_sample_id=tissue_sample_id, subject_id=subject_id, age_bracket=age_bracket, sex=sex, path_category=path_category, tissue_site_detail_id=tissue_site_detail_id, aliquot_id=aliquot_id, autolysis_score=autolysis_score, hardy_scale=hardy_scale, ischemic_time=ischemic_time, ischemic_time_group=ischemic_time_group, rin=rin, uberon_id=uberon_id, data_type=data_type, sort_by=sort_by, sort_direction=sort_direction, page=page, items_per_page=items_per_page)

Get Sample

This service returns information of samples used in analyses from all datasets.
Results may be filtered by dataset ID, sample ID, subject ID, sample metadata, or other provided parameters.
By default, this service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.app_models_request_parameters_hardy_scale import AppModelsRequestParametersHardyScale
from gtex_openapi.models.autolysis_score import AutolysisScore
from gtex_openapi.models.data_type import DataType
from gtex_openapi.models.donor_age_bracket import DonorAgeBracket
from gtex_openapi.models.donor_sex import DonorSex
from gtex_openapi.models.ischemic_time_group import IschemicTimeGroup
from gtex_openapi.models.paginated_response_dataset_sample import PaginatedResponseDatasetSample
from gtex_openapi.models.path_category import PathCategory
from gtex_openapi.models.tissue_site_detail_id import TissueSiteDetailId
from gtex_openapi.models.tissue_site_ontology_id import TissueSiteOntologyId
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    sample_id = ['sample_id_example'] # List[str] | GTEx sample ID (optional)
    tissue_sample_id = ['tissue_sample_id_example'] # List[str] | A list of Tissue Sample ID(s) (optional)
    subject_id = ['subject_id_example'] # List[str] | GTEx subject ID (optional)
    age_bracket = [gtex_openapi.DonorAgeBracket()] # List[DonorAgeBracket] | The age bracket(s) of the donors of interest (optional)
    sex = gtex_openapi.DonorSex() # DonorSex |  (optional)
    path_category = [gtex_openapi.PathCategory()] # List[PathCategory] | A list of Pathology Category(s) (optional)
    tissue_site_detail_id = [gtex_openapi.TissueSiteDetailId()] # List[TissueSiteDetailId] | Tissues of interest (optional)
    aliquot_id = ['aliquot_id_example'] # List[str] |  (optional)
    autolysis_score = [gtex_openapi.AutolysisScore()] # List[AutolysisScore] |  (optional)
    hardy_scale = [gtex_openapi.AppModelsRequestParametersHardyScale()] # List[AppModelsRequestParametersHardyScale] | A list of Hardy Scale(s) of interest (optional)
    ischemic_time = [56] # List[int] | Ischemic Time for the sample of interest (optional)
    ischemic_time_group = [gtex_openapi.IschemicTimeGroup()] # List[IschemicTimeGroup] |  (optional)
    rin = [3.4] # List[float] |  (optional)
    uberon_id = [gtex_openapi.TissueSiteOntologyId()] # List[TissueSiteOntologyId] | A list of Uberon ID(s) of interest. (optional)
    data_type = [gtex_openapi.DataType()] # List[DataType] |  (optional)
    sort_by = gtex_openapi.SampleSortBy() # SampleSortBy |  (optional)
    sort_direction = gtex_openapi.SortDirection() # SortDirection |  (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Sample
        api_response = api_instance.get_sample_api_v2_dataset_sample_get(dataset_id=dataset_id, sample_id=sample_id, tissue_sample_id=tissue_sample_id, subject_id=subject_id, age_bracket=age_bracket, sex=sex, path_category=path_category, tissue_site_detail_id=tissue_site_detail_id, aliquot_id=aliquot_id, autolysis_score=autolysis_score, hardy_scale=hardy_scale, ischemic_time=ischemic_time, ischemic_time_group=ischemic_time_group, rin=rin, uberon_id=uberon_id, data_type=data_type, sort_by=sort_by, sort_direction=sort_direction, page=page, items_per_page=items_per_page)
        print("The response of DatasetsEndpointsApi->get_sample_api_v2_dataset_sample_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_sample_api_v2_dataset_sample_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **sample_id** | [**List[str]**](str.md)| GTEx sample ID | [optional] 
 **tissue_sample_id** | [**List[str]**](str.md)| A list of Tissue Sample ID(s) | [optional] 
 **subject_id** | [**List[str]**](str.md)| GTEx subject ID | [optional] 
 **age_bracket** | [**List[DonorAgeBracket]**](DonorAgeBracket.md)| The age bracket(s) of the donors of interest | [optional] 
 **sex** | [**DonorSex**](.md)|  | [optional] 
 **path_category** | [**List[PathCategory]**](PathCategory.md)| A list of Pathology Category(s) | [optional] 
 **tissue_site_detail_id** | [**List[TissueSiteDetailId]**](TissueSiteDetailId.md)| Tissues of interest | [optional] 
 **aliquot_id** | [**List[str]**](str.md)|  | [optional] 
 **autolysis_score** | [**List[AutolysisScore]**](AutolysisScore.md)|  | [optional] 
 **hardy_scale** | [**List[AppModelsRequestParametersHardyScale]**](AppModelsRequestParametersHardyScale.md)| A list of Hardy Scale(s) of interest | [optional] 
 **ischemic_time** | [**List[int]**](int.md)| Ischemic Time for the sample of interest | [optional] 
 **ischemic_time_group** | [**List[IschemicTimeGroup]**](IschemicTimeGroup.md)|  | [optional] 
 **rin** | [**List[float]**](float.md)|  | [optional] 
 **uberon_id** | [**List[TissueSiteOntologyId]**](TissueSiteOntologyId.md)| A list of Uberon ID(s) of interest. | [optional] 
 **data_type** | [**List[DataType]**](DataType.md)|  | [optional] 
 **sort_by** | [**SampleSortBy**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseDatasetSample**](PaginatedResponseDatasetSample.md)

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

# **get_subject_api_v2_dataset_subject_get**
> PaginatedResponseSubject get_subject_api_v2_dataset_subject_get(dataset_id=dataset_id, sex=sex, age_bracket=age_bracket, hardy_scale=hardy_scale, subject_id=subject_id, page=page, items_per_page=items_per_page)

Get Subject

This service returns information of subjects used in analyses from all datasets.
Results may be filtered by dataset ID, subject ID, sex, age bracket or Hardy Scale.
By default, this service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.donor_age_bracket import DonorAgeBracket
from gtex_openapi.models.donor_sex import DonorSex
from gtex_openapi.models.paginated_response_subject import PaginatedResponseSubject
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    sex = gtex_openapi.DonorSex() # DonorSex |  (optional)
    age_bracket = [gtex_openapi.DonorAgeBracket()] # List[DonorAgeBracket] | The age bracket(s) of the donors of interest (optional)
    hardy_scale = gtex_openapi.AppModelsRequestParametersHardyScale() # AppModelsRequestParametersHardyScale | The hardy scale of interest (optional)
    subject_id = ['subject_id_example'] # List[str] | GTEx subject ID (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Subject
        api_response = api_instance.get_subject_api_v2_dataset_subject_get(dataset_id=dataset_id, sex=sex, age_bracket=age_bracket, hardy_scale=hardy_scale, subject_id=subject_id, page=page, items_per_page=items_per_page)
        print("The response of DatasetsEndpointsApi->get_subject_api_v2_dataset_subject_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_subject_api_v2_dataset_subject_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **sex** | [**DonorSex**](.md)|  | [optional] 
 **age_bracket** | [**List[DonorAgeBracket]**](DonorAgeBracket.md)| The age bracket(s) of the donors of interest | [optional] 
 **hardy_scale** | [**AppModelsRequestParametersHardyScale**](.md)| The hardy scale of interest | [optional] 
 **subject_id** | [**List[str]**](str.md)| GTEx subject ID | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseSubject**](PaginatedResponseSubject.md)

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

# **get_tissue_site_detail_api_v2_dataset_tissue_site_detail_get**
> PaginatedResponseTissueSiteDetail get_tissue_site_detail_api_v2_dataset_tissue_site_detail_get(dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Tissue Site Detail

Retrieve all tissue site detail information in the database

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_tissue_site_detail import PaginatedResponseTissueSiteDetail
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Tissue Site Detail
        api_response = api_instance.get_tissue_site_detail_api_v2_dataset_tissue_site_detail_get(dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of DatasetsEndpointsApi->get_tissue_site_detail_api_v2_dataset_tissue_site_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_tissue_site_detail_api_v2_dataset_tissue_site_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseTissueSiteDetail**](PaginatedResponseTissueSiteDetail.md)

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

# **get_variant_api_v2_dataset_variant_get**
> PaginatedResponseVariant get_variant_api_v2_dataset_variant_get(snp_id=snp_id, variant_id=variant_id, dataset_id=dataset_id, chromosome=chromosome, pos=pos, page=page, items_per_page=items_per_page)

Get Variant

This service returns information about a variant, including position, dbSNP RS ID, the reference allele,
the alternative allele, and whether the minor allele frequency is >= 1%.
For GTEx v6p, there is also information about whether the whole exome sequence and chip sequencing data are
available. Results may be queried by GTEx variant ID (variantId), dbSNP RS ID (snpId) or genomic location
(chromosome and pos). Variants are identified based on the genotype data of each dataset cohort, namely,
are dataset-dependent. Each variant is assigned a unique GTEx variant ID (i.e. the primary key).
Not all variants have a mappable dbSNP RS ID. By default, this service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.chromosome import Chromosome
from gtex_openapi.models.paginated_response_variant import PaginatedResponseVariant
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    snp_id = 'snp_id_example' # str | A Snp ID (optional)
    variant_id = 'variant_id_example' # str | A gtex variant ID (optional)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    chromosome = gtex_openapi.Chromosome() # Chromosome |  (optional)
    pos = [56] # List[int] |  (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Variant
        api_response = api_instance.get_variant_api_v2_dataset_variant_get(snp_id=snp_id, variant_id=variant_id, dataset_id=dataset_id, chromosome=chromosome, pos=pos, page=page, items_per_page=items_per_page)
        print("The response of DatasetsEndpointsApi->get_variant_api_v2_dataset_variant_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_variant_api_v2_dataset_variant_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snp_id** | **str**| A Snp ID | [optional] 
 **variant_id** | **str**| A gtex variant ID | [optional] 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **chromosome** | [**Chromosome**](.md)|  | [optional] 
 **pos** | [**List[int]**](int.md)|  | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseVariant**](PaginatedResponseVariant.md)

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

# **get_variant_by_location_api_v2_dataset_variant_by_location_get**
> PaginatedResponseVariant get_variant_by_location_api_v2_dataset_variant_by_location_get(start, end, chromosome, sort_by=sort_by, sort_direction=sort_direction, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Variant By Location

This service allows the user to query information about variants on a certain chromosome at a certain location

### Example


```python
import gtex_openapi
from gtex_openapi.models.chromosome import Chromosome
from gtex_openapi.models.paginated_response_variant import PaginatedResponseVariant
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
    api_instance = gtex_openapi.DatasetsEndpointsApi(api_client)
    start = 56 # int | 
    end = 56 # int | 
    chromosome = gtex_openapi.Chromosome() # Chromosome | 
    sort_by = gtex_openapi.VariantSortBy() # VariantSortBy |  (optional)
    sort_direction = gtex_openapi.SortDirection() # SortDirection |  (optional)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Variant By Location
        api_response = api_instance.get_variant_by_location_api_v2_dataset_variant_by_location_get(start, end, chromosome, sort_by=sort_by, sort_direction=sort_direction, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of DatasetsEndpointsApi->get_variant_by_location_api_v2_dataset_variant_by_location_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsEndpointsApi->get_variant_by_location_api_v2_dataset_variant_by_location_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**|  | 
 **end** | **int**|  | 
 **chromosome** | [**Chromosome**](.md)|  | 
 **sort_by** | [**VariantSortBy**](.md)|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseVariant**](PaginatedResponseVariant.md)

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

