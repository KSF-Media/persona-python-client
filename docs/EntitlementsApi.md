# persona.EntitlementsApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entitlements_allow_delete**](EntitlementsApi.md#entitlements_allow_delete) | **DELETE** /entitlements/allow | Remove an entitlement
[**entitlements_allow_get**](EntitlementsApi.md#entitlements_allow_get) | **GET** /entitlements/allow | Check if global entitlements are enabled
[**entitlements_allow_post**](EntitlementsApi.md#entitlements_allow_post) | **POST** /entitlements/allow | Add an entitlement for all users
[**entitlements_allow_uuid_post**](EntitlementsApi.md#entitlements_allow_uuid_post) | **POST** /entitlements/allow/{uuid} | Grant product access to a customer
[**entitlements_get**](EntitlementsApi.md#entitlements_get) | **GET** /entitlements | List all entitlements
[**entitlements_global_get**](EntitlementsApi.md#entitlements_global_get) | **GET** /entitlements/global | Lists all past and future global entitlements


# **entitlements_allow_delete**
> list[object] entitlements_allow_delete(body, auth_user=auth_user, authorization=authorization)

Remove an entitlement

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.EntitlementsApi()
body = 56 # int | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Remove an entitlement
    api_response = api_instance.entitlements_allow_delete(body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitlementsApi->entitlements_allow_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **int**|  | 
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

# **entitlements_allow_get**
> list[PersistedEntitlementAccess] entitlements_allow_get(auth_user=auth_user, authorization=authorization, ip=ip, paper=paper)

Check if global entitlements are enabled

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.EntitlementsApi()
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)
ip = 'ip_example' # str |  (optional)
paper = 'paper_example' # str |  (optional)

try:
    # Check if global entitlements are enabled
    api_response = api_instance.entitlements_allow_get(auth_user=auth_user, authorization=authorization, ip=ip, paper=paper)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitlementsApi->entitlements_allow_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **ip** | **str**|  | [optional] 
 **paper** | **str**|  | [optional] 

### Return type

[**list[PersistedEntitlementAccess]**](PersistedEntitlementAccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_allow_post**
> list[object] entitlements_allow_post(body, auth_user=auth_user, authorization=authorization)

Add an entitlement for all users

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
    # Add an entitlement for all users
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

# **entitlements_global_get**
> list[PersistedEntitlementAccess] entitlements_global_get(auth_user=auth_user, authorization=authorization)

Lists all past and future global entitlements

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.EntitlementsApi()
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Lists all past and future global entitlements
    api_response = api_instance.entitlements_global_get(auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitlementsApi->entitlements_global_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**list[PersistedEntitlementAccess]**](PersistedEntitlementAccess.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

