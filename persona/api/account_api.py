# coding: utf-8

"""
    Persona

    KSF Media unified login service  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from persona.api_client import ApiClient
from persona.exceptions import (
    ApiTypeError,
    ApiValueError
)


class AccountApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def account_password_check_token_post(self, body, **kwargs):  # noqa: E501
        """Validate password reset token  # noqa: E501

        The second step in the forgotten password reset procedure is to ensure that the password reset token is still valid. Each token can be used at most once and it is valid for a limited duration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_password_check_token_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_password_check_token_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.account_password_check_token_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def account_password_check_token_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Validate password reset token  # noqa: E501

        The second step in the forgotten password reset procedure is to ensure that the password reset token is still valid. Each token can be used at most once and it is valid for a limited duration.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_password_check_token_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_password_check_token_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in local_var_params or
                local_var_params['body'] is None):
            raise ApiValueError("Missing the required parameter `body` when calling `account_password_check_token_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/account/password/check-token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_password_forgot_post(self, body, **kwargs):  # noqa: E501
        """Request password reset link  # noqa: E501

        This is the starting point of the forgotten password recovery process. It sends a password reset link with a pasword reset token to the given user's email address if such user and email address exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_password_forgot_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ForgotPasswordData body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_password_forgot_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.account_password_forgot_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def account_password_forgot_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Request password reset link  # noqa: E501

        This is the starting point of the forgotten password recovery process. It sends a password reset link with a pasword reset token to the given user's email address if such user and email address exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_password_forgot_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ForgotPasswordData body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_password_forgot_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in local_var_params or
                local_var_params['body'] is None):
            raise ApiValueError("Missing the required parameter `body` when calling `account_password_forgot_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/account/password/forgot', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_password_reset_post(self, body, **kwargs):  # noqa: E501
        """Reset a forgotten password with a token  # noqa: E501

        The final step of the forgotten password reset procedure performs password reset with a token obtained from the email message sent by the POST /password/forgot endpoint and the new password and its confirmation. If @password@ or @confirmPassword@ are missing, then this endpoint performs a mere token validation like the @/password/check-token@ endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_password_reset_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePasswordData body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_password_reset_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.account_password_reset_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def account_password_reset_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Reset a forgotten password with a token  # noqa: E501

        The final step of the forgotten password reset procedure performs password reset with a token obtained from the email message sent by the POST /password/forgot endpoint and the new password and its confirmation. If @password@ or @confirmPassword@ are missing, then this endpoint performs a mere token validation like the @/password/check-token@ endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_password_reset_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePasswordData body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_password_reset_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in local_var_params or
                local_var_params['body'] is None):
            raise ApiValueError("Missing the required parameter `body` when calling `account_password_reset_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/account/password/reset', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
