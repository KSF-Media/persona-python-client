# persona.AdminApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_uuid_get**](AdminApi.md#admin_uuid_get) | **GET** /admin/{uuid} | Get user by admin credentials.


# **admin_uuid_get**
> User admin_uuid_get(uuid, authorization=authorization, auth_user=auth_user, cache_control=cache_control)

Get user by admin credentials.

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.AdminApi()
uuid = 'uuid_example' # str | 
authorization = 'authorization_example' # str |  (optional)
auth_user = 'auth_user_example' # str |  (optional)
cache_control = 'cache_control_example' # str |  (optional)

try:
    # Get user by admin credentials.
    api_response = api_instance.admin_uuid_get(uuid, authorization=authorization, auth_user=auth_user, cache_control=cache_control)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **authorization** | **str**|  | [optional] 
 **auth_user** | [**str**](.md)|  | [optional] 
 **cache_control** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

