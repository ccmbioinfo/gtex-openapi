# gtex_openapi.StaticAssociationEndpointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_eqtl_genes_api_v2_association_egene_get**](StaticAssociationEndpointsApi.md#get_eqtl_genes_api_v2_association_egene_get) | **GET** /api/v2/association/egene | Get Eqtl Genes
[**get_fine_mapping_api_v2_association_fine_mapping_get**](StaticAssociationEndpointsApi.md#get_fine_mapping_api_v2_association_fine_mapping_get) | **GET** /api/v2/association/fineMapping | Get Fine Mapping
[**get_independent_eqtl_api_v2_association_independent_eqtl_get**](StaticAssociationEndpointsApi.md#get_independent_eqtl_api_v2_association_independent_eqtl_get) | **GET** /api/v2/association/independentEqtl | Get Independent Eqtl
[**get_multi_tissue_eqtls_api_v2_association_metasoft_get**](StaticAssociationEndpointsApi.md#get_multi_tissue_eqtls_api_v2_association_metasoft_get) | **GET** /api/v2/association/metasoft | Get Multi Tissue Eqtls
[**get_significant_single_tissue_eqtls_api_v2_association_single_tissue_eqtl_get**](StaticAssociationEndpointsApi.md#get_significant_single_tissue_eqtls_api_v2_association_single_tissue_eqtl_get) | **GET** /api/v2/association/singleTissueEqtl | Get Significant Single Tissue Eqtls
[**get_significant_single_tissue_eqtls_by_location_api_v2_association_single_tissue_eqtl_by_location_get**](StaticAssociationEndpointsApi.md#get_significant_single_tissue_eqtls_by_location_api_v2_association_single_tissue_eqtl_by_location_get) | **GET** /api/v2/association/singleTissueEqtlByLocation | Get Significant Single Tissue Eqtls By Location
[**get_significant_single_tissue_ieqtls_api_v2_association_single_tissue_i_eqtl_get**](StaticAssociationEndpointsApi.md#get_significant_single_tissue_ieqtls_api_v2_association_single_tissue_i_eqtl_get) | **GET** /api/v2/association/singleTissueIEqtl | Get Significant Single Tissue Ieqtls
[**get_significant_single_tissue_isqtls_api_v2_association_single_tissue_i_sqtl_get**](StaticAssociationEndpointsApi.md#get_significant_single_tissue_isqtls_api_v2_association_single_tissue_i_sqtl_get) | **GET** /api/v2/association/singleTissueISqtl | Get Significant Single Tissue Isqtls
[**get_significant_single_tissue_sqtls_api_v2_association_single_tissue_sqtl_get**](StaticAssociationEndpointsApi.md#get_significant_single_tissue_sqtls_api_v2_association_single_tissue_sqtl_get) | **GET** /api/v2/association/singleTissueSqtl | Get Significant Single Tissue Sqtls
[**get_sqtl_genes_api_v2_association_sgene_get**](StaticAssociationEndpointsApi.md#get_sqtl_genes_api_v2_association_sgene_get) | **GET** /api/v2/association/sgene | Get Sqtl Genes


# **get_eqtl_genes_api_v2_association_egene_get**
> PaginatedResponseEqtlGene get_eqtl_genes_api_v2_association_egene_get(tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Eqtl Genes

Retrieve eGenes (eQTL Genes).

- This service returns eGenes (eQTL Genes) from the specified dataset.
- eGenes are genes that have at least one significant cis-eQTL acting upon them.
- Results may be filtered by tissue. By default, the service queries the latest GTEx release.

For each eGene, the results include the allelic fold change (log2AllelicFoldChange), p-value (pValue),
p-value threshold (pValueThreshold), empirical p-value (empiricalPValue), and q-value (qValue).

- The log2AllelicFoldChange is the allelic fold change (in log2 scale) of the most significant eQTL.
- The pValue is the nominal p-value of the most significant eQTL.
- The pValueThreshold is the p-value threshold used to determine whether a cis-eQTL for this gene is  significant.
For more details see https://gtexportal.org/home/documentationPage#staticTextAnalysisMethods.
- The empiricalPValue is the beta distribution-adjusted empirical p-value from FastQTL.
- The qValues were calculated based on the empirical p-values. A false discovery rate (FDR) threshold of <= 0.05
was applied to identify genes with a significant eQTL.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_eqtl_gene import PaginatedResponseEqtlGene
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
    api_instance = gtex_openapi.StaticAssociationEndpointsApi(api_client)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Eqtl Genes
        api_response = api_instance.get_eqtl_genes_api_v2_association_egene_get(tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of StaticAssociationEndpointsApi->get_eqtl_genes_api_v2_association_egene_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticAssociationEndpointsApi->get_eqtl_genes_api_v2_association_egene_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseEqtlGene**](PaginatedResponseEqtlGene.md)

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

# **get_fine_mapping_api_v2_association_fine_mapping_get**
> PaginatedResponseFineMapping get_fine_mapping_api_v2_association_fine_mapping_get(gencode_id, dataset_id=dataset_id, variant_id=variant_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)

Get Fine Mapping

Retrieve Fine Mapping Data

- Finds and returns `Fine Mapping` data for the provided list of genes
- By default, this endpoint fetches data from the latest `GTEx` version

The retrieved data is split into pages with `items_per_page` entries per page

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_fine_mapping import PaginatedResponseFineMapping
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
    api_instance = gtex_openapi.StaticAssociationEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    variant_id = 'variant_id_example' # str | A gtex variant ID (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Fine Mapping
        api_response = api_instance.get_fine_mapping_api_v2_association_fine_mapping_get(gencode_id, dataset_id=dataset_id, variant_id=variant_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)
        print("The response of StaticAssociationEndpointsApi->get_fine_mapping_api_v2_association_fine_mapping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticAssociationEndpointsApi->get_fine_mapping_api_v2_association_fine_mapping_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **variant_id** | **str**| A gtex variant ID | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseFineMapping**](PaginatedResponseFineMapping.md)

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

# **get_independent_eqtl_api_v2_association_independent_eqtl_get**
> PaginatedResponseIndependentEqtl get_independent_eqtl_api_v2_association_independent_eqtl_get(gencode_id, tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Independent Eqtl

Retrieve Independent eQTL Data

- Finds and returns `Independent eQTL Data` data for the provided list of genes
- By default, this endpoint fetches data from the latest `GTEx` version

The retrieved data is split into pages with `items_per_page` entries per page

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_independent_eqtl import PaginatedResponseIndependentEqtl
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
    api_instance = gtex_openapi.StaticAssociationEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Independent Eqtl
        api_response = api_instance.get_independent_eqtl_api_v2_association_independent_eqtl_get(gencode_id, tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of StaticAssociationEndpointsApi->get_independent_eqtl_api_v2_association_independent_eqtl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticAssociationEndpointsApi->get_independent_eqtl_api_v2_association_independent_eqtl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseIndependentEqtl**](PaginatedResponseIndependentEqtl.md)

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

# **get_multi_tissue_eqtls_api_v2_association_metasoft_get**
> PaginatedResponseMetaSoft get_multi_tissue_eqtls_api_v2_association_metasoft_get(gencode_id, variant_id=variant_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Multi Tissue Eqtls

Find multi-tissue eQTL `Metasoft` results.

- This service returns multi-tissue eQTL Metasoft results for a given gene and variant in a specified dataset.
- A Versioned GENCODE ID must be provided.
- For each tissue, the results include: m-value (mValue), normalized effect size (nes), p-value (pValue),
and standard error (se).
- The m-value is the posterior probability that an eQTL effect exists in each tissue tested in the cross-tissue
meta-analysis (Han and Eskin, PLoS Genetics 8(3): e1002555, 2012).
- The normalized effect size is the slope of the linear regression of normalized expression data versus the three
genotype categories using single-tissue eQTL analysis, representing eQTL effect size.
- The p-value is from a t-test that compares observed NES from single-tissue eQTL analysis to a null NES of 0.

By default, the service queries the latest GTEx release. The retrieved data is split into pages
with `items_per_page` entries per page

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_meta_soft import PaginatedResponseMetaSoft
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
    api_instance = gtex_openapi.StaticAssociationEndpointsApi(api_client)
    gencode_id = 'gencode_id_example' # str | A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9
    variant_id = 'variant_id_example' # str | A gtex variant ID (optional)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Multi Tissue Eqtls
        api_response = api_instance.get_multi_tissue_eqtls_api_v2_association_metasoft_get(gencode_id, variant_id=variant_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of StaticAssociationEndpointsApi->get_multi_tissue_eqtls_api_v2_association_metasoft_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticAssociationEndpointsApi->get_multi_tissue_eqtls_api_v2_association_metasoft_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | **str**| A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9 | 
 **variant_id** | **str**| A gtex variant ID | [optional] 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseMetaSoft**](PaginatedResponseMetaSoft.md)

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

# **get_significant_single_tissue_eqtls_api_v2_association_single_tissue_eqtl_get**
> PaginatedResponseSingleTissueEqtl get_significant_single_tissue_eqtls_api_v2_association_single_tissue_eqtl_get(gencode_id=gencode_id, variant_id=variant_id, tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Significant Single Tissue Eqtls

Find significant single tissue eQTLs.

- This service returns precomputed significant single tissue eQTLs.
- Results may be filtered by tissue, gene, variant or dataset.
- To search by gene, use the versioned GENCODE ID.
- To search by variant, use the dbSNP rs ID (snpId).

By default, the service queries the latest GTEx release and the retrieved data is split
into pages with `items_per_page` entries per page

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_single_tissue_eqtl import PaginatedResponseSingleTissueEqtl
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
    api_instance = gtex_openapi.StaticAssociationEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 (optional)
    variant_id = ['variant_id_example'] # List[str] | A gtex variant ID (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Significant Single Tissue Eqtls
        api_response = api_instance.get_significant_single_tissue_eqtls_api_v2_association_single_tissue_eqtl_get(gencode_id=gencode_id, variant_id=variant_id, tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of StaticAssociationEndpointsApi->get_significant_single_tissue_eqtls_api_v2_association_single_tissue_eqtl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticAssociationEndpointsApi->get_significant_single_tissue_eqtls_api_v2_association_single_tissue_eqtl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | [optional] 
 **variant_id** | [**List[str]**](str.md)| A gtex variant ID | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseSingleTissueEqtl**](PaginatedResponseSingleTissueEqtl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable Process Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_significant_single_tissue_eqtls_by_location_api_v2_association_single_tissue_eqtl_by_location_get**
> IGVResponse get_significant_single_tissue_eqtls_by_location_api_v2_association_single_tissue_eqtl_by_location_get(tissue_site_detail_id, start, end, chromosome, dataset_id=dataset_id)

Get Significant Single Tissue Eqtls By Location

Find significant single tissue eQTLs using Chromosomal Locations.

- This service returns precomputed significant single tissue eQTLs.
- Results may be filtered by tissue, and/or dataset.

By default, the service queries the latest GTEx release. Since this endpoint is used to support a 
third party program on the portal, the return structure is different from other endpoints and is
not paginated.

### Example


```python
import gtex_openapi
from gtex_openapi.models.igv_response import IGVResponse
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
    api_instance = gtex_openapi.StaticAssociationEndpointsApi(api_client)
    tissue_site_detail_id = gtex_openapi.TissueSiteDetailId() # TissueSiteDetailId | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID
    start = 56 # int | 
    end = 56 # int | 
    chromosome = gtex_openapi.Chromosome() # Chromosome | Chromosome to Query
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)

    try:
        # Get Significant Single Tissue Eqtls By Location
        api_response = api_instance.get_significant_single_tissue_eqtls_by_location_api_v2_association_single_tissue_eqtl_by_location_get(tissue_site_detail_id, start, end, chromosome, dataset_id=dataset_id)
        print("The response of StaticAssociationEndpointsApi->get_significant_single_tissue_eqtls_by_location_api_v2_association_single_tissue_eqtl_by_location_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticAssociationEndpointsApi->get_significant_single_tissue_eqtls_by_location_api_v2_association_single_tissue_eqtl_by_location_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tissue_site_detail_id** | [**TissueSiteDetailId**](.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | 
 **start** | **int**|  | 
 **end** | **int**|  | 
 **chromosome** | [**Chromosome**](.md)| Chromosome to Query | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 

### Return type

[**IGVResponse**](IGVResponse.md)

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

# **get_significant_single_tissue_ieqtls_api_v2_association_single_tissue_i_eqtl_get**
> PaginatedResponseSingleTissueIEqtl get_significant_single_tissue_ieqtls_api_v2_association_single_tissue_i_eqtl_get(gencode_id=gencode_id, variant_id=variant_id, tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Significant Single Tissue Ieqtls

Retrieve Interaction eQTL Data.

- This service returns cell type interaction eQTLs (ieQTLs), from a specified dataset.
- Results may be filtered by tissue
- By default, the service queries the latest GTEx release.

The retrieved data is split into pages with `items_per_page` entries per page

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_single_tissue_i_eqtl import PaginatedResponseSingleTissueIEqtl
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
    api_instance = gtex_openapi.StaticAssociationEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 (optional)
    variant_id = ['variant_id_example'] # List[str] | A gtex variant ID (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Significant Single Tissue Ieqtls
        api_response = api_instance.get_significant_single_tissue_ieqtls_api_v2_association_single_tissue_i_eqtl_get(gencode_id=gencode_id, variant_id=variant_id, tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of StaticAssociationEndpointsApi->get_significant_single_tissue_ieqtls_api_v2_association_single_tissue_i_eqtl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticAssociationEndpointsApi->get_significant_single_tissue_ieqtls_api_v2_association_single_tissue_i_eqtl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | [optional] 
 **variant_id** | [**List[str]**](str.md)| A gtex variant ID | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseSingleTissueIEqtl**](PaginatedResponseSingleTissueIEqtl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable Process Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_significant_single_tissue_isqtls_api_v2_association_single_tissue_i_sqtl_get**
> PaginatedResponseSingleTissueISqtl get_significant_single_tissue_isqtls_api_v2_association_single_tissue_i_sqtl_get(gencode_id=gencode_id, variant_id=variant_id, tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Significant Single Tissue Isqtls

Retrieve Interaction sQTL Data.

- This service retrieves cell type interaction sQTLs (isQTLs), from a specified dataset.
- Results may be filtered by tissue
- By default, the service queries the latest GTEx release.

The retrieved data is split into pages with `items_per_page` entries per page

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_single_tissue_i_sqtl import PaginatedResponseSingleTissueISqtl
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
    api_instance = gtex_openapi.StaticAssociationEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 (optional)
    variant_id = ['variant_id_example'] # List[str] | A gtex variant ID (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Significant Single Tissue Isqtls
        api_response = api_instance.get_significant_single_tissue_isqtls_api_v2_association_single_tissue_i_sqtl_get(gencode_id=gencode_id, variant_id=variant_id, tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of StaticAssociationEndpointsApi->get_significant_single_tissue_isqtls_api_v2_association_single_tissue_i_sqtl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticAssociationEndpointsApi->get_significant_single_tissue_isqtls_api_v2_association_single_tissue_i_sqtl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | [optional] 
 **variant_id** | [**List[str]**](str.md)| A gtex variant ID | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseSingleTissueISqtl**](PaginatedResponseSingleTissueISqtl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable Process Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_significant_single_tissue_sqtls_api_v2_association_single_tissue_sqtl_get**
> PaginatedResponseSingleTissueSqtl get_significant_single_tissue_sqtls_api_v2_association_single_tissue_sqtl_get(gencode_id=gencode_id, variant_id=variant_id, tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Significant Single Tissue Sqtls

Retrieve Single Tissue sQTL Data.

- This service returns single tissue sQTL data for the given genes, from a specified dataset.
- Results may be filtered by tissue
- By default, the service queries the latest GTEx release.

The retrieved data is split into pages with `items_per_page` entries per page

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_single_tissue_sqtl import PaginatedResponseSingleTissueSqtl
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
    api_instance = gtex_openapi.StaticAssociationEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 (optional)
    variant_id = ['variant_id_example'] # List[str] | A gtex variant ID (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Significant Single Tissue Sqtls
        api_response = api_instance.get_significant_single_tissue_sqtls_api_v2_association_single_tissue_sqtl_get(gencode_id=gencode_id, variant_id=variant_id, tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of StaticAssociationEndpointsApi->get_significant_single_tissue_sqtls_api_v2_association_single_tissue_sqtl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticAssociationEndpointsApi->get_significant_single_tissue_sqtls_api_v2_association_single_tissue_sqtl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | [optional] 
 **variant_id** | [**List[str]**](str.md)| A gtex variant ID | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseSingleTissueSqtl**](PaginatedResponseSingleTissueSqtl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable Process Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sqtl_genes_api_v2_association_sgene_get**
> PaginatedResponseSGene get_sqtl_genes_api_v2_association_sgene_get(tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)

Get Sqtl Genes

Retrieve sGenes (sQTL Genes).

- This service returns sGenes (sQTL Genes) from the specified dataset.
- Results may be filtered by tissue.
- By default, the service queries the latest GTEx release.

The retrieved data is split into pages with `items_per_page` entries per page

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_s_gene import PaginatedResponseSGene
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
    api_instance = gtex_openapi.StaticAssociationEndpointsApi(api_client)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Sqtl Genes
        api_response = api_instance.get_sqtl_genes_api_v2_association_sgene_get(tissue_site_detail_id=tissue_site_detail_id, dataset_id=dataset_id, page=page, items_per_page=items_per_page)
        print("The response of StaticAssociationEndpointsApi->get_sqtl_genes_api_v2_association_sgene_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StaticAssociationEndpointsApi->get_sqtl_genes_api_v2_association_sgene_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseSGene**](PaginatedResponseSGene.md)

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

