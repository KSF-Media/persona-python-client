# openapi_client.LoginApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_post**](LoginApi.md#login_post) | **POST** /login | Login with email and password
[**login_some_post**](LoginApi.md#login_some_post) | **POST** /login/some | Login with social media
[**login_sso_post**](LoginApi.md#login_sso_post) | **POST** /login/sso | Login with the AccessToken given by the SSO auth


# **login_post**
> LoginResponse login_post(login_data)

Login with email and password

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.LoginApi()
login_data = openapi_client.LoginData() # LoginData | 

try:
    # Login with email and password
    api_response = api_instance.login_post(login_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_data** | [**LoginData**](LoginData.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_some_post**
> LoginResponse login_some_post(login_data_so_me)

Login with social media

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.LoginApi()
login_data_so_me = openapi_client.LoginDataSoMe() # LoginDataSoMe | 

try:
    # Login with social media
    api_response = api_instance.login_some_post(login_data_so_me)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_some_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_data_so_me** | [**LoginDataSoMe**](LoginDataSoMe.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_sso_post**
> LoginResponse login_sso_post(login_data_sso)

Login with the AccessToken given by the SSO auth

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.LoginApi()
login_data_sso = openapi_client.LoginDataSSO() # LoginDataSSO | 

try:
    # Login with the AccessToken given by the SSO auth
    api_response = api_instance.login_sso_post(login_data_sso)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_sso_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_data_sso** | [**LoginDataSSO**](LoginDataSSO.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

