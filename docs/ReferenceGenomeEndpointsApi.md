# gtex_openapi.ReferenceGenomeEndpointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exons_api_v2_reference_exon_get**](ReferenceGenomeEndpointsApi.md#get_exons_api_v2_reference_exon_get) | **GET** /api/v2/reference/exon | Get Exons
[**get_gene_search_api_v2_reference_gene_search_get**](ReferenceGenomeEndpointsApi.md#get_gene_search_api_v2_reference_gene_search_get) | **GET** /api/v2/reference/geneSearch | Get Gene Search
[**get_genes_api_v2_reference_gene_get**](ReferenceGenomeEndpointsApi.md#get_genes_api_v2_reference_gene_get) | **GET** /api/v2/reference/gene | Get Genes
[**get_genomic_features_api_v2_reference_features_feature_id_get**](ReferenceGenomeEndpointsApi.md#get_genomic_features_api_v2_reference_features_feature_id_get) | **GET** /api/v2/reference/features/{featureId} | Get Genomic Features
[**get_gwas_catalog_by_location_api_v2_reference_gwas_catalog_by_location_get**](ReferenceGenomeEndpointsApi.md#get_gwas_catalog_by_location_api_v2_reference_gwas_catalog_by_location_get) | **GET** /api/v2/reference/gwasCatalogByLocation | Get Gwas Catalog By Location
[**get_neighbor_gene_api_v2_reference_neighbor_gene_get**](ReferenceGenomeEndpointsApi.md#get_neighbor_gene_api_v2_reference_neighbor_gene_get) | **GET** /api/v2/reference/neighborGene | Get Neighbor Gene
[**get_transcripts_api_v2_reference_transcript_get**](ReferenceGenomeEndpointsApi.md#get_transcripts_api_v2_reference_transcript_get) | **GET** /api/v2/reference/transcript | Get Transcripts


# **get_exons_api_v2_reference_exon_get**
> PaginatedResponseExon get_exons_api_v2_reference_exon_get(gencode_id, gencode_version=gencode_version, genome_build=genome_build, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Exons

This service returns exons from all known transcripts of the given gene.
 - A versioned GENCODE ID is required to ensure that all exons are from a single gene.
 - A dataset ID or both GENCODE version and genome build must be provided.
 - Although annotated exons are not dataset dependent,
specifying a dataset here is equivalent to specifying the GENCODE version and genome build used by that dataset.

### Example


```python
import gtex_openapi
from gtex_openapi.models.app_models_request_parameters_genome_build import AppModelsRequestParametersGenomeBuild
from gtex_openapi.models.dataset_id import DatasetId
from gtex_openapi.models.paginated_response_exon import PaginatedResponseExon
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
    api_instance = gtex_openapi.ReferenceGenomeEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    gencode_version = gtex_openapi.AppModelsRequestParametersGencodeVersion() # AppModelsRequestParametersGencodeVersion | GENCODE annotation release. (optional)
    genome_build = gtex_openapi.AppModelsRequestParametersGenomeBuild() # AppModelsRequestParametersGenomeBuild |  (optional)
    dataset_id = gtex_openapi.DatasetId() # DatasetId |  (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Exons
        api_response = api_instance.get_exons_api_v2_reference_exon_get(gencode_id, gencode_version=gencode_version, genome_build=genome_build, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of ReferenceGenomeEndpointsApi->get_exons_api_v2_reference_exon_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceGenomeEndpointsApi->get_exons_api_v2_reference_exon_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **gencode_version** | [**AppModelsRequestParametersGencodeVersion**](.md)| GENCODE annotation release. | [optional] 
 **genome_build** | [**AppModelsRequestParametersGenomeBuild**](.md)|  | [optional] 
 **dataset_id** | [**DatasetId**](.md)|  | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseExon**](PaginatedResponseExon.md)

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

# **get_gene_search_api_v2_reference_gene_search_get**
> PaginatedResponseGene get_gene_search_api_v2_reference_gene_search_get(gene_id, gencode_version=gencode_version, genome_build=genome_build, page=page, items_per_page=items_per_page)

Get Gene Search

Find genes that are partial or complete match of a gene_id
 - gene_id could be a gene symbol, a gencode ID, or an Ensemble ID
 - Gencode Version and Genome Build must be specified

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_gene import PaginatedResponseGene
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
    api_instance = gtex_openapi.ReferenceGenomeEndpointsApi(api_client)
    gene_id = 'gene_id_example' # str | 
    gencode_version = gtex_openapi.AppModelsRequestParametersGencodeVersion() # AppModelsRequestParametersGencodeVersion | GENCODE annotation release. (optional)
    genome_build = gtex_openapi.AppModelsRequestParametersGenomeBuild() # AppModelsRequestParametersGenomeBuild |  (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Gene Search
        api_response = api_instance.get_gene_search_api_v2_reference_gene_search_get(gene_id, gencode_version=gencode_version, genome_build=genome_build, page=page, items_per_page=items_per_page)
        print("The response of ReferenceGenomeEndpointsApi->get_gene_search_api_v2_reference_gene_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceGenomeEndpointsApi->get_gene_search_api_v2_reference_gene_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | **str**|  | 
 **gencode_version** | [**AppModelsRequestParametersGencodeVersion**](.md)| GENCODE annotation release. | [optional] 
 **genome_build** | [**AppModelsRequestParametersGenomeBuild**](.md)|  | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseGene**](PaginatedResponseGene.md)

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

# **get_genes_api_v2_reference_gene_get**
> PaginatedResponseGene get_genes_api_v2_reference_gene_get(gene_id, gencode_version=gencode_version, genome_build=genome_build, page=page, items_per_page=items_per_page)

Get Genes

This service returns information about reference genes. A genome build and GENCODE version must be provided.
 - Genes are searchable by gene symbol, GENCODE ID and versioned GENCODE ID.
 - Versioned GENCODE ID is recommended to ensure unique ID matching.
 - By default, this service queries the genome build and GENCODE version used by the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_gene import PaginatedResponseGene
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
    api_instance = gtex_openapi.ReferenceGenomeEndpointsApi(api_client)
    gene_id = ['gene_id_example'] # List[str] | A gene symbol, versioned gencodeId, or unversioned gencodeId.
    gencode_version = gtex_openapi.AppModelsRequestParametersGencodeVersion() # AppModelsRequestParametersGencodeVersion | GENCODE annotation release. (optional)
    genome_build = gtex_openapi.AppModelsRequestParametersGenomeBuild() # AppModelsRequestParametersGenomeBuild |  (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Genes
        api_response = api_instance.get_genes_api_v2_reference_gene_get(gene_id, gencode_version=gencode_version, genome_build=genome_build, page=page, items_per_page=items_per_page)
        print("The response of ReferenceGenomeEndpointsApi->get_genes_api_v2_reference_gene_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceGenomeEndpointsApi->get_genes_api_v2_reference_gene_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gene_id** | [**List[str]**](str.md)| A gene symbol, versioned gencodeId, or unversioned gencodeId. | 
 **gencode_version** | [**AppModelsRequestParametersGencodeVersion**](.md)| GENCODE annotation release. | [optional] 
 **genome_build** | [**AppModelsRequestParametersGenomeBuild**](.md)|  | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseGene**](PaginatedResponseGene.md)

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

# **get_genomic_features_api_v2_reference_features_feature_id_get**
> Feature get_genomic_features_api_v2_reference_features_feature_id_get(feature_id, dataset_id=dataset_id)

Get Genomic Features

### Example


```python
import gtex_openapi
from gtex_openapi.models.feature import Feature
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
    api_instance = gtex_openapi.ReferenceGenomeEndpointsApi(api_client)
    feature_id = 'feature_id_example' # str | 
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)

    try:
        # Get Genomic Features
        api_response = api_instance.get_genomic_features_api_v2_reference_features_feature_id_get(feature_id, dataset_id=dataset_id)
        print("The response of ReferenceGenomeEndpointsApi->get_genomic_features_api_v2_reference_features_feature_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceGenomeEndpointsApi->get_genomic_features_api_v2_reference_features_feature_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**|  | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 

### Return type

[**Feature**](Feature.md)

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

# **get_gwas_catalog_by_location_api_v2_reference_gwas_catalog_by_location_get**
> PaginatedResponseGWAS get_gwas_catalog_by_location_api_v2_reference_gwas_catalog_by_location_get(start, end, chromosome, page=page, items_per_page=items_per_page)

Get Gwas Catalog By Location

Find the GWAS Catalog on a certain chromosome between start and end locations.

### Example


```python
import gtex_openapi
from gtex_openapi.models.chromosome import Chromosome
from gtex_openapi.models.paginated_response_gwas import PaginatedResponseGWAS
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
    api_instance = gtex_openapi.ReferenceGenomeEndpointsApi(api_client)
    start = 56 # int | 
    end = 56 # int | 
    chromosome = gtex_openapi.Chromosome() # Chromosome | 
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Gwas Catalog By Location
        api_response = api_instance.get_gwas_catalog_by_location_api_v2_reference_gwas_catalog_by_location_get(start, end, chromosome, page=page, items_per_page=items_per_page)
        print("The response of ReferenceGenomeEndpointsApi->get_gwas_catalog_by_location_api_v2_reference_gwas_catalog_by_location_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceGenomeEndpointsApi->get_gwas_catalog_by_location_api_v2_reference_gwas_catalog_by_location_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**|  | 
 **end** | **int**|  | 
 **chromosome** | [**Chromosome**](.md)|  | 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseGWAS**](PaginatedResponseGWAS.md)

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

# **get_neighbor_gene_api_v2_reference_neighbor_gene_get**
> PaginatedResponseGene get_neighbor_gene_api_v2_reference_neighbor_gene_get(pos, chromosome, bp_window, page=page, gencode_version=gencode_version, genome_build=genome_build, items_per_page=items_per_page)

Get Neighbor Gene

Find all neighboring genes on a certain chromosome around a position with a certain window size.

### Example


```python
import gtex_openapi
from gtex_openapi.models.chromosome import Chromosome
from gtex_openapi.models.paginated_response_gene import PaginatedResponseGene
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
    api_instance = gtex_openapi.ReferenceGenomeEndpointsApi(api_client)
    pos = 56 # int | 
    chromosome = gtex_openapi.Chromosome() # Chromosome | 
    bp_window = 56 # int | 
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    gencode_version = gtex_openapi.AppModelsRequestParametersGencodeVersion() # AppModelsRequestParametersGencodeVersion | GENCODE annotation release. (optional)
    genome_build = gtex_openapi.AppModelsRequestParametersGenomeBuild() # AppModelsRequestParametersGenomeBuild |  (optional)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Neighbor Gene
        api_response = api_instance.get_neighbor_gene_api_v2_reference_neighbor_gene_get(pos, chromosome, bp_window, page=page, gencode_version=gencode_version, genome_build=genome_build, items_per_page=items_per_page)
        print("The response of ReferenceGenomeEndpointsApi->get_neighbor_gene_api_v2_reference_neighbor_gene_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceGenomeEndpointsApi->get_neighbor_gene_api_v2_reference_neighbor_gene_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pos** | **int**|  | 
 **chromosome** | [**Chromosome**](.md)|  | 
 **bp_window** | **int**|  | 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **gencode_version** | [**AppModelsRequestParametersGencodeVersion**](.md)| GENCODE annotation release. | [optional] 
 **genome_build** | [**AppModelsRequestParametersGenomeBuild**](.md)|  | [optional] 
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseGene**](PaginatedResponseGene.md)

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

# **get_transcripts_api_v2_reference_transcript_get**
> PaginatedResponseTranscript get_transcripts_api_v2_reference_transcript_get(gencode_id, gencode_version=gencode_version, genome_build=genome_build, page=page, items_per_page=items_per_page)

Get Transcripts

Find all transcripts of a reference gene.

- This service returns information about transcripts of the given versioned GENCODE ID.
- A genome build and GENCODE version must be provided.
- By default, this service queries the genome build and GENCODE version used by the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_transcript import PaginatedResponseTranscript
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
    api_instance = gtex_openapi.ReferenceGenomeEndpointsApi(api_client)
    gencode_id = 'gencode_id_example' # str | A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9
    gencode_version = gtex_openapi.AppModelsRequestParametersGencodeVersion() # AppModelsRequestParametersGencodeVersion | GENCODE annotation release. (optional)
    genome_build = gtex_openapi.AppModelsRequestParametersGenomeBuild() # AppModelsRequestParametersGenomeBuild |  (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Transcripts
        api_response = api_instance.get_transcripts_api_v2_reference_transcript_get(gencode_id, gencode_version=gencode_version, genome_build=genome_build, page=page, items_per_page=items_per_page)
        print("The response of ReferenceGenomeEndpointsApi->get_transcripts_api_v2_reference_transcript_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceGenomeEndpointsApi->get_transcripts_api_v2_reference_transcript_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | **str**| A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9 | 
 **gencode_version** | [**AppModelsRequestParametersGencodeVersion**](.md)| GENCODE annotation release. | [optional] 
 **genome_build** | [**AppModelsRequestParametersGenomeBuild**](.md)|  | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseTranscript**](PaginatedResponseTranscript.md)

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

