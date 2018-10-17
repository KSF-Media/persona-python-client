# coding: utf-8

"""
    Persona

    KSF Media unified login service  # noqa: E501

    OpenAPI spec version: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class UsersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def users_uuid_get(self, uuid, **kwargs):  # noqa: E501
        """Get user by UUID.  # noqa: E501

        Authorization header expects the following format ‘OAuth {token}’  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.users_uuid_get(uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str uuid: (required)
        :param str authorization:
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.users_uuid_get_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.users_uuid_get_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def users_uuid_get_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Get user by UUID.  # noqa: E501

        Authorization header expects the following format ‘OAuth {token}’  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.users_uuid_get_with_http_info(uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str uuid: (required)
        :param str authorization:
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['uuid', 'authorization']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_uuid_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in local_var_params or
                local_var_params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `users_uuid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']  # noqa: E501

        query_params = []

        header_params = {}
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
            '/users/{uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async=local_var_params.get('async'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
