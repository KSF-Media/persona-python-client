# persona.AdminApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_search_get**](AdminApi.md#admin_search_get) | **GET** /admin/search | Search for users
[**admin_uuid_get**](AdminApi.md#admin_uuid_get) | **GET** /admin/{uuid} | Get user by admin credentials.


# **admin_search_get**
> list[User] admin_search_get(query, auth_user=auth_user, authorization=authorization)

Search for users

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.AdminApi()
query = 'query_example' # str | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Search for users
    api_response = api_instance.admin_search_get(query, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_uuid_get**
> User admin_uuid_get(uuid, auth_user=auth_user, authorization=authorization, cache_control=cache_control)

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
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)
cache_control = 'cache_control_example' # str |  (optional)

try:
    # Get user by admin credentials.
    api_response = api_instance.admin_uuid_get(uuid, auth_user=auth_user, authorization=authorization, cache_control=cache_control)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **cache_control** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

