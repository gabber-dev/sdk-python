# ChatCompletionRequestAssistantMessage

Messages sent by the model in response to user messages. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**ChatCompletionRequestSystemMessageContent**](ChatCompletionRequestSystemMessageContent.md) |  | [optional] 
**refusal** | **str** | The refusal message by the assistant. | [optional] 
**role** | **str** | The role of the messages author, in this case &#x60;assistant&#x60;. | 
**tool_calls** | [**List[ChatCompletionMessageToolCall]**](ChatCompletionMessageToolCall.md) | The tool calls generated by the model, such as function calls. | [optional] 

## Example

```python
from gabber.generated.gabber.models.chat_completion_request_assistant_message import ChatCompletionRequestAssistantMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionRequestAssistantMessage from a JSON string
chat_completion_request_assistant_message_instance = ChatCompletionRequestAssistantMessage.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionRequestAssistantMessage.to_json())

# convert the object into a dict
chat_completion_request_assistant_message_dict = chat_completion_request_assistant_message_instance.to_dict()
# create an instance of ChatCompletionRequestAssistantMessage from a dict
chat_completion_request_assistant_message_from_dict = ChatCompletionRequestAssistantMessage.from_dict(chat_completion_request_assistant_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


