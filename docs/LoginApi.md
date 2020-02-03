# persona.LoginApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_post**](LoginApi.md#login_post) | **POST** /login | Login with email and password
[**login_some_post**](LoginApi.md#login_some_post) | **POST** /login/some | Login with social media
[**login_sso_post**](LoginApi.md#login_sso_post) | **POST** /login/sso | Login with the AccessToken given by the SSO auth
[**login_uuid_delete**](LoginApi.md#login_uuid_delete) | **DELETE** /login/{uuid} | Logout


# **login_post**
> LoginResponse login_post(body)

Login with email and password

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.LoginApi()
body = persona.LoginData() # LoginData | 

try:
    # Login with email and password
    api_response = api_instance.login_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginData**](LoginData.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_some_post**
> LoginResponse login_some_post(body)

Login with social media

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.LoginApi()
body = persona.LoginDataSoMe() # LoginDataSoMe | 

try:
    # Login with social media
    api_response = api_instance.login_some_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_some_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginDataSoMe**](LoginDataSoMe.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_sso_post**
> LoginResponse login_sso_post(body)

Login with the AccessToken given by the SSO auth

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.LoginApi()
body = persona.LoginDataSSO() # LoginDataSSO | 

try:
    # Login with the AccessToken given by the SSO auth
    api_response = api_instance.login_sso_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_sso_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginDataSSO**](LoginDataSSO.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_uuid_delete**
> list[object] login_uuid_delete(uuid, authorization=authorization, everywhere=everywhere)

Logout

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.LoginApi()
uuid = 'uuid_example' # str | 
authorization = 'authorization_example' # str |  (optional)
everywhere = False # bool |  (optional) (default to False)

try:
    # Logout
    api_response = api_instance.login_uuid_delete(uuid, authorization=authorization, everywhere=everywhere)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_uuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **authorization** | **str**|  | [optional] 
 **everywhere** | **bool**|  | [optional] [default to False]

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

