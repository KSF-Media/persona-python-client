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
[**users_uuid_password_put**](UsersApi.md#users_uuid_password_put) | **PUT** /users/{uuid}/password | Set / Change user password
[**users_uuid_patch**](UsersApi.md#users_uuid_patch) | **PATCH** /users/{uuid} | Update a user
[**users_uuid_subscriptions_subsno_address_change_post**](UsersApi.md#users_uuid_subscriptions_subsno_address_change_post) | **POST** /users/{uuid}/subscriptions/{subsno}/addressChange | Make a temporary address change for a subscription
[**users_uuid_subscriptions_subsno_pause_post**](UsersApi.md#users_uuid_subscriptions_subsno_pause_post) | **POST** /users/{uuid}/subscriptions/{subsno}/pause | Pause users subscription
[**users_uuid_subscriptions_subsno_reclamation_post**](UsersApi.md#users_uuid_subscriptions_subsno_reclamation_post) | **POST** /users/{uuid}/subscriptions/{subsno}/reclamation | Create a new delivery reclamation for a subscription
[**users_uuid_subscriptions_subsno_reclamations_reclaimno_get**](UsersApi.md#users_uuid_subscriptions_subsno_reclamations_reclaimno_get) | **GET** /users/{uuid}/subscriptions/{subsno}/reclamations/{reclaimno} | Get a delivery reclamation


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
> list[str] users_uuid_entitlement_get(uuid, authorization=authorization, cache_control=cache_control)

Get users entitlements.

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
authorization = 'authorization_example' # str |  (optional)
cache_control = 'cache_control_example' # str |  (optional)

try:
    # Get users entitlements.
    api_response = api_instance.users_uuid_entitlement_get(uuid, authorization=authorization, cache_control=cache_control)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_entitlement_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
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
> User users_uuid_gdpr_put(uuid, body, authorization=authorization)

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
authorization = 'authorization_example' # str |  (optional)

try:
    # Updates the GDPR consent settings for a given user.
    api_response = api_instance.users_uuid_gdpr_put(uuid, body, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_gdpr_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **body** | [**list[GdprConsent]**](list.md)|  | 
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
> User users_uuid_get(uuid, authorization=authorization, cache_control=cache_control)

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
authorization = 'authorization_example' # str |  (optional)
cache_control = 'cache_control_example' # str |  (optional)

try:
    # Get user by UUID.
    api_response = api_instance.users_uuid_get(uuid, authorization=authorization, cache_control=cache_control)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
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
> User users_uuid_legal_put(uuid, body, authorization=authorization)

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
authorization = 'authorization_example' # str |  (optional)

try:
    # Updates the legal consent settings for a given user.
    api_response = api_instance.users_uuid_legal_put(uuid, body, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_legal_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **body** | [**list[LegalConsent]**](list.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_password_put**
> User users_uuid_password_put(uuid, body, authorization=authorization)

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
authorization = 'authorization_example' # str |  (optional)

try:
    # Set / Change user password
    api_response = api_instance.users_uuid_password_put(uuid, body, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_password_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **body** | [**UserUpdatePassword**](UserUpdatePassword.md)|  | 
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
> User users_uuid_patch(uuid, body, authorization=authorization)

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
authorization = 'authorization_example' # str |  (optional)

try:
    # Update a user
    api_response = api_instance.users_uuid_patch(uuid, body, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_uuid_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)|  | 
 **body** | [**UserUpdate**](UserUpdate.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_uuid_subscriptions_subsno_address_change_post**
> Subscription users_uuid_subscriptions_subsno_address_change_post(uuid, subsno, body, authorization=authorization)

Make a temporary address change for a subscription

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
authorization = 'authorization_example' # str |  (optional)

try:
    # Make a temporary address change for a subscription
    api_response = api_instance.users_uuid_subscriptions_subsno_address_change_post(uuid, subsno, body, authorization=authorization)
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
> Subscription users_uuid_subscriptions_subsno_pause_post(uuid, subsno, body, authorization=authorization)

Pause users subscription

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
authorization = 'authorization_example' # str |  (optional)

try:
    # Pause users subscription
    api_response = api_instance.users_uuid_subscriptions_subsno_pause_post(uuid, subsno, body, authorization=authorization)
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
> DeliveryReclamation users_uuid_subscriptions_subsno_reclamation_post(uuid, subsno, body, authorization=authorization)

Create a new delivery reclamation for a subscription

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
authorization = 'authorization_example' # str |  (optional)

try:
    # Create a new delivery reclamation for a subscription
    api_response = api_instance.users_uuid_subscriptions_subsno_reclamation_post(uuid, subsno, body, authorization=authorization)
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
> DeliveryReclamation users_uuid_subscriptions_subsno_reclamations_reclaimno_get(uuid, subsno, reclaimno, authorization=authorization)

Get a delivery reclamation

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
authorization = 'authorization_example' # str |  (optional)

try:
    # Get a delivery reclamation
    api_response = api_instance.users_uuid_subscriptions_subsno_reclamations_reclaimno_get(uuid, subsno, reclaimno, authorization=authorization)
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
 **authorization** | **str**|  | [optional] 

### Return type

[**DeliveryReclamation**](DeliveryReclamation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

