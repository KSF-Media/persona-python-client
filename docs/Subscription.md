# Subscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subsno** | **int** | Subscription Id - primary key together with extno | 
**extno** | **int** | Subscription Extension Id - how many times a subscription has been extended | 
**cusno** | **int** | Customer getting the subscription | 
**paycusno** | **int** | Customer paying for the subscription | 
**kind** | **str** | Subscription kind - what kind of order is it | 
**state** | **str** | Current state of the Subscription | 
**pricegroup** | **str** | Pricegroup of the Subscription | [optional] 
**package** | [**Package**](Package.md) |  | 
**dates** | [**SubscriptionDates**](SubscriptionDates.md) |  | 
**extsubsexists** | **bool** | If the extension of this subscription exists | 
**campaign** | [**PackageCampaign**](PackageCampaign.md) |  | [optional] 
**paused** | [**list[PausedSubscription]**](PausedSubscription.md) | Pause periods of this subscription | [optional] 
**receiver** | **str** | The name of subscription receiver | [optional] 
**delivery_address** | [**DeliveryAddress**](DeliveryAddress.md) |  | [optional] 
**pending_address_changes** | [**list[PendingAddressChange]**](PendingAddressChange.md) | Pending and ongoing temporary address changes | [optional] 
**order_number** | **str** | Order number of subscription | [optional] 
**payment_method** | **str** | Payment method of subscription | [optional] 
**payment_method_id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


