# FunctionObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of what the function does, used by the model to choose when and how to call the function. | [optional] 
**name** | **str** | The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. | 
**parameters** | **object** | The parameters the functions accepts, described as a JSON Schema object. See the [guide](/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.   Omitting &#x60;parameters&#x60; defines a function with an empty parameter list. | [optional] 
**strict** | **bool** | Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the &#x60;parameters&#x60; field. Only a subset of JSON Schema is supported when &#x60;strict&#x60; is &#x60;true&#x60;. Learn more about Structured Outputs in the [function calling guide](docs/guides/function-calling). | [optional] [default to False]

## Example

```python
from gabber.generated.gabber.models.function_object import FunctionObject

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionObject from a JSON string
function_object_instance = FunctionObject.from_json(json)
# print the JSON string representation of the object
print(FunctionObject.to_json())

# convert the object into a dict
function_object_dict = function_object_instance.to_dict()
# create an instance of FunctionObject from a dict
function_object_from_dict = FunctionObject.from_dict(function_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


