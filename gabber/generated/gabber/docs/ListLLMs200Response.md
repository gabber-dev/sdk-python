# ListLLMs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** | The token for the next page of results, or null if there are no more pages. | 
**total_count** | **int** | The total number of items available. | 
**values** | [**List[LLM]**](LLM.md) | The array of voices. | 

## Example

```python
from gabber.generated.gabber.models.list_llms200_response import ListLLMs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListLLMs200Response from a JSON string
list_llms200_response_instance = ListLLMs200Response.from_json(json)
# print the JSON string representation of the object
print(ListLLMs200Response.to_json())

# convert the object into a dict
list_llms200_response_dict = list_llms200_response_instance.to_dict()
# create an instance of ListLLMs200Response from a dict
list_llms200_response_from_dict = ListLLMs200Response.from_dict(list_llms200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


