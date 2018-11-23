# persona_client.UsersApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_uuid_gdpr_put**](UsersApi.md#users_uuid_gdpr_put) | **PUT** /users/{uuid}/gdpr | Updates the GDPR consent settings for a given user.
[**users_uuid_get**](UsersApi.md#users_uuid_get) | **GET** /users/{uuid} | Get user by UUID.


# **users_uuid_gdpr_put**
> list[object] users_uuid_gdpr_put(uuid, gdpr_consent, authorization=authorization)

Updates the GDPR consent settings for a given user.

Authorization header expects the following format ‘OAuth {token}’

### Example
```python
from __future__ import print_function
import time
import persona_client
from persona_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona_client.UsersApi()
uuid = 'uuid_example' # str | 
gdpr_consent = NULL # list[GdprConsent] | 
authorization = 'authorization_example' # str |  (optional)

try:
    # Updates the GDPR consent settings for a given user.
    api_response = api_instance.users_uuid_gdpr_put(uuid, gdpr_consent, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_gdpr_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **gdpr_consent** | [**list[GdprConsent]**](list.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_get**
> User users_uuid_get(uuid, authorization=authorization)

Get user by UUID.

Authorization header expects the following format ‘OAuth {token}’

### Example
```python
from __future__ import print_function
import time
import persona_client
from persona_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona_client.UsersApi()
uuid = 'uuid_example' # str | 
authorization = 'authorization_example' # str |  (optional)

try:
    # Get user by UUID.
    api_response = api_instance.users_uuid_get(uuid, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

