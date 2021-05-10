# persona.AccountApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_password_forgot_post**](AccountApi.md#account_password_forgot_post) | **POST** /account/password/forgot | Request password reset link
[**account_password_reset_post**](AccountApi.md#account_password_reset_post) | **POST** /account/password/reset | Reset a forgotten password with a token


# **account_password_forgot_post**
> list[object] account_password_forgot_post(body)

Request password reset link

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.AccountApi()
body = persona.ForgotPasswordData() # ForgotPasswordData | 

try:
    # Request password reset link
    api_response = api_instance.account_password_forgot_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_password_forgot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForgotPasswordData**](ForgotPasswordData.md)|  | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_password_reset_post**
> list[object] account_password_reset_post(body)

Reset a forgotten password with a token

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.AccountApi()
body = persona.UpdatePasswordData() # UpdatePasswordData | 

try:
    # Reset a forgotten password with a token
    api_response = api_instance.account_password_reset_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_password_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePasswordData**](UpdatePasswordData.md)|  | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

