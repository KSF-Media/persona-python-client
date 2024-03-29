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


class EntitlementsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def entitlements_allow_delete(self, body, **kwargs):  # noqa: E501
        """Remove an entitlement  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_allow_delete(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int body: (required)
        :param str auth_user:
        :param str authorization:
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.entitlements_allow_delete_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.entitlements_allow_delete_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def entitlements_allow_delete_with_http_info(self, body, **kwargs):  # noqa: E501
        """Remove an entitlement  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_allow_delete_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int body: (required)
        :param str auth_user:
        :param str authorization:
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['body', 'auth_user', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method entitlements_allow_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in local_var_params or
                local_var_params['body'] is None):
            raise ApiValueError("Missing the required parameter `body` when calling `entitlements_allow_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'auth_user' in local_var_params:
            header_params['AuthUser'] = local_var_params['auth_user']  # noqa: E501
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/entitlements/allow', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def entitlements_allow_get(self, **kwargs):  # noqa: E501
        """Check if global entitlements are enabled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_allow_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_user:
        :param str authorization:
        :param str ip:
        :param str paper:
        :return: list[PersistedEntitlementAccess]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.entitlements_allow_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.entitlements_allow_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def entitlements_allow_get_with_http_info(self, **kwargs):  # noqa: E501
        """Check if global entitlements are enabled  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_allow_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_user:
        :param str authorization:
        :param str ip:
        :param str paper:
        :return: list[PersistedEntitlementAccess]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['auth_user', 'authorization', 'ip', 'paper']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method entitlements_allow_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ip' in local_var_params:
            query_params.append(('ip', local_var_params['ip']))  # noqa: E501
        if 'paper' in local_var_params:
            query_params.append(('paper', local_var_params['paper']))  # noqa: E501

        header_params = {}
        if 'auth_user' in local_var_params:
            header_params['AuthUser'] = local_var_params['auth_user']  # noqa: E501
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/entitlements/allow', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PersistedEntitlementAccess]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def entitlements_allow_post(self, body, **kwargs):  # noqa: E501
        """Add an entitlement for all users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_allow_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EntitlementAccess body: (required)
        :param str auth_user:
        :param str authorization:
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.entitlements_allow_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.entitlements_allow_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def entitlements_allow_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add an entitlement for all users  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_allow_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EntitlementAccess body: (required)
        :param str auth_user:
        :param str authorization:
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['body', 'auth_user', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method entitlements_allow_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in local_var_params or
                local_var_params['body'] is None):
            raise ApiValueError("Missing the required parameter `body` when calling `entitlements_allow_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'auth_user' in local_var_params:
            header_params['AuthUser'] = local_var_params['auth_user']  # noqa: E501
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/entitlements/allow', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def entitlements_allow_uuid_post(self, uuid, body, **kwargs):  # noqa: E501
        """Grant product access to a customer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_allow_uuid_post(uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param EntitlementAccess body: (required)
        :param str auth_user:
        :param str authorization:
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.entitlements_allow_uuid_post_with_http_info(uuid, body, **kwargs)  # noqa: E501
        else:
            (data) = self.entitlements_allow_uuid_post_with_http_info(uuid, body, **kwargs)  # noqa: E501
            return data

    def entitlements_allow_uuid_post_with_http_info(self, uuid, body, **kwargs):  # noqa: E501
        """Grant product access to a customer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_allow_uuid_post_with_http_info(uuid, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: (required)
        :param EntitlementAccess body: (required)
        :param str auth_user:
        :param str authorization:
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['uuid', 'body', 'auth_user', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method entitlements_allow_uuid_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in local_var_params or
                local_var_params['uuid'] is None):
            raise ApiValueError("Missing the required parameter `uuid` when calling `entitlements_allow_uuid_post`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in local_var_params or
                local_var_params['body'] is None):
            raise ApiValueError("Missing the required parameter `body` when calling `entitlements_allow_uuid_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'auth_user' in local_var_params:
            header_params['AuthUser'] = local_var_params['auth_user']  # noqa: E501
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json;charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/entitlements/allow/{uuid}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def entitlements_free_pass_get(self, **kwargs):  # noqa: E501
        """Verify given free pass hash  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_free_pass_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_user:
        :param str authorization:
        :param str free_pass_hash:
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.entitlements_free_pass_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.entitlements_free_pass_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def entitlements_free_pass_get_with_http_info(self, **kwargs):  # noqa: E501
        """Verify given free pass hash  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_free_pass_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_user:
        :param str authorization:
        :param str free_pass_hash:
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['auth_user', 'authorization', 'free_pass_hash']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method entitlements_free_pass_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'free_pass_hash' in local_var_params:
            query_params.append(('freePassHash', local_var_params['free_pass_hash']))  # noqa: E501

        header_params = {}
        if 'auth_user' in local_var_params:
            header_params['AuthUser'] = local_var_params['auth_user']  # noqa: E501
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/entitlements/free-pass', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def entitlements_get(self, **kwargs):  # noqa: E501
        """List all entitlements  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, list[str])
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.entitlements_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.entitlements_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def entitlements_get_with_http_info(self, **kwargs):  # noqa: E501
        """List all entitlements  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, list[str])
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method entitlements_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/entitlements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, list[str])',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def entitlements_global_get(self, **kwargs):  # noqa: E501
        """Lists all past and future global entitlements  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_global_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_user:
        :param str authorization:
        :return: list[PersistedEntitlementAccess]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.entitlements_global_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.entitlements_global_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def entitlements_global_get_with_http_info(self, **kwargs):  # noqa: E501
        """Lists all past and future global entitlements  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.entitlements_global_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str auth_user:
        :param str authorization:
        :return: list[PersistedEntitlementAccess]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['auth_user', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method entitlements_global_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'auth_user' in local_var_params:
            header_params['AuthUser'] = local_var_params['auth_user']  # noqa: E501
        if 'authorization' in local_var_params:
            header_params['Authorization'] = local_var_params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/entitlements/global', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PersistedEntitlementAccess]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
