# BiobankResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_size** | **int** |  | 
**records_total** | **int** |  | 
**records_filtered** | **int** |  | 
**num_pages** | **int** |  | 
**sample** | [**List[BiobankSample]**](BiobankSample.md) |  | 

## Example

```python
from gtex_openapi.models.biobank_response import BiobankResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BiobankResponse from a JSON string
biobank_response_instance = BiobankResponse.from_json(json)
# print the JSON string representation of the object
print(BiobankResponse.to_json())

# convert the object into a dict
biobank_response_dict = biobank_response_instance.to_dict()
# create an instance of BiobankResponse from a dict
biobank_response_from_dict = BiobankResponse.from_dict(biobank_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


