# persona.AccountApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_password_check_token_post**](AccountApi.md#account_password_check_token_post) | **POST** /account/password/check-token | Validate password reset token
[**account_password_forgot_post**](AccountApi.md#account_password_forgot_post) | **POST** /account/password/forgot | Request password reset link
[**account_password_reset_post**](AccountApi.md#account_password_reset_post) | **POST** /account/password/reset | Reset a forgotten password with a token


# **account_password_check_token_post**
> account_password_check_token_post(body)

Validate password reset token

The second step in the forgotten password reset procedure is to ensure that the password reset token is still valid. Each token can be used at most once and it is valid for a limited duration.

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.AccountApi()
body = 'body_example' # str | 

try:
    # Validate password reset token
    api_instance.account_password_check_token_post(body)
except ApiException as e:
    print("Exception when calling AccountApi->account_password_check_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_password_forgot_post**
> account_password_forgot_post(body)

Request password reset link

This is the starting point of the forgotten password recovery process. It sends a password reset link with a pasword reset token to the given user's email address if such user and email address exist.

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
    api_instance.account_password_forgot_post(body)
except ApiException as e:
    print("Exception when calling AccountApi->account_password_forgot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForgotPasswordData**](ForgotPasswordData.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_password_reset_post**
> account_password_reset_post(body)

Reset a forgotten password with a token

The final step of the forgotten password reset procedure performs password reset with a token obtained from the email message sent by the POST /password/forgot endpoint and the new password and its confirmation.

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
    api_instance.account_password_reset_post(body)
except ApiException as e:
    print("Exception when calling AccountApi->account_password_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePasswordData**](UpdatePasswordData.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

