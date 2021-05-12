# Package

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Package identifier | 
**name** | **str** | Package name | 
**info** | **list[str]** | Package description | 
**paper** | [**Paper**](Paper.md) |  | 
**digital_only** | **bool** | All products in this package are digital | 
**products** | [**list[Product]**](Product.md) | The Products contained in a package | 
**offers** | [**list[PackageOffer]**](PackageOffer.md) | Offers for the package | 
**campaigns** | [**list[PackageCampaign]**](PackageCampaign.md) | Active campaigns for the package | 
**next_delivery** | **date** |  | [optional] 
**can_pause** | **bool** | Does the package allow delivery pauses | 
**can_temp_addr** | **bool** | Does the package allow temporary address changes | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


