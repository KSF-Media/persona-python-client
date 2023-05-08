# persona.AdminApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_search_post**](AdminApi.md#admin_search_post) | **POST** /admin/search | Search for users
[**admin_transfer_passive_subscribers_listid_post**](AdminApi.md#admin_transfer_passive_subscribers_listid_post) | **POST** /admin/transfer-passive-subscribers/{listid} | Transfers passive customers from Kayak to Mailchimp
[**admin_user_post**](AdminApi.md#admin_user_post) | **POST** /admin/user | Create a new user with admin options.


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

