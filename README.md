# persona
KSF Media unified login service

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.3.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/KSF-Media/persona-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/KSF-Media/persona-python-client.git`)

Then import the package:
```python
import persona 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import persona
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import persona
from persona.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = persona.AccountApi(persona.ApiClient(configuration))
email = 'email_example' # str | 
redir = True # bool |  (optional)

try:
    # Request password reset link
    api_response = api_instance.account_password_forgot_get(email, redir=redir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_password_forgot_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://http:/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**account_password_forgot_get**](docs/AccountApi.md#account_password_forgot_get) | **GET** /account/password/forgot | Request password reset link
*AccountApi* | [**account_password_forgot_post**](docs/AccountApi.md#account_password_forgot_post) | **POST** /account/password/forgot | Request password reset link
*AccountApi* | [**account_password_reset_post**](docs/AccountApi.md#account_password_reset_post) | **POST** /account/password/reset | Reset a forgotten password with a token
*AdminApi* | [**admin_search_post**](docs/AdminApi.md#admin_search_post) | **POST** /admin/search | Search for users
*AdminApi* | [**admin_user_post**](docs/AdminApi.md#admin_user_post) | **POST** /admin/user | Create a new user with admin options.
*EntitlementsApi* | [**entitlements_allow_delete**](docs/EntitlementsApi.md#entitlements_allow_delete) | **DELETE** /entitlements/allow | Remove an entitlement
*EntitlementsApi* | [**entitlements_allow_get**](docs/EntitlementsApi.md#entitlements_allow_get) | **GET** /entitlements/allow | Check if global entitlements are enabled
*EntitlementsApi* | [**entitlements_allow_post**](docs/EntitlementsApi.md#entitlements_allow_post) | **POST** /entitlements/allow | Add an entitlement for all users
*EntitlementsApi* | [**entitlements_allow_uuid_post**](docs/EntitlementsApi.md#entitlements_allow_uuid_post) | **POST** /entitlements/allow/{uuid} | Grant product access to a customer
*EntitlementsApi* | [**entitlements_get**](docs/EntitlementsApi.md#entitlements_get) | **GET** /entitlements | List all entitlements
*LoginApi* | [**login_ip_get**](docs/LoginApi.md#login_ip_get) | **GET** /login/ip | Login with IP
*LoginApi* | [**login_post**](docs/LoginApi.md#login_post) | **POST** /login | Login with email and password
*LoginApi* | [**login_some_post**](docs/LoginApi.md#login_some_post) | **POST** /login/some | Login with social media
*LoginApi* | [**login_sso_post**](docs/LoginApi.md#login_sso_post) | **POST** /login/sso | Login with the AccessToken given by the SSO auth
*LoginApi* | [**login_uuid_delete**](docs/LoginApi.md#login_uuid_delete) | **DELETE** /login/{uuid} | Logout
*UsersApi* | [**users_post**](docs/UsersApi.md#users_post) | **POST** /users | Create a new user.
*UsersApi* | [**users_temporary_post**](docs/UsersApi.md#users_temporary_post) | **POST** /users/temporary | Create a new user with email.
*UsersApi* | [**users_uuid_entitlement_get**](docs/UsersApi.md#users_uuid_entitlement_get) | **GET** /users/{uuid}/entitlement | Get users entitlements.
*UsersApi* | [**users_uuid_gdpr_put**](docs/UsersApi.md#users_uuid_gdpr_put) | **PUT** /users/{uuid}/gdpr | Updates the GDPR consent settings for a given user.
*UsersApi* | [**users_uuid_get**](docs/UsersApi.md#users_uuid_get) | **GET** /users/{uuid} | Get user by UUID.
*UsersApi* | [**users_uuid_legal_put**](docs/UsersApi.md#users_uuid_legal_put) | **PUT** /users/{uuid}/legal | Updates the legal consent settings for a given user.
*UsersApi* | [**users_uuid_newsletters_get**](docs/UsersApi.md#users_uuid_newsletters_get) | **GET** /users/{uuid}/newsletters | Get newsletter subscriptions
*UsersApi* | [**users_uuid_newsletters_put**](docs/UsersApi.md#users_uuid_newsletters_put) | **PUT** /users/{uuid}/newsletters | Update newsletter subscriptions
*UsersApi* | [**users_uuid_password_put**](docs/UsersApi.md#users_uuid_password_put) | **PUT** /users/{uuid}/password | Set / Change user password
*UsersApi* | [**users_uuid_patch**](docs/UsersApi.md#users_uuid_patch) | **PATCH** /users/{uuid} | Update a user
*UsersApi* | [**users_uuid_payments_get**](docs/UsersApi.md#users_uuid_payments_get) | **GET** /users/{uuid}/payments | Get user&#39;s subscriptions and payment events
*UsersApi* | [**users_uuid_scope_get**](docs/UsersApi.md#users_uuid_scope_get) | **GET** /users/{uuid}/scope | Check if user has valid token for a scope
*UsersApi* | [**users_uuid_subscriptions_subsno_address_change_delete**](docs/UsersApi.md#users_uuid_subscriptions_subsno_address_change_delete) | **DELETE** /users/{uuid}/subscriptions/{subsno}/addressChange | Delete temporary address change for subscription
*UsersApi* | [**users_uuid_subscriptions_subsno_address_change_patch**](docs/UsersApi.md#users_uuid_subscriptions_subsno_address_change_patch) | **PATCH** /users/{uuid}/subscriptions/{subsno}/addressChange | Edit temporary address change dates of a subscription
*UsersApi* | [**users_uuid_subscriptions_subsno_address_change_post**](docs/UsersApi.md#users_uuid_subscriptions_subsno_address_change_post) | **POST** /users/{uuid}/subscriptions/{subsno}/addressChange | Make a temporary address change for a subscription
*UsersApi* | [**users_uuid_subscriptions_subsno_cancel_put**](docs/UsersApi.md#users_uuid_subscriptions_subsno_cancel_put) | **PUT** /users/{uuid}/subscriptions/{subsno}/cancel | Cancels user subscription
*UsersApi* | [**users_uuid_subscriptions_subsno_pause_patch**](docs/UsersApi.md#users_uuid_subscriptions_subsno_pause_patch) | **PATCH** /users/{uuid}/subscriptions/{subsno}/pause | Edit pause duration
*UsersApi* | [**users_uuid_subscriptions_subsno_pause_post**](docs/UsersApi.md#users_uuid_subscriptions_subsno_pause_post) | **POST** /users/{uuid}/subscriptions/{subsno}/pause | Pause users subscription
*UsersApi* | [**users_uuid_subscriptions_subsno_reclamation_post**](docs/UsersApi.md#users_uuid_subscriptions_subsno_reclamation_post) | **POST** /users/{uuid}/subscriptions/{subsno}/reclamation | Create a new delivery reclamation for a subscription
*UsersApi* | [**users_uuid_subscriptions_subsno_reclamations_reclaimno_get**](docs/UsersApi.md#users_uuid_subscriptions_subsno_reclamations_reclaimno_get) | **GET** /users/{uuid}/subscriptions/{subsno}/reclamations/{reclaimno} | Get a delivery reclamation
*UsersApi* | [**users_uuid_subscriptions_subsno_unpause_post**](docs/UsersApi.md#users_uuid_subscriptions_subsno_unpause_post) | **POST** /users/{uuid}/subscriptions/{subsno}/unpause | Unpause users subscription


## Documentation For Models

 - [ActiveDays](docs/ActiveDays.md)
 - [Address](docs/Address.md)
 - [AdminNewUser](docs/AdminNewUser.md)
 - [CancelSubscriptionReason](docs/CancelSubscriptionReason.md)
 - [DeleteTempAddressChangeDates](docs/DeleteTempAddressChangeDates.md)
 - [DeliveryAddress](docs/DeliveryAddress.md)
 - [DeliveryReclamation](docs/DeliveryReclamation.md)
 - [EntitlementAccess](docs/EntitlementAccess.md)
 - [FaroUser](docs/FaroUser.md)
 - [ForgotPasswordData](docs/ForgotPasswordData.md)
 - [GdprConsent](docs/GdprConsent.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [InlineResponse400InvalidRequestBody](docs/InlineResponse400InvalidRequestBody.md)
 - [InlineResponse403](docs/InlineResponse403.md)
 - [InlineResponse4031](docs/InlineResponse4031.md)
 - [InlineResponse4031AccessTokenExpired](docs/InlineResponse4031AccessTokenExpired.md)
 - [InlineResponse4032](docs/InlineResponse4032.md)
 - [InlineResponse4032EmailAddressInUse](docs/InlineResponse4032EmailAddressInUse.md)
 - [InlineResponse4032EmailNotAuthorized](docs/InlineResponse4032EmailNotAuthorized.md)
 - [InlineResponse4032OauthFailed](docs/InlineResponse4032OauthFailed.md)
 - [InlineResponse403InvalidCredentials](docs/InlineResponse403InvalidCredentials.md)
 - [InlineResponse415](docs/InlineResponse415.md)
 - [InlineResponse415UnsupportedMediaType](docs/InlineResponse415UnsupportedMediaType.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [InlineResponse500InternalServerError](docs/InlineResponse500InternalServerError.md)
 - [JanrainUser](docs/JanrainUser.md)
 - [LegalConsent](docs/LegalConsent.md)
 - [LoginData](docs/LoginData.md)
 - [LoginDataSSO](docs/LoginDataSSO.md)
 - [LoginDataSoMe](docs/LoginDataSoMe.md)
 - [LoginResponse](docs/LoginResponse.md)
 - [NewDeliveryReclamation](docs/NewDeliveryReclamation.md)
 - [NewTemporaryUser](docs/NewTemporaryUser.md)
 - [NewUser](docs/NewUser.md)
 - [NewsletterSubscriptions](docs/NewsletterSubscriptions.md)
 - [Package](docs/Package.md)
 - [PackageCampaign](docs/PackageCampaign.md)
 - [PackageOffer](docs/PackageOffer.md)
 - [Paper](docs/Paper.md)
 - [PastTemporaryAddress](docs/PastTemporaryAddress.md)
 - [PausedSubscription](docs/PausedSubscription.md)
 - [Payment](docs/Payment.md)
 - [PendingAddressChange](docs/PendingAddressChange.md)
 - [PersistedEntitlementAccess](docs/PersistedEntitlementAccess.md)
 - [Product](docs/Product.md)
 - [SearchQuery](docs/SearchQuery.md)
 - [SearchResult](docs/SearchResult.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionDates](docs/SubscriptionDates.md)
 - [SubscriptionPauseDates](docs/SubscriptionPauseDates.md)
 - [SubscriptionPauseEdit](docs/SubscriptionPauseEdit.md)
 - [SubscriptionPayments](docs/SubscriptionPayments.md)
 - [TemporaryAddressChange](docs/TemporaryAddressChange.md)
 - [TemporaryAddressChangeDates](docs/TemporaryAddressChangeDates.md)
 - [UpdatePasswordData](docs/UpdatePasswordData.md)
 - [User](docs/User.md)
 - [UserUpdate](docs/UserUpdate.md)
 - [UserUpdateAddress](docs/UserUpdateAddress.md)
 - [UserUpdatePassword](docs/UserUpdatePassword.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




