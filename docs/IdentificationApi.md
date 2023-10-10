# persona.IdentificationApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identification_login_get**](IdentificationApi.md#identification_login_get) | **GET** /identification/login | Authenticate with OpenID Connect
[**identification_login_return_get**](IdentificationApi.md#identification_login_return_get) | **GET** /identification/login/return | Redirect endpoint for OpenID Connect
[**identification_user_stamp_uuid_post**](IdentificationApi.md#identification_user_stamp_uuid_post) | **POST** /identification/user/stamp/{uuid} | Query when the strong identification was last updated


# **identification_login_get**
> identification_login_get()

Authenticate with OpenID Connect

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.IdentificationApi()

try:
    # Authenticate with OpenID Connect
    api_instance.identification_login_get()
except ApiException as e:
    print("Exception when calling IdentificationApi->identification_login_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identification_login_return_get**
> str identification_login_return_get(code, state, cookie, cookie2)

Redirect endpoint for OpenID Connect

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.IdentificationApi()
code = 'code_example' # str | 
state = 'state_example' # str | 
cookie = '/path/to/file' # file | 
cookie2 = '/path/to/file' # file | 

try:
    # Redirect endpoint for OpenID Connect
    api_response = api_instance.identification_login_return_get(code, state, cookie, cookie2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentificationApi->identification_login_return_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **state** | **str**|  | 
 **cookie** | **file**|  | 
 **cookie2** | **file**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identification_user_stamp_uuid_post**
> str identification_user_stamp_uuid_post(uuid, auth_user=auth_user, authorization=authorization)

Query when the strong identification was last updated

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.IdentificationApi()
uuid = 'uuid_example' # str | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Query when the strong identification was last updated
    api_response = api_instance.identification_user_stamp_uuid_post(uuid, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentificationApi->identification_user_stamp_uuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

