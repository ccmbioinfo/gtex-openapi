# gtex_openapi.DynamicAssociationEndpointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_post**](DynamicAssociationEndpointsApi.md#bulk_calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_post) | **POST** /api/v2/association/dyneqtl | Bulk Calculate Expression Quantitative Trait Loci
[**calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_get**](DynamicAssociationEndpointsApi.md#calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_get) | **GET** /api/v2/association/dyneqtl | Calculate Expression Quantitative Trait Loci
[**calculate_ieqtls_api_v2_association_dynieqtl_get**](DynamicAssociationEndpointsApi.md#calculate_ieqtls_api_v2_association_dynieqtl_get) | **GET** /api/v2/association/dynieqtl | Calculate Ieqtls
[**calculate_isqtls_api_v2_association_dynisqtl_get**](DynamicAssociationEndpointsApi.md#calculate_isqtls_api_v2_association_dynisqtl_get) | **GET** /api/v2/association/dynisqtl | Calculate Isqtls
[**calculate_splicing_quantitative_trait_loci_api_v2_association_dynsqtl_get**](DynamicAssociationEndpointsApi.md#calculate_splicing_quantitative_trait_loci_api_v2_association_dynsqtl_get) | **GET** /api/v2/association/dynsqtl | Calculate Splicing Quantitative Trait Loci


# **bulk_calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_post**
> PostDynamicEqtlResult bulk_calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_post(dynamic_eqtl_body, dataset_id=dataset_id)

Bulk Calculate Expression Quantitative Trait Loci

Calculate your own eQTLs

- This service calculates the gene-variant association for any given pair of gene and variant,
which may or may not be significant.
- This requires as input a GENCODE ID, GTEx variant ID, and tissue site detail ID.

By default, the calculation is based on the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.dynamic_eqtl_body import DynamicEqtlBody
from gtex_openapi.models.post_dynamic_eqtl_result import PostDynamicEqtlResult
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
    api_instance = gtex_openapi.DynamicAssociationEndpointsApi(api_client)
    dynamic_eqtl_body = [gtex_openapi.DynamicEqtlBody()] # List[DynamicEqtlBody] | 
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)

    try:
        # Bulk Calculate Expression Quantitative Trait Loci
        api_response = api_instance.bulk_calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_post(dynamic_eqtl_body, dataset_id=dataset_id)
        print("The response of DynamicAssociationEndpointsApi->bulk_calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicAssociationEndpointsApi->bulk_calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_eqtl_body** | [**List[DynamicEqtlBody]**](DynamicEqtlBody.md)|  | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 

### Return type

[**PostDynamicEqtlResult**](PostDynamicEqtlResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_get**
> Eqtl calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_get(tissue_site_detail_id, gencode_id, variant_id, dataset_id=dataset_id)

Calculate Expression Quantitative Trait Loci

Calculate your own eQTLs

- This service calculates the gene-variant association for any given pair of gene and variant,
which may or may not be significant.
- This requires as input a GENCODE ID, GTEx variant ID, and tissue site detail ID.

By default, the calculation is based on the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.eqtl import Eqtl
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
    api_instance = gtex_openapi.DynamicAssociationEndpointsApi(api_client)
    tissue_site_detail_id = gtex_openapi.Tissuesitedetailid() # Tissuesitedetailid | The ID of the tissue of interest. Can be a GTEx specific ID or an Ontology ID
    gencode_id = 'gencode_id_example' # str | A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9
    variant_id = 'variant_id_example' # str | A gtex variant ID
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)

    try:
        # Calculate Expression Quantitative Trait Loci
        api_response = api_instance.calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_get(tissue_site_detail_id, gencode_id, variant_id, dataset_id=dataset_id)
        print("The response of DynamicAssociationEndpointsApi->calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicAssociationEndpointsApi->calculate_expression_quantitative_trait_loci_api_v2_association_dyneqtl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tissue_site_detail_id** | [**Tissuesitedetailid**](.md)| The ID of the tissue of interest. Can be a GTEx specific ID or an Ontology ID | 
 **gencode_id** | **str**| A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9 | 
 **variant_id** | **str**| A gtex variant ID | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 

### Return type

[**Eqtl**](Eqtl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable to calculate eQTL |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_ieqtls_api_v2_association_dynieqtl_get**
> IEqtl calculate_ieqtls_api_v2_association_dynieqtl_get(cell_type, tissue_site_detail_id, gencode_id, variant_id, dataset_id=dataset_id)

Calculate Ieqtls

Calculate your own Cell Specific eQTLs.

- This service calculates the gene-variant association for any given pair of
gene and variant, which may or may not be significant.
- This requires as input a GENCODE ID, GTEx variant ID, and tissue site detail ID.

By default, the calculation is based on the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.cell_type import CellType
from gtex_openapi.models.i_eqtl import IEqtl
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
    api_instance = gtex_openapi.DynamicAssociationEndpointsApi(api_client)
    cell_type = gtex_openapi.CellType() # CellType | 
    tissue_site_detail_id = gtex_openapi.TissueSiteDetailId() # TissueSiteDetailId | The ID of the tissue of interest. Can be a GTEx specific ID or an Ontology ID
    gencode_id = 'gencode_id_example' # str | A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9
    variant_id = 'variant_id_example' # str | A gtex variant ID
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)

    try:
        # Calculate Ieqtls
        api_response = api_instance.calculate_ieqtls_api_v2_association_dynieqtl_get(cell_type, tissue_site_detail_id, gencode_id, variant_id, dataset_id=dataset_id)
        print("The response of DynamicAssociationEndpointsApi->calculate_ieqtls_api_v2_association_dynieqtl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicAssociationEndpointsApi->calculate_ieqtls_api_v2_association_dynieqtl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cell_type** | [**CellType**](.md)|  | 
 **tissue_site_detail_id** | [**TissueSiteDetailId**](.md)| The ID of the tissue of interest. Can be a GTEx specific ID or an Ontology ID | 
 **gencode_id** | **str**| A Versioned GENCODE ID of a gene, e.g. ENSG00000065613.9 | 
 **variant_id** | **str**| A gtex variant ID | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 

### Return type

[**IEqtl**](IEqtl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable to calculate ieQTL |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_isqtls_api_v2_association_dynisqtl_get**
> ISqtl calculate_isqtls_api_v2_association_dynisqtl_get(cell_type, tissue_site_detail_id, phenotype_id, variant_id, dataset_id=dataset_id)

Calculate Isqtls

Calculate your own Cell Specific sQTLs.

- This service calculates the gene-variant association for any given pair of
gene and variant, which may or may not be significant.
- This requires as input a GENCODE ID, GTEx variant ID, and tissue site detail ID.

By default, the calculation is based on the latest GTEx release.

### Example


```python
import gtex_openapi
from gtex_openapi.models.cell_type import CellType
from gtex_openapi.models.i_sqtl import ISqtl
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
    api_instance = gtex_openapi.DynamicAssociationEndpointsApi(api_client)
    cell_type = gtex_openapi.CellType() # CellType | 
    tissue_site_detail_id = gtex_openapi.Tissuesitedetailid() # Tissuesitedetailid | The ID of the tissue of interest. Can be a GTEx specific ID or an Ontology ID
    phenotype_id = 'phenotype_id_example' # str | 
    variant_id = 'variant_id_example' # str | A gtex variant ID
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)

    try:
        # Calculate Isqtls
        api_response = api_instance.calculate_isqtls_api_v2_association_dynisqtl_get(cell_type, tissue_site_detail_id, phenotype_id, variant_id, dataset_id=dataset_id)
        print("The response of DynamicAssociationEndpointsApi->calculate_isqtls_api_v2_association_dynisqtl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicAssociationEndpointsApi->calculate_isqtls_api_v2_association_dynisqtl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cell_type** | [**CellType**](.md)|  | 
 **tissue_site_detail_id** | [**Tissuesitedetailid**](.md)| The ID of the tissue of interest. Can be a GTEx specific ID or an Ontology ID | 
 **phenotype_id** | **str**|  | 
 **variant_id** | **str**| A gtex variant ID | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 

### Return type

[**ISqtl**](ISqtl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable to calculate isQTL |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_splicing_quantitative_trait_loci_api_v2_association_dynsqtl_get**
> Sqtl calculate_splicing_quantitative_trait_loci_api_v2_association_dynsqtl_get(tissue_site_detail_id, phenotype_id, variant_id, dataset_id=dataset_id)

Calculate Splicing Quantitative Trait Loci

### Example


```python
import gtex_openapi
from gtex_openapi.models.sqtl import Sqtl
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
    api_instance = gtex_openapi.DynamicAssociationEndpointsApi(api_client)
    tissue_site_detail_id = gtex_openapi.TissueSiteDetailId() # TissueSiteDetailId | The ID of the tissue of interest. Can be a GTEx specific ID or an Ontology ID
    phenotype_id = 'phenotype_id_example' # str | 
    variant_id = 'variant_id_example' # str | A gtex variant ID
    dataset_id = gtex_openapi.DatasetId() # DatasetId | Unique identifier of a dataset. Usually includes a data source and data release. (optional)

    try:
        # Calculate Splicing Quantitative Trait Loci
        api_response = api_instance.calculate_splicing_quantitative_trait_loci_api_v2_association_dynsqtl_get(tissue_site_detail_id, phenotype_id, variant_id, dataset_id=dataset_id)
        print("The response of DynamicAssociationEndpointsApi->calculate_splicing_quantitative_trait_loci_api_v2_association_dynsqtl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicAssociationEndpointsApi->calculate_splicing_quantitative_trait_loci_api_v2_association_dynsqtl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tissue_site_detail_id** | [**TissueSiteDetailId**](.md)| The ID of the tissue of interest. Can be a GTEx specific ID or an Ontology ID | 
 **phenotype_id** | **str**|  | 
 **variant_id** | **str**| A gtex variant ID | 
 **dataset_id** | [**DatasetId**](.md)| Unique identifier of a dataset. Usually includes a data source and data release. | [optional] 

### Return type

[**Sqtl**](Sqtl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable to calculate sQTL |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

