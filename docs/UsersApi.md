# persona.UsersApi

All URIs are relative to *http://http:/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_post**](UsersApi.md#users_post) | **POST** /users | Create a new user.
[**users_temporary_post**](UsersApi.md#users_temporary_post) | **POST** /users/temporary | Create a new user with email.
[**users_uuid_entitlement_get**](UsersApi.md#users_uuid_entitlement_get) | **GET** /users/{uuid}/entitlement | Get users entitlements.
[**users_uuid_gdpr_put**](UsersApi.md#users_uuid_gdpr_put) | **PUT** /users/{uuid}/gdpr | Updates the GDPR consent settings for a given user.
[**users_uuid_get**](UsersApi.md#users_uuid_get) | **GET** /users/{uuid} | Get user by UUID.
[**users_uuid_legal_put**](UsersApi.md#users_uuid_legal_put) | **PUT** /users/{uuid}/legal | Updates the legal consent settings for a given user.
[**users_uuid_newsletters_get**](UsersApi.md#users_uuid_newsletters_get) | **GET** /users/{uuid}/newsletters | Get newsletter subscriptions
[**users_uuid_newsletters_put**](UsersApi.md#users_uuid_newsletters_put) | **PUT** /users/{uuid}/newsletters | Update newsletter subscriptions
[**users_uuid_password_put**](UsersApi.md#users_uuid_password_put) | **PUT** /users/{uuid}/password | Set / Change user password
[**users_uuid_patch**](UsersApi.md#users_uuid_patch) | **PATCH** /users/{uuid} | Update a user
[**users_uuid_payments_get**](UsersApi.md#users_uuid_payments_get) | **GET** /users/{uuid}/payments | Get user&#39;s subscriptions and payment events
[**users_uuid_scope_get**](UsersApi.md#users_uuid_scope_get) | **GET** /users/{uuid}/scope | Check if user has valid token for a scope
[**users_uuid_subscriptions_subsno_address_change_delete**](UsersApi.md#users_uuid_subscriptions_subsno_address_change_delete) | **DELETE** /users/{uuid}/subscriptions/{subsno}/addressChange | Delete temporary address change for subscription
[**users_uuid_subscriptions_subsno_address_change_patch**](UsersApi.md#users_uuid_subscriptions_subsno_address_change_patch) | **PATCH** /users/{uuid}/subscriptions/{subsno}/addressChange | Edit temporary address change dates of a subscription
[**users_uuid_subscriptions_subsno_address_change_post**](UsersApi.md#users_uuid_subscriptions_subsno_address_change_post) | **POST** /users/{uuid}/subscriptions/{subsno}/addressChange | Make a temporary address change for a subscription
[**users_uuid_subscriptions_subsno_cancel_put**](UsersApi.md#users_uuid_subscriptions_subsno_cancel_put) | **PUT** /users/{uuid}/subscriptions/{subsno}/cancel | Cancels user subscription
[**users_uuid_subscriptions_subsno_pause_patch**](UsersApi.md#users_uuid_subscriptions_subsno_pause_patch) | **PATCH** /users/{uuid}/subscriptions/{subsno}/pause | Edit pause duration
[**users_uuid_subscriptions_subsno_pause_post**](UsersApi.md#users_uuid_subscriptions_subsno_pause_post) | **POST** /users/{uuid}/subscriptions/{subsno}/pause | Pause users subscription
[**users_uuid_subscriptions_subsno_reclamation_post**](UsersApi.md#users_uuid_subscriptions_subsno_reclamation_post) | **POST** /users/{uuid}/subscriptions/{subsno}/reclamation | Create a new delivery reclamation for a subscription
[**users_uuid_subscriptions_subsno_reclamations_reclaimno_get**](UsersApi.md#users_uuid_subscriptions_subsno_reclamations_reclaimno_get) | **GET** /users/{uuid}/subscriptions/{subsno}/reclamations/{reclaimno} | Get a delivery reclamation
[**users_uuid_subscriptions_subsno_unpause_post**](UsersApi.md#users_uuid_subscriptions_subsno_unpause_post) | **POST** /users/{uuid}/subscriptions/{subsno}/unpause | Unpause users subscription


# **users_post**
> LoginResponse users_post(body)

Create a new user.

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
body = persona.NewUser() # NewUser | 

try:
    # Create a new user.
    api_response = api_instance.users_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewUser**](NewUser.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_temporary_post**
> LoginResponse users_temporary_post(body)

Create a new user with email.

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
body = persona.NewTemporaryUser() # NewTemporaryUser | 

try:
    # Create a new user with email.
    api_response = api_instance.users_temporary_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_temporary_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewTemporaryUser**](NewTemporaryUser.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_entitlement_get**
> list[str] users_uuid_entitlement_get(uuid, auth_user=auth_user, authorization=authorization, cache_control=cache_control)

Get users entitlements.

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)
cache_control = 'cache_control_example' # str |  (optional)

try:
    # Get users entitlements.
    api_response = api_instance.users_uuid_entitlement_get(uuid, auth_user=auth_user, authorization=authorization, cache_control=cache_control)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_entitlement_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **cache_control** | **str**|  | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_gdpr_put**
> User users_uuid_gdpr_put(uuid, body, auth_user=auth_user, authorization=authorization)

Updates the GDPR consent settings for a given user.

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
body = None # list[GdprConsent] | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Updates the GDPR consent settings for a given user.
    api_response = api_instance.users_uuid_gdpr_put(uuid, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_gdpr_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **body** | [**list[GdprConsent]**](list.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_get**
> User users_uuid_get(uuid, auth_user=auth_user, authorization=authorization, cache_control=cache_control)

Get user by UUID.

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)
cache_control = 'cache_control_example' # str |  (optional)

try:
    # Get user by UUID.
    api_response = api_instance.users_uuid_get(uuid, auth_user=auth_user, authorization=authorization, cache_control=cache_control)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **cache_control** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_legal_put**
> User users_uuid_legal_put(uuid, body, auth_user=auth_user, authorization=authorization)

Updates the legal consent settings for a given user.

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
body = None # list[LegalConsent] | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Updates the legal consent settings for a given user.
    api_response = api_instance.users_uuid_legal_put(uuid, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_legal_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **body** | [**list[LegalConsent]**](list.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_newsletters_get**
> list[Newsletter] users_uuid_newsletters_get(uuid, auth_user=auth_user, authorization=authorization)

Get newsletter subscriptions

Get list of newsletter subscriptions from mailchimp

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Get newsletter subscriptions
    api_response = api_instance.users_uuid_newsletters_get(uuid, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_newsletters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**list[Newsletter]**](Newsletter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_newsletters_put**
> list[Newsletter] users_uuid_newsletters_put(uuid, body, auth_user=auth_user, authorization=authorization)

Update newsletter subscriptions

Get list of newsletter subscriptions from mailchimp

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
body = None # list[Newsletter] | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Update newsletter subscriptions
    api_response = api_instance.users_uuid_newsletters_put(uuid, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_newsletters_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **body** | [**list[Newsletter]**](list.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**list[Newsletter]**](Newsletter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_password_put**
> User users_uuid_password_put(uuid, body, auth_user=auth_user, authorization=authorization)

Set / Change user password

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
body = persona.UserUpdatePassword() # UserUpdatePassword | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Set / Change user password
    api_response = api_instance.users_uuid_password_put(uuid, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_password_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **body** | [**UserUpdatePassword**](UserUpdatePassword.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_patch**
> User users_uuid_patch(uuid, body, auth_user=auth_user, authorization=authorization)

Update a user

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
body = persona.UserUpdate() # UserUpdate | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Update a user
    api_response = api_instance.users_uuid_patch(uuid, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **body** | [**UserUpdate**](UserUpdate.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_payments_get**
> list[SubscriptionPayments] users_uuid_payments_get(uuid, auth_user=auth_user, authorization=authorization)

Get user's subscriptions and payment events

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Get user's subscriptions and payment events
    api_response = api_instance.users_uuid_payments_get(uuid, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_payments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**list[SubscriptionPayments]**](SubscriptionPayments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_scope_get**
> int users_uuid_scope_get(uuid, scope, authorization=authorization)

Check if user has valid token for a scope

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
scope = 'scope_example' # str | 
authorization = 'authorization_example' # str |  (optional)

try:
    # Check if user has valid token for a scope
    api_response = api_instance.users_uuid_scope_get(uuid, scope, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_scope_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **scope** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_subscriptions_subsno_address_change_delete**
> Subscription users_uuid_subscriptions_subsno_address_change_delete(uuid, subsno, body, auth_user=auth_user, authorization=authorization)

Delete temporary address change for subscription

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
subsno = 56 # int | 
body = persona.DeleteTempAddressChangeDates() # DeleteTempAddressChangeDates | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Delete temporary address change for subscription
    api_response = api_instance.users_uuid_subscriptions_subsno_address_change_delete(uuid, subsno, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_subscriptions_subsno_address_change_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **subsno** | **int**|  | 
 **body** | [**DeleteTempAddressChangeDates**](DeleteTempAddressChangeDates.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_subscriptions_subsno_address_change_patch**
> Subscription users_uuid_subscriptions_subsno_address_change_patch(uuid, subsno, body, auth_user=auth_user, authorization=authorization)

Edit temporary address change dates of a subscription

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
subsno = 56 # int | 
body = persona.TemporaryAddressChangeDates() # TemporaryAddressChangeDates | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Edit temporary address change dates of a subscription
    api_response = api_instance.users_uuid_subscriptions_subsno_address_change_patch(uuid, subsno, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_subscriptions_subsno_address_change_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **subsno** | **int**|  | 
 **body** | [**TemporaryAddressChangeDates**](TemporaryAddressChangeDates.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_subscriptions_subsno_address_change_post**
> Subscription users_uuid_subscriptions_subsno_address_change_post(uuid, subsno, body, auth_user=auth_user, authorization=authorization)

Make a temporary address change for a subscription

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
subsno = 56 # int | 
body = persona.TemporaryAddressChange() # TemporaryAddressChange | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Make a temporary address change for a subscription
    api_response = api_instance.users_uuid_subscriptions_subsno_address_change_post(uuid, subsno, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_subscriptions_subsno_address_change_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **subsno** | **int**|  | 
 **body** | [**TemporaryAddressChange**](TemporaryAddressChange.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_subscriptions_subsno_cancel_put**
> Subscription users_uuid_subscriptions_subsno_cancel_put(uuid, subsno, body, auth_user=auth_user, authorization=authorization)

Cancels user subscription

The subscription continues to be valid until the end of the billing period. Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
subsno = 56 # int | 
body = persona.CancelSubscriptionReason() # CancelSubscriptionReason | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Cancels user subscription
    api_response = api_instance.users_uuid_subscriptions_subsno_cancel_put(uuid, subsno, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_subscriptions_subsno_cancel_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **subsno** | **int**|  | 
 **body** | [**CancelSubscriptionReason**](CancelSubscriptionReason.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_subscriptions_subsno_pause_patch**
> Subscription users_uuid_subscriptions_subsno_pause_patch(uuid, subsno, body, auth_user=auth_user, authorization=authorization)

Edit pause duration

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
subsno = 56 # int | 
body = persona.SubscriptionPauseEdit() # SubscriptionPauseEdit | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Edit pause duration
    api_response = api_instance.users_uuid_subscriptions_subsno_pause_patch(uuid, subsno, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_subscriptions_subsno_pause_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **subsno** | **int**|  | 
 **body** | [**SubscriptionPauseEdit**](SubscriptionPauseEdit.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_subscriptions_subsno_pause_post**
> Subscription users_uuid_subscriptions_subsno_pause_post(uuid, subsno, body, auth_user=auth_user, authorization=authorization)

Pause users subscription

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
subsno = 56 # int | 
body = persona.SubscriptionPauseDates() # SubscriptionPauseDates | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Pause users subscription
    api_response = api_instance.users_uuid_subscriptions_subsno_pause_post(uuid, subsno, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_subscriptions_subsno_pause_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **subsno** | **int**|  | 
 **body** | [**SubscriptionPauseDates**](SubscriptionPauseDates.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_subscriptions_subsno_reclamation_post**
> DeliveryReclamation users_uuid_subscriptions_subsno_reclamation_post(uuid, subsno, body, auth_user=auth_user, authorization=authorization)

Create a new delivery reclamation for a subscription

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
subsno = 56 # int | 
body = persona.NewDeliveryReclamation() # NewDeliveryReclamation | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Create a new delivery reclamation for a subscription
    api_response = api_instance.users_uuid_subscriptions_subsno_reclamation_post(uuid, subsno, body, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_subscriptions_subsno_reclamation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **subsno** | **int**|  | 
 **body** | [**NewDeliveryReclamation**](NewDeliveryReclamation.md)|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**DeliveryReclamation**](DeliveryReclamation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_subscriptions_subsno_reclamations_reclaimno_get**
> DeliveryReclamation users_uuid_subscriptions_subsno_reclamations_reclaimno_get(uuid, subsno, reclaimno, auth_user=auth_user, authorization=authorization)

Get a delivery reclamation

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
subsno = 56 # int | 
reclaimno = 56 # int | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Get a delivery reclamation
    api_response = api_instance.users_uuid_subscriptions_subsno_reclamations_reclaimno_get(uuid, subsno, reclaimno, auth_user=auth_user, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_subscriptions_subsno_reclamations_reclaimno_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **subsno** | **int**|  | 
 **reclaimno** | **int**|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**DeliveryReclamation**](DeliveryReclamation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_subscriptions_subsno_unpause_post**
> Subscription users_uuid_subscriptions_subsno_unpause_post(uuid, subsno, auth_user=auth_user, authorization=authorization, start_date=start_date, end_date=end_date)

Unpause users subscription

Authorization header expects the following format ‘OAuth {token}’

### Example

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = persona.UsersApi()
uuid = 'uuid_example' # str | 
subsno = 56 # int | 
auth_user = 'auth_user_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)
start_date = '2013-10-20' # date |  (optional)
end_date = '2013-10-20' # date |  (optional)

try:
    # Unpause users subscription
    api_response = api_instance.users_uuid_subscriptions_subsno_unpause_post(uuid, subsno, auth_user=auth_user, authorization=authorization, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_subscriptions_subsno_unpause_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **subsno** | **int**|  | 
 **auth_user** | [**str**](.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

