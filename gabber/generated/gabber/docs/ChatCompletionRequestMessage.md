# ChatCompletionRequestMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**ChatCompletionRequestSystemMessageContent**](ChatCompletionRequestSystemMessageContent.md) |  | 
**role** | **str** | The role of the messages author, in this case &#x60;tool&#x60;. | 
**refusal** | **str** | The refusal message by the assistant. | [optional] 
**tool_calls** | [**List[ChatCompletionMessageToolCall]**](ChatCompletionMessageToolCall.md) | The tool calls generated by the model, such as function calls. | [optional] 
**tool_call_id** | **str** | Tool call that this message is responding to. | 

## Example

```python
from gabber.generated.gabber.models.chat_completion_request_message import ChatCompletionRequestMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionRequestMessage from a JSON string
chat_completion_request_message_instance = ChatCompletionRequestMessage.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionRequestMessage.to_json())

# convert the object into a dict
chat_completion_request_message_dict = chat_completion_request_message_instance.to_dict()
# create an instance of ChatCompletionRequestMessage from a dict
chat_completion_request_message_from_dict = ChatCompletionRequestMessage.from_dict(chat_completion_request_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


