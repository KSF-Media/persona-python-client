# openapi_client.UsersApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_uuid_get**](UsersApi.md#users_uuid_get) | **GET** /users/{uuid} | Get user by UUID.


# **users_uuid_get**
> User users_uuid_get(uuid, authorization=authorization)

Get user by UUID.

Authorization header expects the following format ‘OAuth {token}’

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.UsersApi()
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

