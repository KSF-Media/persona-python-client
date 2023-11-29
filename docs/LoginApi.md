# persona.LoginApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_ip_get**](LoginApi.md#login_ip_get) | **GET** /login/ip | Login with IP
[**login_post**](LoginApi.md#login_post) | **POST** /login | Login with email and password
[**login_sso_post**](LoginApi.md#login_sso_post) | **POST** /login/sso | Disabled. Always returns 403.
[**login_uuid_delete**](LoginApi.md#login_uuid_delete) | **DELETE** /login/{uuid} | Logout


# **login_ip_get**
> LoginResponse login_ip_get(x_real_ip, paper)

Login with IP

Returns auth & token for customers with IP based entitlement

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.LoginApi()
x_real_ip = 'x_real_ip_example' # str | 
paper = 'paper_example' # str | 

try:
    # Login with IP
    api_response = api_instance.login_ip_get(x_real_ip, paper)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_ip_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_real_ip** | **str**|  | 
 **paper** | **str**|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **login_sso_post**
> LoginResponse login_sso_post(body)

Disabled. Always returns 403.

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
    # Disabled. Always returns 403.
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

