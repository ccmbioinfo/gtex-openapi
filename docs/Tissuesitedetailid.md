# Tissuesitedetailid

The ID of the tissue of interest. Can be a GTEx specific ID or an Ontology ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from gtex_openapi.models.tissuesitedetailid import Tissuesitedetailid

# TODO update the JSON string below
json = "{}"
# create an instance of Tissuesitedetailid from a JSON string
tissuesitedetailid_instance = Tissuesitedetailid.from_json(json)
# print the JSON string representation of the object
print(Tissuesitedetailid.to_json())

# convert the object into a dict
tissuesitedetailid_dict = tissuesitedetailid_instance.to_dict()
# create an instance of Tissuesitedetailid from a dict
tissuesitedetailid_from_dict = Tissuesitedetailid.from_dict(tissuesitedetailid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


