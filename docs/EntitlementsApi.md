# persona.EntitlementsApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entitlements_allow_post**](EntitlementsApi.md#entitlements_allow_post) | **POST** /entitlements/allow | 
[**entitlements_allow_uuid_post**](EntitlementsApi.md#entitlements_allow_uuid_post) | **POST** /entitlements/allow/{uuid} | Grant product access to a customer
[**entitlements_get**](EntitlementsApi.md#entitlements_get) | **GET** /entitlements | List all entitlements


# **entitlements_allow_post**
> list[object] entitlements_allow_post(body, auth_user=auth_user, authorization=authorization)



### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.EntitlementsApi()
body = persona.EntitlementAccess() # EntitlementAccess | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_response = api_instance.entitlements_allow_post(body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitlementsApi->entitlements_allow_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EntitlementAccess**](EntitlementAccess.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_allow_uuid_post**
> list[object] entitlements_allow_uuid_post(uuid, body, auth_user=auth_user, authorization=authorization)

Grant product access to a customer

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.EntitlementsApi()
uuid = 'uuid_example' # str | 
body = persona.EntitlementAccess() # EntitlementAccess | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Grant product access to a customer
    api_response = api_instance.entitlements_allow_uuid_post(uuid, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitlementsApi->entitlements_allow_uuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **body** | [**EntitlementAccess**](EntitlementAccess.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_get**
> dict(str, list[str]) entitlements_get()

List all entitlements

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.EntitlementsApi()

try:
    # List all entitlements
    api_response = api_instance.entitlements_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitlementsApi->entitlements_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, list[str])**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

