# gabber.generated.gabber
The Gabber API is a set of APIs that allow you to interact with the Gabber platform.

The `gabber.generated.gabber` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3, < 3.0.0
* python-dateutil >= 2.8.2
* aiohttp >= 3.8.4
* aiohttp-retry >= 2.8.3
* pydantic >= 2
* typing-extensions >= 4.7.1

## Getting Started

In your own code, to use this library to connect and interact with gabber.generated.gabber,
you can run the following:

```python

import gabber.generated.gabber
from gabber.generated.gabber.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gabber.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = gabber.generated.gabber.Configuration(
    host = "https://api.gabber.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
async with gabber.generated.gabber.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gabber.generated.gabber.CreditApi(api_client)
    create_credit_request = gabber.generated.gabber.CreateCreditRequest() # CreateCreditRequest | 
    x_human_id = 'x_human_id_example' # str | When using x-api-key authentication, this header is used to scope requests to a specific human. (optional)

    try:
        # Create a new credit type
        api_response = await api_instance.create_credit(create_credit_request, x_human_id=x_human_id)
        print("The response of CreditApi->create_credit:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CreditApi->create_credit: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.gabber.dev*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CreditApi* | [**create_credit**](gabber/generated/gabber/docs/CreditApi.md#create_credit) | **POST** /v1/credit | Create a new credit type
*CreditApi* | [**create_credit_ledger_entry**](gabber/generated/gabber/docs/CreditApi.md#create_credit_ledger_entry) | **POST** /v1/credit/{credit}/ledger | Create a new credit ledger entry
*CreditApi* | [**get_credit**](gabber/generated/gabber/docs/CreditApi.md#get_credit) | **GET** /v1/credit/{credit} | Get a single credit object
*CreditApi* | [**get_latest_credit_ledger_entry**](gabber/generated/gabber/docs/CreditApi.md#get_latest_credit_ledger_entry) | **GET** /v1/credit/{credit}/ledger/latest | Get the latest credit ledger entry for a human. Requires a human id.
*CreditApi* | [**list_credits**](gabber/generated/gabber/docs/CreditApi.md#list_credits) | **GET** /v1/credit/list | Get a list of credits
*DummyApi* | [**dummy_get**](gabber/generated/gabber/docs/DummyApi.md#dummy_get) | **GET** /dummy | Dummy endpoint
*InferenceApi* | [**chat_completions**](gabber/generated/gabber/docs/InferenceApi.md#chat_completions) | **POST** /v1/chat/completions | Chat Completions (+ Voice)
*LLMApi* | [**create_context**](gabber/generated/gabber/docs/LLMApi.md#create_context) | **POST** /v1/llm/context | Create a new Context.
*LLMApi* | [**create_context_message**](gabber/generated/gabber/docs/LLMApi.md#create_context_message) | **POST** /v1/llm/context/{context}/message | Create a new ContextMessage.
*LLMApi* | [**get_context**](gabber/generated/gabber/docs/LLMApi.md#get_context) | **GET** /v1/llm/context/{context} | Retrieve a Context.
*LLMApi* | [**get_context_message**](gabber/generated/gabber/docs/LLMApi.md#get_context_message) | **GET** /v1/llm/context/{context}/message/{message} | Retrieve a ContextMessage.
*LLMApi* | [**get_llm**](gabber/generated/gabber/docs/LLMApi.md#get_llm) | **GET** /v1/llm/{llm} | Get a list of llms
*LLMApi* | [**list_context_messages**](gabber/generated/gabber/docs/LLMApi.md#list_context_messages) | **GET** /v1/llm/context/{context}/message/list | List ContextMessages.
*LLMApi* | [**list_contexts**](gabber/generated/gabber/docs/LLMApi.md#list_contexts) | **GET** /v1/llm/context/list | List Contexts.
*LLMApi* | [**list_llms**](gabber/generated/gabber/docs/LLMApi.md#list_llms) | **GET** /v1/llm/list | Get a list of llms
*LLMApi* | [**query_advanced_context_memory**](gabber/generated/gabber/docs/LLMApi.md#query_advanced_context_memory) | **POST** /v1/llm/context/{context}/advanced_memory/query | Query the advanced context memory
*PersonaApi* | [**create_persona**](gabber/generated/gabber/docs/PersonaApi.md#create_persona) | **POST** /v1/persona | Create a persona
*PersonaApi* | [**delete_persona**](gabber/generated/gabber/docs/PersonaApi.md#delete_persona) | **DELETE** /v1/persona/{persona_id} | Delete a persona
*PersonaApi* | [**get_persona**](gabber/generated/gabber/docs/PersonaApi.md#get_persona) | **GET** /v1/persona/{persona_id} | Get a persona
*PersonaApi* | [**list_personas**](gabber/generated/gabber/docs/PersonaApi.md#list_personas) | **GET** /v1/persona/list | Get a list of personas
*PersonaApi* | [**update_persona**](gabber/generated/gabber/docs/PersonaApi.md#update_persona) | **PUT** /v1/persona/{persona_id} | Update a persona
*RealtimeApi* | [**attach_human**](gabber/generated/gabber/docs/RealtimeApi.md#attach_human) | **POST** /v1/realtime/session/{session}/attach_human | Attach a human to a RealtimeSession
*RealtimeApi* | [**dtmf**](gabber/generated/gabber/docs/RealtimeApi.md#dtmf) | **POST** /v1/realtime/{session}/dtmf | DTMF
*RealtimeApi* | [**end_realtime_session**](gabber/generated/gabber/docs/RealtimeApi.md#end_realtime_session) | **POST** /v1/realtime/{session}/end | End a RealtimeSession.
*RealtimeApi* | [**get_realtime_session**](gabber/generated/gabber/docs/RealtimeApi.md#get_realtime_session) | **GET** /v1/realtime/{session} | Get a RealtimeSession.
*RealtimeApi* | [**get_realtime_session_messages**](gabber/generated/gabber/docs/RealtimeApi.md#get_realtime_session_messages) | **GET** /v1/realtime/{session}/messages | Get a RealtimeSession messages.
*RealtimeApi* | [**get_realtime_session_timeline**](gabber/generated/gabber/docs/RealtimeApi.md#get_realtime_session_timeline) | **GET** /v1/realtime/{session}/timeline | Get a RealtimeSession timeline.
*RealtimeApi* | [**initiate_outbound_call**](gabber/generated/gabber/docs/RealtimeApi.md#initiate_outbound_call) | **POST** /v1/realtime/{session}/outbound_call | Initiate an outbound call.
*RealtimeApi* | [**list_realtime_sessions**](gabber/generated/gabber/docs/RealtimeApi.md#list_realtime_sessions) | **GET** /v1/realtime/list | List Realtime Sessions.
*RealtimeApi* | [**speak**](gabber/generated/gabber/docs/RealtimeApi.md#speak) | **POST** /v1/realtime/{session}/speak | Speak
*RealtimeApi* | [**start_realtime_session**](gabber/generated/gabber/docs/RealtimeApi.md#start_realtime_session) | **POST** /v1/realtime/start | Start a new RealtimeSession.
*RealtimeApi* | [**update_realtime_session**](gabber/generated/gabber/docs/RealtimeApi.md#update_realtime_session) | **POST** /v1/realtime/{session}/update | Update a RealtimeSession.
*ScenarioApi* | [**create_scenario**](gabber/generated/gabber/docs/ScenarioApi.md#create_scenario) | **POST** /v1/scenario | Create a scenario
*ScenarioApi* | [**delete_scenario**](gabber/generated/gabber/docs/ScenarioApi.md#delete_scenario) | **DELETE** /v1/scenario/{scenario_id} | Delete a scenario
*ScenarioApi* | [**get_scenario**](gabber/generated/gabber/docs/ScenarioApi.md#get_scenario) | **GET** /v1/scenario/{scenario_id} | Get a scenario
*ScenarioApi* | [**list_scenarios**](gabber/generated/gabber/docs/ScenarioApi.md#list_scenarios) | **GET** /v1/scenario/list | Get a list of scenarios
*ScenarioApi* | [**update_scenario**](gabber/generated/gabber/docs/ScenarioApi.md#update_scenario) | **PUT** /v1/scenario/{scenario_id} | Update a scenario
*ToolApi* | [**create_tool_definition**](gabber/generated/gabber/docs/ToolApi.md#create_tool_definition) | **POST** /v1/tool | Create a tool definition
*ToolApi* | [**delete_tool_definition**](gabber/generated/gabber/docs/ToolApi.md#delete_tool_definition) | **DELETE** /v1/tool/{tool} | Delete a tool definition
*ToolApi* | [**get_tool_call_result**](gabber/generated/gabber/docs/ToolApi.md#get_tool_call_result) | **GET** /v1/tool/call/{call}/result | Get a tool call result
*ToolApi* | [**get_tool_definition**](gabber/generated/gabber/docs/ToolApi.md#get_tool_definition) | **GET** /v1/tool/{tool} | Get a tool definition
*ToolApi* | [**list_tool_definitions**](gabber/generated/gabber/docs/ToolApi.md#list_tool_definitions) | **GET** /v1/tool/list | List tools
*ToolApi* | [**update_tool_definition**](gabber/generated/gabber/docs/ToolApi.md#update_tool_definition) | **PUT** /v1/tool/{tool} | Update a tool definition
*UsageApi* | [**check_usage_token**](gabber/generated/gabber/docs/UsageApi.md#check_usage_token) | **POST** /v1/usage/token/check | Check a usage token
*UsageApi* | [**create_usage_token**](gabber/generated/gabber/docs/UsageApi.md#create_usage_token) | **POST** /v1/usage/token | Create a new usage token
*UsageApi* | [**get_usage_limits**](gabber/generated/gabber/docs/UsageApi.md#get_usage_limits) | **GET** /v1/usage/limits | Get usage limits
*UsageApi* | [**revoke_usage_token**](gabber/generated/gabber/docs/UsageApi.md#revoke_usage_token) | **POST** /v1/usage/token/revoke | Revoke a usage token
*UsageApi* | [**update_usage_token**](gabber/generated/gabber/docs/UsageApi.md#update_usage_token) | **PUT** /v1/usage/token | Update limits on a usage token
*UsageApi* | [**update_usage_token_ttl**](gabber/generated/gabber/docs/UsageApi.md#update_usage_token_ttl) | **POST** /v1/usage/token/update_ttl | Update the TTL of a usage token
*VoiceApi* | [**clone_voice**](gabber/generated/gabber/docs/VoiceApi.md#clone_voice) | **POST** /v1/voice/clone | Clone a voice
*VoiceApi* | [**delete_voice**](gabber/generated/gabber/docs/VoiceApi.md#delete_voice) | **DELETE** /v1/voice/{voice_id} | Delete a voice
*VoiceApi* | [**generate_voice**](gabber/generated/gabber/docs/VoiceApi.md#generate_voice) | **POST** /v1/voice/generate | Generate voice
*VoiceApi* | [**get_voice**](gabber/generated/gabber/docs/VoiceApi.md#get_voice) | **GET** /v1/voice/{voice_id} | Get a voice
*VoiceApi* | [**list_voices**](gabber/generated/gabber/docs/VoiceApi.md#list_voices) | **GET** /v1/voice/list | Get a list of voices
*VoiceApi* | [**update_voice**](gabber/generated/gabber/docs/VoiceApi.md#update_voice) | **PUT** /v1/voice/{voice_id} | Update a voice


## Documentation For Models

 - [AttachHumanRequest](gabber/generated/gabber/docs/AttachHumanRequest.md)
 - [BadRequest](gabber/generated/gabber/docs/BadRequest.md)
 - [ChatCompletionMessageToolCall](gabber/generated/gabber/docs/ChatCompletionMessageToolCall.md)
 - [ChatCompletionMessageToolCallChunk](gabber/generated/gabber/docs/ChatCompletionMessageToolCallChunk.md)
 - [ChatCompletionMessageToolCallFunction](gabber/generated/gabber/docs/ChatCompletionMessageToolCallFunction.md)
 - [ChatCompletionNamedToolChoice](gabber/generated/gabber/docs/ChatCompletionNamedToolChoice.md)
 - [ChatCompletionNamedToolChoiceFunction](gabber/generated/gabber/docs/ChatCompletionNamedToolChoiceFunction.md)
 - [ChatCompletionRequest](gabber/generated/gabber/docs/ChatCompletionRequest.md)
 - [ChatCompletionRequestAssistantMessage](gabber/generated/gabber/docs/ChatCompletionRequestAssistantMessage.md)
 - [ChatCompletionRequestGabber](gabber/generated/gabber/docs/ChatCompletionRequestGabber.md)
 - [ChatCompletionRequestMessage](gabber/generated/gabber/docs/ChatCompletionRequestMessage.md)
 - [ChatCompletionRequestMessageContentPartAudio](gabber/generated/gabber/docs/ChatCompletionRequestMessageContentPartAudio.md)
 - [ChatCompletionRequestMessageContentPartAudioInputAudio](gabber/generated/gabber/docs/ChatCompletionRequestMessageContentPartAudioInputAudio.md)
 - [ChatCompletionRequestMessageContentPartText](gabber/generated/gabber/docs/ChatCompletionRequestMessageContentPartText.md)
 - [ChatCompletionRequestSystemMessage](gabber/generated/gabber/docs/ChatCompletionRequestSystemMessage.md)
 - [ChatCompletionRequestSystemMessageContent](gabber/generated/gabber/docs/ChatCompletionRequestSystemMessageContent.md)
 - [ChatCompletionRequestToolMessage](gabber/generated/gabber/docs/ChatCompletionRequestToolMessage.md)
 - [ChatCompletionRequestUserMessage](gabber/generated/gabber/docs/ChatCompletionRequestUserMessage.md)
 - [ChatCompletionRequestUserMessageContent](gabber/generated/gabber/docs/ChatCompletionRequestUserMessageContent.md)
 - [ChatCompletionRequestUserMessageContentPart](gabber/generated/gabber/docs/ChatCompletionRequestUserMessageContentPart.md)
 - [ChatCompletionResponse](gabber/generated/gabber/docs/ChatCompletionResponse.md)
 - [ChatCompletionResponseChoicesInner](gabber/generated/gabber/docs/ChatCompletionResponseChoicesInner.md)
 - [ChatCompletionResponseGabber](gabber/generated/gabber/docs/ChatCompletionResponseGabber.md)
 - [ChatCompletionResponseGabberMessageData](gabber/generated/gabber/docs/ChatCompletionResponseGabberMessageData.md)
 - [ChatCompletionResponseGabberMessageDataData](gabber/generated/gabber/docs/ChatCompletionResponseGabberMessageDataData.md)
 - [ChatCompletionResponseMessage](gabber/generated/gabber/docs/ChatCompletionResponseMessage.md)
 - [ChatCompletionResponseMessageGabber](gabber/generated/gabber/docs/ChatCompletionResponseMessageGabber.md)
 - [ChatCompletionResponseMessageGabberVoice](gabber/generated/gabber/docs/ChatCompletionResponseMessageGabberVoice.md)
 - [ChatCompletionStreamResponse](gabber/generated/gabber/docs/ChatCompletionStreamResponse.md)
 - [ChatCompletionStreamResponseChoice](gabber/generated/gabber/docs/ChatCompletionStreamResponseChoice.md)
 - [ChatCompletionStreamResponseDelta](gabber/generated/gabber/docs/ChatCompletionStreamResponseDelta.md)
 - [ChatCompletionStreamResponseDeltaGabber](gabber/generated/gabber/docs/ChatCompletionStreamResponseDeltaGabber.md)
 - [ChatCompletionStreamResponseDeltaGabberVoice](gabber/generated/gabber/docs/ChatCompletionStreamResponseDeltaGabberVoice.md)
 - [ChatCompletionTool](gabber/generated/gabber/docs/ChatCompletionTool.md)
 - [ChatCompletionToolChoiceOption](gabber/generated/gabber/docs/ChatCompletionToolChoiceOption.md)
 - [CheckUsageToken200Response](gabber/generated/gabber/docs/CheckUsageToken200Response.md)
 - [CheckUsageTokenRequest](gabber/generated/gabber/docs/CheckUsageTokenRequest.md)
 - [Context](gabber/generated/gabber/docs/Context.md)
 - [ContextAdvancedMemoryEdge](gabber/generated/gabber/docs/ContextAdvancedMemoryEdge.md)
 - [ContextAdvancedMemoryNode](gabber/generated/gabber/docs/ContextAdvancedMemoryNode.md)
 - [ContextAdvancedMemoryQueryRequest](gabber/generated/gabber/docs/ContextAdvancedMemoryQueryRequest.md)
 - [ContextAdvancedMemoryQueryResult](gabber/generated/gabber/docs/ContextAdvancedMemoryQueryResult.md)
 - [ContextCreateRequest](gabber/generated/gabber/docs/ContextCreateRequest.md)
 - [ContextMessage](gabber/generated/gabber/docs/ContextMessage.md)
 - [ContextMessageContent](gabber/generated/gabber/docs/ContextMessageContent.md)
 - [ContextMessageContentText](gabber/generated/gabber/docs/ContextMessageContentText.md)
 - [ContextMessageCreateParams](gabber/generated/gabber/docs/ContextMessageCreateParams.md)
 - [ContextMessageToolCall](gabber/generated/gabber/docs/ContextMessageToolCall.md)
 - [ContextMessageToolCallFunction](gabber/generated/gabber/docs/ContextMessageToolCallFunction.md)
 - [CreateCreditLedgerEntryRequest](gabber/generated/gabber/docs/CreateCreditLedgerEntryRequest.md)
 - [CreateCreditRequest](gabber/generated/gabber/docs/CreateCreditRequest.md)
 - [CreatePersonaRequest](gabber/generated/gabber/docs/CreatePersonaRequest.md)
 - [CreateScenarioRequest](gabber/generated/gabber/docs/CreateScenarioRequest.md)
 - [CreateToolDefinitionCallSettings](gabber/generated/gabber/docs/CreateToolDefinitionCallSettings.md)
 - [CreateToolDefinitionCallSettingsDestination](gabber/generated/gabber/docs/CreateToolDefinitionCallSettingsDestination.md)
 - [CreateToolDefinitionRequest](gabber/generated/gabber/docs/CreateToolDefinitionRequest.md)
 - [CreateUsageToken200Response](gabber/generated/gabber/docs/CreateUsageToken200Response.md)
 - [Credit](gabber/generated/gabber/docs/Credit.md)
 - [CreditLedgerEntry](gabber/generated/gabber/docs/CreditLedgerEntry.md)
 - [DeletePersona200Response](gabber/generated/gabber/docs/DeletePersona200Response.md)
 - [DeleteScenario200Response](gabber/generated/gabber/docs/DeleteScenario200Response.md)
 - [DeleteVoice200Response](gabber/generated/gabber/docs/DeleteVoice200Response.md)
 - [DummyGet200Response](gabber/generated/gabber/docs/DummyGet200Response.md)
 - [FunctionObject](gabber/generated/gabber/docs/FunctionObject.md)
 - [GenerateVoiceRequest](gabber/generated/gabber/docs/GenerateVoiceRequest.md)
 - [GetRealtimeSessionMessages200Response](gabber/generated/gabber/docs/GetRealtimeSessionMessages200Response.md)
 - [GetRealtimeSessionTimeline200Response](gabber/generated/gabber/docs/GetRealtimeSessionTimeline200Response.md)
 - [HistoryMessage](gabber/generated/gabber/docs/HistoryMessage.md)
 - [HumanData](gabber/generated/gabber/docs/HumanData.md)
 - [HumanDataType](gabber/generated/gabber/docs/HumanDataType.md)
 - [InlineObject](gabber/generated/gabber/docs/InlineObject.md)
 - [LLM](gabber/generated/gabber/docs/LLM.md)
 - [ListContextMessages200Response](gabber/generated/gabber/docs/ListContextMessages200Response.md)
 - [ListContexts200Response](gabber/generated/gabber/docs/ListContexts200Response.md)
 - [ListCredits200Response](gabber/generated/gabber/docs/ListCredits200Response.md)
 - [ListLLMs200Response](gabber/generated/gabber/docs/ListLLMs200Response.md)
 - [ListPersonas200Response](gabber/generated/gabber/docs/ListPersonas200Response.md)
 - [ListRealtimeSessions200Response](gabber/generated/gabber/docs/ListRealtimeSessions200Response.md)
 - [ListScenarios200Response](gabber/generated/gabber/docs/ListScenarios200Response.md)
 - [ListToolDefinitions200Response](gabber/generated/gabber/docs/ListToolDefinitions200Response.md)
 - [ListVoices200Response](gabber/generated/gabber/docs/ListVoices200Response.md)
 - [Persona](gabber/generated/gabber/docs/Persona.md)
 - [PersonaTagsInner](gabber/generated/gabber/docs/PersonaTagsInner.md)
 - [RealtimeSession](gabber/generated/gabber/docs/RealtimeSession.md)
 - [RealtimeSessionConfig](gabber/generated/gabber/docs/RealtimeSessionConfig.md)
 - [RealtimeSessionConfigCreate](gabber/generated/gabber/docs/RealtimeSessionConfigCreate.md)
 - [RealtimeSessionConfigUpdate](gabber/generated/gabber/docs/RealtimeSessionConfigUpdate.md)
 - [RealtimeSessionConnectionDetails](gabber/generated/gabber/docs/RealtimeSessionConnectionDetails.md)
 - [RealtimeSessionDTMFDigit](gabber/generated/gabber/docs/RealtimeSessionDTMFDigit.md)
 - [RealtimeSessionDTMFRequest](gabber/generated/gabber/docs/RealtimeSessionDTMFRequest.md)
 - [RealtimeSessionData](gabber/generated/gabber/docs/RealtimeSessionData.md)
 - [RealtimeSessionDataType](gabber/generated/gabber/docs/RealtimeSessionDataType.md)
 - [RealtimeSessionGeneralConfig](gabber/generated/gabber/docs/RealtimeSessionGeneralConfig.md)
 - [RealtimeSessionGenerativeConfig](gabber/generated/gabber/docs/RealtimeSessionGenerativeConfig.md)
 - [RealtimeSessionGenerativeConfigCreate](gabber/generated/gabber/docs/RealtimeSessionGenerativeConfigCreate.md)
 - [RealtimeSessionGenerativeConfigUpdate](gabber/generated/gabber/docs/RealtimeSessionGenerativeConfigUpdate.md)
 - [RealtimeSessionInitiateOutboundCallRequest](gabber/generated/gabber/docs/RealtimeSessionInitiateOutboundCallRequest.md)
 - [RealtimeSessionInitiateOutboundCallRequestPhone](gabber/generated/gabber/docs/RealtimeSessionInitiateOutboundCallRequestPhone.md)
 - [RealtimeSessionInputConfig](gabber/generated/gabber/docs/RealtimeSessionInputConfig.md)
 - [RealtimeSessionOutputConfig](gabber/generated/gabber/docs/RealtimeSessionOutputConfig.md)
 - [RealtimeSessionStartResponse](gabber/generated/gabber/docs/RealtimeSessionStartResponse.md)
 - [RealtimeSessionTimelineItem](gabber/generated/gabber/docs/RealtimeSessionTimelineItem.md)
 - [RevokeUsageTokenRequest](gabber/generated/gabber/docs/RevokeUsageTokenRequest.md)
 - [SDKAgentState](gabber/generated/gabber/docs/SDKAgentState.md)
 - [SDKConnectOptions](gabber/generated/gabber/docs/SDKConnectOptions.md)
 - [SDKConnectOptionsOneOf](gabber/generated/gabber/docs/SDKConnectOptionsOneOf.md)
 - [SDKConnectOptionsOneOf1](gabber/generated/gabber/docs/SDKConnectOptionsOneOf1.md)
 - [SDKConnectionState](gabber/generated/gabber/docs/SDKConnectionState.md)
 - [SDKSendChatMessageParams](gabber/generated/gabber/docs/SDKSendChatMessageParams.md)
 - [SDKSessionTranscription](gabber/generated/gabber/docs/SDKSessionTranscription.md)
 - [Scenario](gabber/generated/gabber/docs/Scenario.md)
 - [Session](gabber/generated/gabber/docs/Session.md)
 - [SessionMessage](gabber/generated/gabber/docs/SessionMessage.md)
 - [SessionStartRequest](gabber/generated/gabber/docs/SessionStartRequest.md)
 - [SessionStartRequestOneOf](gabber/generated/gabber/docs/SessionStartRequestOneOf.md)
 - [SessionStartRequestOneOf1](gabber/generated/gabber/docs/SessionStartRequestOneOf1.md)
 - [SessionStartResponse](gabber/generated/gabber/docs/SessionStartResponse.md)
 - [SessionStartResponseConnectionDetails](gabber/generated/gabber/docs/SessionStartResponseConnectionDetails.md)
 - [SessionTimelineItem](gabber/generated/gabber/docs/SessionTimelineItem.md)
 - [SpeakRequest](gabber/generated/gabber/docs/SpeakRequest.md)
 - [StartRealtimeSessionRequest](gabber/generated/gabber/docs/StartRealtimeSessionRequest.md)
 - [TTSWebsocketRequestMessage](gabber/generated/gabber/docs/TTSWebsocketRequestMessage.md)
 - [TTSWebsocketRequestMessagePayload](gabber/generated/gabber/docs/TTSWebsocketRequestMessagePayload.md)
 - [TTSWebsocketRequestMessagePushTextPayload](gabber/generated/gabber/docs/TTSWebsocketRequestMessagePushTextPayload.md)
 - [TTSWebsocketRequestMessageStartSessionPayload](gabber/generated/gabber/docs/TTSWebsocketRequestMessageStartSessionPayload.md)
 - [TTSWebsocketRequestMessageType](gabber/generated/gabber/docs/TTSWebsocketRequestMessageType.md)
 - [TTSWebsocketResponseMessage](gabber/generated/gabber/docs/TTSWebsocketResponseMessage.md)
 - [TTSWebsocketResponseMessageAudioPayload](gabber/generated/gabber/docs/TTSWebsocketResponseMessageAudioPayload.md)
 - [TTSWebsocketResponseMessageErrorPayload](gabber/generated/gabber/docs/TTSWebsocketResponseMessageErrorPayload.md)
 - [TTSWebsocketResponseMessagePayload](gabber/generated/gabber/docs/TTSWebsocketResponseMessagePayload.md)
 - [TTSWebsocketResponseMessageType](gabber/generated/gabber/docs/TTSWebsocketResponseMessageType.md)
 - [ToolCallResult](gabber/generated/gabber/docs/ToolCallResult.md)
 - [ToolDefinition](gabber/generated/gabber/docs/ToolDefinition.md)
 - [ToolDefinitionCallSettingDestinationClientApp](gabber/generated/gabber/docs/ToolDefinitionCallSettingDestinationClientApp.md)
 - [ToolDefinitionCallSettingDestinationWebRequest](gabber/generated/gabber/docs/ToolDefinitionCallSettingDestinationWebRequest.md)
 - [ToolDefinitionCallSettings](gabber/generated/gabber/docs/ToolDefinitionCallSettings.md)
 - [ToolDefinitionCallSettingsDestination](gabber/generated/gabber/docs/ToolDefinitionCallSettingsDestination.md)
 - [ToolDefinitionParameter](gabber/generated/gabber/docs/ToolDefinitionParameter.md)
 - [UpdatePersonaRequest](gabber/generated/gabber/docs/UpdatePersonaRequest.md)
 - [UpdateScenarioRequest](gabber/generated/gabber/docs/UpdateScenarioRequest.md)
 - [UpdateSessionRequest](gabber/generated/gabber/docs/UpdateSessionRequest.md)
 - [UpdateUsageLimitsRequest](gabber/generated/gabber/docs/UpdateUsageLimitsRequest.md)
 - [UpdateUsageTokenTTLRequest](gabber/generated/gabber/docs/UpdateUsageTokenTTLRequest.md)
 - [UpdateVoiceRequest](gabber/generated/gabber/docs/UpdateVoiceRequest.md)
 - [Usage](gabber/generated/gabber/docs/Usage.md)
 - [UsageLimit](gabber/generated/gabber/docs/UsageLimit.md)
 - [UsageTokenRequest](gabber/generated/gabber/docs/UsageTokenRequest.md)
 - [UsageType](gabber/generated/gabber/docs/UsageType.md)
 - [Voice](gabber/generated/gabber/docs/Voice.md)
 - [VoicePricing](gabber/generated/gabber/docs/VoicePricing.md)
 - [VoiceTag](gabber/generated/gabber/docs/VoiceTag.md)
 - [WebhookMessage](gabber/generated/gabber/docs/WebhookMessage.md)
 - [WebhookMessageRealtimeSessionMessageCommitted](gabber/generated/gabber/docs/WebhookMessageRealtimeSessionMessageCommitted.md)
 - [WebhookMessageRealtimeSessionMessageCommittedPayload](gabber/generated/gabber/docs/WebhookMessageRealtimeSessionMessageCommittedPayload.md)
 - [WebhookMessageRealtimeSessionStateChanged](gabber/generated/gabber/docs/WebhookMessageRealtimeSessionStateChanged.md)
 - [WebhookMessageRealtimeSessionStateChangedPayload](gabber/generated/gabber/docs/WebhookMessageRealtimeSessionStateChangedPayload.md)
 - [WebhookMessageRealtimeSessionStateChangedpayloadSession](gabber/generated/gabber/docs/WebhookMessageRealtimeSessionStateChangedpayloadSession.md)
 - [WebhookMessageRealtimeSessionTimeLimitExceeded](gabber/generated/gabber/docs/WebhookMessageRealtimeSessionTimeLimitExceeded.md)
 - [WebhookMessageRealtimeSessionTimeLimitExceededPayload](gabber/generated/gabber/docs/WebhookMessageRealtimeSessionTimeLimitExceededPayload.md)
 - [WebhookMessageToolCall](gabber/generated/gabber/docs/WebhookMessageToolCall.md)
 - [WebhookMessageToolCallFunction](gabber/generated/gabber/docs/WebhookMessageToolCallFunction.md)
 - [WebhookMessageToolCallsFinished](gabber/generated/gabber/docs/WebhookMessageToolCallsFinished.md)
 - [WebhookMessageToolCallsFinishedPayload](gabber/generated/gabber/docs/WebhookMessageToolCallsFinishedPayload.md)
 - [WebhookMessageToolCallsStarted](gabber/generated/gabber/docs/WebhookMessageToolCallsStarted.md)
 - [WebhookMessageToolCallsStartedPayload](gabber/generated/gabber/docs/WebhookMessageToolCallsStartedPayload.md)
 - [WebhookMessageUsageTracked](gabber/generated/gabber/docs/WebhookMessageUsageTracked.md)
 - [WebhookMessageUsageTrackedPayload](gabber/generated/gabber/docs/WebhookMessageUsageTrackedPayload.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header

<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication (JWT)


## Author




