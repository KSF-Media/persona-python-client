# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**email** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**cusno** | **int** |  | 
**subs** | [**list[Subscription]**](Subscription.md) |  | 
**consent** | [**list[GdprConsent]**](GdprConsent.md) |  | 
**legal** | [**list[LegalConsent]**](LegalConsent.md) |  | 
**pending_address_changes** | [**list[PendingAddressChange]**](PendingAddressChange.md) |  | [optional] 
**past_temporary_addresses** | [**list[PastTemporaryAddress]**](PastTemporaryAddress.md) |  | 
**has_completed_registration** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


