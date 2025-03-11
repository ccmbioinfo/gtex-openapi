# gtex_openapi.ExpressionDataEndpointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_clustered_median_exon_expression_api_v2_expression_clustered_median_exon_expression_get**](ExpressionDataEndpointsApi.md#get_clustered_median_exon_expression_api_v2_expression_clustered_median_exon_expression_get) | **GET** /api/v2/expression/clusteredMedianExonExpression | Get Clustered Median Exon Expression
[**get_clustered_median_gene_expression_api_v2_expression_clustered_median_gene_expression_get**](ExpressionDataEndpointsApi.md#get_clustered_median_gene_expression_api_v2_expression_clustered_median_gene_expression_get) | **GET** /api/v2/expression/clusteredMedianGeneExpression | Get Clustered Median Gene Expression
[**get_clustered_median_junction_expression_api_v2_expression_clustered_median_junction_expression_get**](ExpressionDataEndpointsApi.md#get_clustered_median_junction_expression_api_v2_expression_clustered_median_junction_expression_get) | **GET** /api/v2/expression/clusteredMedianJunctionExpression | Get Clustered Median Junction Expression
[**get_clustered_median_transcript_expression_api_v2_expression_clustered_median_transcript_expression_get**](ExpressionDataEndpointsApi.md#get_clustered_median_transcript_expression_api_v2_expression_clustered_median_transcript_expression_get) | **GET** /api/v2/expression/clusteredMedianTranscriptExpression | Get Clustered Median Transcript Expression
[**get_expression_pca_api_v2_expression_expression_pca_get**](ExpressionDataEndpointsApi.md#get_expression_pca_api_v2_expression_expression_pca_get) | **GET** /api/v2/expression/expressionPca | Get Expression Pca
[**get_gene_expression_api_v2_expression_gene_expression_get**](ExpressionDataEndpointsApi.md#get_gene_expression_api_v2_expression_gene_expression_get) | **GET** /api/v2/expression/geneExpression | Get Gene Expression
[**get_median_exon_expression_api_v2_expression_median_exon_expression_get**](ExpressionDataEndpointsApi.md#get_median_exon_expression_api_v2_expression_median_exon_expression_get) | **GET** /api/v2/expression/medianExonExpression | Get Median Exon Expression
[**get_median_gene_expression_api_v2_expression_median_gene_expression_get**](ExpressionDataEndpointsApi.md#get_median_gene_expression_api_v2_expression_median_gene_expression_get) | **GET** /api/v2/expression/medianGeneExpression | Get Median Gene Expression
[**get_median_junction_expression_api_v2_expression_median_junction_expression_get**](ExpressionDataEndpointsApi.md#get_median_junction_expression_api_v2_expression_median_junction_expression_get) | **GET** /api/v2/expression/medianJunctionExpression | Get Median Junction Expression
[**get_median_transcript_expression_api_v2_expression_median_transcript_expression_get**](ExpressionDataEndpointsApi.md#get_median_transcript_expression_api_v2_expression_median_transcript_expression_get) | **GET** /api/v2/expression/medianTranscriptExpression | Get Median Transcript Expression
[**get_single_nucleus_gex_api_v2_expression_single_nucleus_gene_expression_get**](ExpressionDataEndpointsApi.md#get_single_nucleus_gex_api_v2_expression_single_nucleus_gene_expression_get) | **GET** /api/v2/expression/singleNucleusGeneExpression | Get Single Nucleus Gex
[**get_single_nucleus_gex_summary_api_v2_expression_single_nucleus_gene_expression_summary_get**](ExpressionDataEndpointsApi.md#get_single_nucleus_gex_summary_api_v2_expression_single_nucleus_gene_expression_summary_get) | **GET** /api/v2/expression/singleNucleusGeneExpressionSummary | Get Single Nucleus Gex Summary
[**get_top_expressed_genes_api_v2_expression_top_expressed_gene_get**](ExpressionDataEndpointsApi.md#get_top_expressed_genes_api_v2_expression_top_expressed_gene_get) | **GET** /api/v2/expression/topExpressedGene | Get Top Expressed Genes


# **get_clustered_median_exon_expression_api_v2_expression_clustered_median_exon_expression_get**
> ClusteredMedianExonExpression get_clustered_median_exon_expression_api_v2_expression_clustered_median_exon_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id)

Get Clustered Median Exon Expression

Find median transcript expression data along with hierarchical clusters .

- Returns median normalized transcript expression in tissues of all known transcripts of a given gene along with the
hierarchical clustering results of tissues and transcripts, based on exon expression, in Newick format.
- The hierarchical clustering is performed by calculating Euclidean distances and using the average linkage method.
- **This endpoint is not paginated.**

By default, this endpoint queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.clustered_median_exon_expression import ClusteredMedianExonExpression
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)

    try:
        # Get Clustered Median Exon Expression
        api_response = api_instance.get_clustered_median_exon_expression_api_v2_expression_clustered_median_exon_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id)
        print("The response of ExpressionDataEndpointsApi->get_clustered_median_exon_expression_api_v2_expression_clustered_median_exon_expression_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_clustered_median_exon_expression_api_v2_expression_clustered_median_exon_expression_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 

### Return type

[**ClusteredMedianExonExpression**](ClusteredMedianExonExpression.md)

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

# **get_clustered_median_gene_expression_api_v2_expression_clustered_median_gene_expression_get**
> ClusteredMedianGeneExpression get_clustered_median_gene_expression_api_v2_expression_clustered_median_gene_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id)

Get Clustered Median Gene Expression

Find median gene expression data along with hierarchical clusters .

- Returns median gene expression in tissues along with The hierarchical clustering results of tissues and genes,
based on gene expression, in Newick format.
- Results may be filtered by dataset, gene or tissue, but at least one gene must be provided
- The hierarchical clustering is performed by calculating Euclidean distances and using the average linkage method.
- **This endpoint is not paginated.**

By default, this service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.clustered_median_gene_expression import ClusteredMedianGeneExpression
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)

    try:
        # Get Clustered Median Gene Expression
        api_response = api_instance.get_clustered_median_gene_expression_api_v2_expression_clustered_median_gene_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id)
        print("The response of ExpressionDataEndpointsApi->get_clustered_median_gene_expression_api_v2_expression_clustered_median_gene_expression_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_clustered_median_gene_expression_api_v2_expression_clustered_median_gene_expression_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 

### Return type

[**ClusteredMedianGeneExpression**](ClusteredMedianGeneExpression.md)

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

# **get_clustered_median_junction_expression_api_v2_expression_clustered_median_junction_expression_get**
> ClusteredMedianJunctionExpression get_clustered_median_junction_expression_api_v2_expression_clustered_median_junction_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id)

Get Clustered Median Junction Expression

Find median junction expression data along with hierarchical clusters .

-  Returns median junction read counts in tissues of a given gene from all known transcripts along with
the hierarchical clustering results of tissues and genes, based on junction expression, in Newick format.
- Results may be filtered by dataset, gene or tissue, but at least one gene must be provided.
- The hierarchical clustering is performed by calculating Euclidean distances and using the average linkage method.
- **This endpoint is not paginated.**

By default, this service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.clustered_median_junction_expression import ClusteredMedianJunctionExpression
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)

    try:
        # Get Clustered Median Junction Expression
        api_response = api_instance.get_clustered_median_junction_expression_api_v2_expression_clustered_median_junction_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id)
        print("The response of ExpressionDataEndpointsApi->get_clustered_median_junction_expression_api_v2_expression_clustered_median_junction_expression_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_clustered_median_junction_expression_api_v2_expression_clustered_median_junction_expression_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 

### Return type

[**ClusteredMedianJunctionExpression**](ClusteredMedianJunctionExpression.md)

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

# **get_clustered_median_transcript_expression_api_v2_expression_clustered_median_transcript_expression_get**
> ClusteredMedianTranscriptExpression get_clustered_median_transcript_expression_api_v2_expression_clustered_median_transcript_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id)

Get Clustered Median Transcript Expression

Find median transcript expression data of all known transcripts of a gene along with hierarchical clusters .

-   Returns median normalized expression in tissues of all known transcripts of a given gene along with
the hierarchical clustering results of tissues and genes, based on expression, in Newick format.
- Results may be filtered by dataset, gene or tissue, but at least one gene must be provided.
- The hierarchical clustering is performed by calculating Euclidean distances and using the average linkage method.
- **This endpoint is not paginated.**

By default, this service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.clustered_median_transcript_expression import ClusteredMedianTranscriptExpression
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)

    try:
        # Get Clustered Median Transcript Expression
        api_response = api_instance.get_clustered_median_transcript_expression_api_v2_expression_clustered_median_transcript_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id)
        print("The response of ExpressionDataEndpointsApi->get_clustered_median_transcript_expression_api_v2_expression_clustered_median_transcript_expression_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_clustered_median_transcript_expression_api_v2_expression_clustered_median_transcript_expression_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 

### Return type

[**ClusteredMedianTranscriptExpression**](ClusteredMedianTranscriptExpression.md)

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

# **get_expression_pca_api_v2_expression_expression_pca_get**
> PaginatedResponseExpressionPCA get_expression_pca_api_v2_expression_expression_pca_get(tissue_site_detail_id, dataset_id=dataset_id, sample_id=sample_id, page=page, items_per_page=items_per_page)

Get Expression Pca

Find gene expression PCA data.

- Returns gene expression PCA (principal component analysis) in tissues.
- Results may be filtered by tissue, sample, or dataset.

By default, the service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_expression_pca import PaginatedResponseExpressionPCA
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    sample_id = 'sample_id_example' # str |  (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Expression Pca
        api_response = api_instance.get_expression_pca_api_v2_expression_expression_pca_get(tissue_site_detail_id, dataset_id=dataset_id, sample_id=sample_id, page=page, items_per_page=items_per_page)
        print("The response of ExpressionDataEndpointsApi->get_expression_pca_api_v2_expression_expression_pca_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_expression_pca_api_v2_expression_expression_pca_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **sample_id** | **str**|  | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseExpressionPCA**](PaginatedResponseExpressionPCA.md)

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

# **get_gene_expression_api_v2_expression_gene_expression_get**
> PaginatedResponseGeneExpression get_gene_expression_api_v2_expression_gene_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, attribute_subset=attribute_subset, page=page, items_per_page=items_per_page)

Get Gene Expression

Find normalized gene expression data.

- Returns normalized gene expression in tissues at the sample level.
- Results may be filtered by dataset, gene or tissue, but at least one gene must be provided.

By default, this service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_gene_expression import PaginatedResponseGeneExpression
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    attribute_subset = gtex_openapi.DonorAttribute() # DonorAttribute | Donor attribute to subset data by (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Gene Expression
        api_response = api_instance.get_gene_expression_api_v2_expression_gene_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, attribute_subset=attribute_subset, page=page, items_per_page=items_per_page)
        print("The response of ExpressionDataEndpointsApi->get_gene_expression_api_v2_expression_gene_expression_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_gene_expression_api_v2_expression_gene_expression_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **attribute_subset** | [**DonorAttribute**](.md)| Donor attribute to subset data by | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseGeneExpression**](PaginatedResponseGeneExpression.md)

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

# **get_median_exon_expression_api_v2_expression_median_exon_expression_get**
> PaginatedResponseMedianExonExpression get_median_exon_expression_api_v2_expression_median_exon_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)

Get Median Exon Expression

Find median exon expression data.

- Returns median exon read counts, in tissues, of a collapsed gene model.
- Results may be filtered by dataset, gene or tissue, but at least one gene must be provided

By default, this service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_median_exon_expression import PaginatedResponseMedianExonExpression
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Median Exon Expression
        api_response = api_instance.get_median_exon_expression_api_v2_expression_median_exon_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)
        print("The response of ExpressionDataEndpointsApi->get_median_exon_expression_api_v2_expression_median_exon_expression_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_median_exon_expression_api_v2_expression_median_exon_expression_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseMedianExonExpression**](PaginatedResponseMedianExonExpression.md)

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

# **get_median_gene_expression_api_v2_expression_median_gene_expression_get**
> PaginatedResponseMedianGeneExpression get_median_gene_expression_api_v2_expression_median_gene_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)

Get Median Gene Expression

Find median gene expression data along with hierarchical clusters .

- Returns median gene  expression in tissues.

By default, this endpoint queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_median_gene_expression import PaginatedResponseMedianGeneExpression
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Median Gene Expression
        api_response = api_instance.get_median_gene_expression_api_v2_expression_median_gene_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)
        print("The response of ExpressionDataEndpointsApi->get_median_gene_expression_api_v2_expression_median_gene_expression_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_median_gene_expression_api_v2_expression_median_gene_expression_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseMedianGeneExpression**](PaginatedResponseMedianGeneExpression.md)

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

# **get_median_junction_expression_api_v2_expression_median_junction_expression_get**
> PaginatedResponseMedianJunctionExpression get_median_junction_expression_api_v2_expression_median_junction_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)

Get Median Junction Expression

Find junction gene expression data.

- Returns median junction read counts in tissues of a given gene from all known transcripts.
- Results may be filtered by dataset or tissue.

By default, this service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_median_junction_expression import PaginatedResponseMedianJunctionExpression
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Median Junction Expression
        api_response = api_instance.get_median_junction_expression_api_v2_expression_median_junction_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)
        print("The response of ExpressionDataEndpointsApi->get_median_junction_expression_api_v2_expression_median_junction_expression_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_median_junction_expression_api_v2_expression_median_junction_expression_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseMedianJunctionExpression**](PaginatedResponseMedianJunctionExpression.md)

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

# **get_median_transcript_expression_api_v2_expression_median_transcript_expression_get**
> PaginatedResponseMedianTranscriptExpression get_median_transcript_expression_api_v2_expression_median_transcript_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)

Get Median Transcript Expression

Find median transcript expression data of all known transcripts of a gene.

- Returns median normalized expression in tissues of all known transcripts of a given gene.
- Results may be filtered by dataset or tissue.

 By default, this service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_median_transcript_expression import PaginatedResponseMedianTranscriptExpression
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Median Transcript Expression
        api_response = api_instance.get_median_transcript_expression_api_v2_expression_median_transcript_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)
        print("The response of ExpressionDataEndpointsApi->get_median_transcript_expression_api_v2_expression_median_transcript_expression_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_median_transcript_expression_api_v2_expression_median_transcript_expression_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseMedianTranscriptExpression**](PaginatedResponseMedianTranscriptExpression.md)

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

# **get_single_nucleus_gex_api_v2_expression_single_nucleus_gene_expression_get**
> PaginatedResponseSingleNucleusGeneExpressionResult get_single_nucleus_gex_api_v2_expression_single_nucleus_gene_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, exclude_data_array=exclude_data_array, page=page, items_per_page=items_per_page)

Get Single Nucleus Gex

Retrieve Single Nucleus Gene Expression Data for a given Gene.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_single_nucleus_gene_expression_result import PaginatedResponseSingleNucleusGeneExpressionResult
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    gencode_id = ['gencode_id_example'] # List[str] | A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5
    dataset_id = gtex_openapi.DatasetId() # DatasetId |  (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    exclude_data_array = True # bool | Include Expression Values in Result. Set to `false` to include the data array (optional) (default to True)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Single Nucleus Gex
        api_response = api_instance.get_single_nucleus_gex_api_v2_expression_single_nucleus_gene_expression_get(gencode_id, dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, exclude_data_array=exclude_data_array, page=page, items_per_page=items_per_page)
        print("The response of ExpressionDataEndpointsApi->get_single_nucleus_gex_api_v2_expression_single_nucleus_gene_expression_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_single_nucleus_gex_api_v2_expression_single_nucleus_gene_expression_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gencode_id** | [**List[str]**](str.md)| A list of Versioned GENCODE IDs, e.g. ENSG00000065613.9,ENSG00000203782.5 | 
 **dataset_id** | [**DatasetId**](.md)|  | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **exclude_data_array** | **bool**| Include Expression Values in Result. Set to &#x60;false&#x60; to include the data array | [optional] [default to True]
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseSingleNucleusGeneExpressionResult**](PaginatedResponseSingleNucleusGeneExpressionResult.md)

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

# **get_single_nucleus_gex_summary_api_v2_expression_single_nucleus_gene_expression_summary_get**
> PaginatedResponseSingleNucleusGeneExpressionSummary get_single_nucleus_gex_summary_api_v2_expression_single_nucleus_gene_expression_summary_get(dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)

Get Single Nucleus Gex Summary

Retrieve Summarized Single Nucleus Gene Expression Data.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_single_nucleus_gene_expression_summary import PaginatedResponseSingleNucleusGeneExpressionSummary
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    dataset_id = gtex_openapi.DatasetId() # DatasetId |  (optional)
    tissue_site_detail_id = [gtex_openapi.TissuesitedetailidInner()] # List[TissuesitedetailidInner] | A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID (optional)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Single Nucleus Gex Summary
        api_response = api_instance.get_single_nucleus_gex_summary_api_v2_expression_single_nucleus_gene_expression_summary_get(dataset_id=dataset_id, tissue_site_detail_id=tissue_site_detail_id, page=page, items_per_page=items_per_page)
        print("The response of ExpressionDataEndpointsApi->get_single_nucleus_gex_summary_api_v2_expression_single_nucleus_gene_expression_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_single_nucleus_gex_summary_api_v2_expression_single_nucleus_gene_expression_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_id** | [**DatasetId**](.md)|  | [optional] 
 **tissue_site_detail_id** | [**List[TissuesitedetailidInner]**](TissuesitedetailidInner.md)| A list of Tissue IDs of the tissue(s) of interest. Can be a GTEx specific ID or an Ontology ID | [optional] 
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseSingleNucleusGeneExpressionSummary**](PaginatedResponseSingleNucleusGeneExpressionSummary.md)

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

# **get_top_expressed_genes_api_v2_expression_top_expressed_gene_get**
> PaginatedResponseTopExpressedGenes get_top_expressed_genes_api_v2_expression_top_expressed_gene_get(tissue_site_detail_id, dataset_id=dataset_id, filter_mt_gene=filter_mt_gene, page=page, items_per_page=items_per_page)

Get Top Expressed Genes

Find top expressed genes for a specified tissue.

- Returns top expressed genes for a specified tissue in a dataset, sorted by median expression.
- When the optional parameter `filterMtGene` is set to true, mitochondrial genes will be excluded from the results.

By default, this service queries the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.paginated_response_top_expressed_genes import PaginatedResponseTopExpressedGenes
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
    api_instance = gtex_openapi.ExpressionDataEndpointsApi(api_client)
    tissue_site_detail_id = gtex_openapi.Tissuesitedetailid() # Tissuesitedetailid | The ID of the tissue of interest. Can be a GTEx specific ID or an Ontology ID
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)
    filter_mt_gene = True # bool | exclude mt genes (optional) (default to True)
    page = 0 # int | The 0-based numeric ID of the page to retrieve (optional) (default to 0)
    items_per_page = 250 # int |  (optional) (default to 250)

    try:
        # Get Top Expressed Genes
        api_response = api_instance.get_top_expressed_genes_api_v2_expression_top_expressed_gene_get(tissue_site_detail_id, dataset_id=dataset_id, filter_mt_gene=filter_mt_gene, page=page, items_per_page=items_per_page)
        print("The response of ExpressionDataEndpointsApi->get_top_expressed_genes_api_v2_expression_top_expressed_gene_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpressionDataEndpointsApi->get_top_expressed_genes_api_v2_expression_top_expressed_gene_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tissue_site_detail_id** | [**Tissuesitedetailid**](.md)| The ID of the tissue of interest. Can be a GTEx specific ID or an Ontology ID | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 
 **filter_mt_gene** | **bool**| exclude mt genes | [optional] [default to True]
 **page** | **int**| The 0-based numeric ID of the page to retrieve | [optional] [default to 0]
 **items_per_page** | **int**|  | [optional] [default to 250]

### Return type

[**PaginatedResponseTopExpressedGenes**](PaginatedResponseTopExpressedGenes.md)

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

