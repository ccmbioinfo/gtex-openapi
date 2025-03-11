# TissueSiteDetail

The TissueSiteDetail is returned by the endpoints: `GET /tissueSiteDetail`. It provides the client with information about samples obtained from the detailed tissue site.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tissue_site_detail_id** | [**TissueSiteDetailId**](TissueSiteDetailId.md) |  | 
**color_hex** | **str** |  | 
**color_rgb** | **str** |  | 
**dataset_id** | [**DatasetId**](DatasetId.md) |  | 
**e_gene_count** | **int** |  | [optional] 
**expressed_gene_count** | **int** |  | [optional] 
**has_e_genes** | **bool** |  | 
**has_s_genes** | **bool** |  | 
**mapped_in_hubmap** | **bool** |  | 
**eqtl_sample_summary** | [**SexBasedSummary**](SexBasedSummary.md) |  | 
**rna_seq_sample_summary** | [**SexBasedSummary**](SexBasedSummary.md) |  | 
**s_gene_count** | **int** |  | [optional] 
**sampling_site** | **str** |  | 
**tissue_site** | **str** |  | 
**tissue_site_detail** | **str** |  | 
**tissue_site_detail_abbr** | **str** |  | 
**ontology_id** | [**TissueSiteOntologyId**](TissueSiteOntologyId.md) |  | 
**ontology_iri** | **str** |  | 

## Example

```python
from gtex_openapi.models.tissue_site_detail import TissueSiteDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TissueSiteDetail from a JSON string
tissue_site_detail_instance = TissueSiteDetail.from_json(json)
# print the JSON string representation of the object
print(TissueSiteDetail.to_json())

# convert the object into a dict
tissue_site_detail_dict = tissue_site_detail_instance.to_dict()
# create an instance of TissueSiteDetail from a dict
tissue_site_detail_from_dict = TissueSiteDetail.from_dict(tissue_site_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


