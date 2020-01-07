# persona.AccountApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_code_for_token_post**](AccountApi.md#account_code_for_token_post) | **POST** /account/codeForToken | Get a password reset token
[**account_forgot_pass_post**](AccountApi.md#account_forgot_pass_post) | **POST** /account/forgotPass | Forgot Password
[**account_reset_forgotten_password_post**](AccountApi.md#account_reset_forgotten_password_post) | **POST** /account/resetForgottenPassword | Reset a forgotten password with a token


# **account_code_for_token_post**
> TokenResponse account_code_for_token_post(body)

Get a password reset token

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.AccountApi()
body = persona.CodeForTokenData() # CodeForTokenData | 

try:
    # Get a password reset token
    api_response = api_instance.account_code_for_token_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_code_for_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CodeForTokenData**](CodeForTokenData.md)|  | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_forgot_pass_post**
> ForgotPasswordResponse account_forgot_pass_post(body)

Forgot Password

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
    # Forgot Password
    api_response = api_instance.account_forgot_pass_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_forgot_pass_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForgotPasswordData**](ForgotPasswordData.md)|  | 

### Return type

[**ForgotPasswordResponse**](ForgotPasswordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_reset_forgotten_password_post**
> ForgotPasswordResponse account_reset_forgotten_password_post(body)

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
    api_response = api_instance.account_reset_forgotten_password_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_reset_forgotten_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePasswordData**](UpdatePasswordData.md)|  | 

### Return type

[**ForgotPasswordResponse**](ForgotPasswordResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

