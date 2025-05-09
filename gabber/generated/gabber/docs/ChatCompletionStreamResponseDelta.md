# ChatCompletionStreamResponseDelta

A chat completion delta generated by streamed model responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The contents of the chunk message. | 
**role** | **str** | The role of the author of this message. | 
**tool_calls** | [**List[ChatCompletionMessageToolCallChunk]**](ChatCompletionMessageToolCallChunk.md) |  | [optional] 
**refusal** | **str** | The refusal message generated by the model. | [optional] 
**gabber** | [**ChatCompletionStreamResponseDeltaGabber**](ChatCompletionStreamResponseDeltaGabber.md) |  | [optional] 

## Example

```python
from gabber.generated.gabber.models.chat_completion_stream_response_delta import ChatCompletionStreamResponseDelta

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionStreamResponseDelta from a JSON string
chat_completion_stream_response_delta_instance = ChatCompletionStreamResponseDelta.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionStreamResponseDelta.to_json())

# convert the object into a dict
chat_completion_stream_response_delta_dict = chat_completion_stream_response_delta_instance.to_dict()
# create an instance of ChatCompletionStreamResponseDelta from a dict
chat_completion_stream_response_delta_from_dict = ChatCompletionStreamResponseDelta.from_dict(chat_completion_stream_response_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


