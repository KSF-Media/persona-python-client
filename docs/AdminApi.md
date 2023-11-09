# persona.AdminApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_free_pass_delete**](AdminApi.md#admin_free_pass_delete) | **DELETE** /admin/free-pass | Revokes an existing free pass
[**admin_free_pass_put**](AdminApi.md#admin_free_pass_put) | **PUT** /admin/free-pass | Creates a free pass to an article
[**admin_free_passes_get**](AdminApi.md#admin_free_passes_get) | **GET** /admin/free-passes | Lists all free passes
[**admin_search_post**](AdminApi.md#admin_search_post) | **POST** /admin/search | Search for users
[**admin_transfer_passive_subscribers_listid_post**](AdminApi.md#admin_transfer_passive_subscribers_listid_post) | **POST** /admin/transfer-passive-subscribers/{listid} | Transfers passive customers from Kayak to Mailchimp
[**admin_user_post**](AdminApi.md#admin_user_post) | **POST** /admin/user | Create a new user with admin options.


# **admin_free_pass_delete**
> admin_free_pass_delete(body, auth_user=auth_user, authorization=authorization)

Revokes an existing free pass

Marks a free pass as being revoked so that it can't be used anymore. Currently, revoked free passes can't be reinstated through Persona API (though it's possible to do so with an SQL query).

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.AdminApi()
body = 'body_example' # str | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Revokes an existing free pass
    api_instance.admin_free_pass_delete(body, auth_user=auth_user, authorization=authorization)
except ApiException as e:
    print("Exception when calling AdminApi->admin_free_pass_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_free_pass_put**
> str admin_free_pass_put(body, auth_user=auth_user, authorization=authorization)

Creates a free pass to an article

Free passes can be used to temporarily bypass the paywall for individual articles.

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.AdminApi()
body = persona.FreePassInput() # FreePassInput | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Creates a free pass to an article
    api_response = api_instance.admin_free_pass_put(body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_free_pass_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FreePassInput**](FreePassInput.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_free_passes_get**
> list[FreePass] admin_free_passes_get(auth_user=auth_user, authorization=authorization)

Lists all free passes

This end point returns the list of all free passes, including those that have been expired or revoked.

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.AdminApi()
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Lists all free passes
    api_response = api_instance.admin_free_passes_get(auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_free_passes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**list[FreePass]**](FreePass.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_search_post**
> list[SearchResult] admin_search_post(body, auth_user=auth_user, authorization=authorization)

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
body = persona.SearchQuery() # SearchQuery | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Search for users
    api_response = api_instance.admin_search_post(body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchQuery**](SearchQuery.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**list[SearchResult]**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_transfer_passive_subscribers_listid_post**
> object admin_transfer_passive_subscribers_listid_post(listid, auth_user=auth_user, authorization=authorization)

Transfers passive customers from Kayak to Mailchimp

Passive subscribers/members/customers are users who don't have active entitlements and haven't opted out from email marketing. For the given list (audience) ID, this endpoint transfers the list of passive subscribers from Kayak to Mailchimp (via Faro).

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.AdminApi()
listid = 'listid_example' # str | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Transfers passive customers from Kayak to Mailchimp
    api_response = api_instance.admin_transfer_passive_subscribers_listid_post(listid, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_transfer_passive_subscribers_listid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listid** | **str**|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_user_post**
> LoginResponse admin_user_post(body, auth_user=auth_user, authorization=authorization)

Create a new user with admin options.

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.AdminApi()
body = persona.AdminNewUser() # AdminNewUser | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Create a new user with admin options.
    api_response = api_instance.admin_user_post(body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdminNewUser**](AdminNewUser.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

