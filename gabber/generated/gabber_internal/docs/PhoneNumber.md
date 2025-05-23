# PhoneNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PhoneNumberType**](PhoneNumberType.md) |  | 
**number** | **str** |  | 
**capabilities** | [**PhoneNumberCapabilities**](PhoneNumberCapabilities.md) |  | 
**twilio_account_sid** | **str** |  | [optional] 
**phone_connection** | **str** |  | 
**attachment** | [**PhoneNumberAttachment**](PhoneNumberAttachment.md) |  | [optional] 

## Example

```python
from gabber.generated.gabber_internal.models.phone_number import PhoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumber from a JSON string
phone_number_instance = PhoneNumber.from_json(json)
# print the JSON string representation of the object
print(PhoneNumber.to_json())

# convert the object into a dict
phone_number_dict = phone_number_instance.to_dict()
# create an instance of PhoneNumber from a dict
phone_number_from_dict = PhoneNumber.from_dict(phone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


