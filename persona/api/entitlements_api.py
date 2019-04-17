# coding: utf-8

"""
    Persona

    KSF Media unified login service  # noqa: E501

    OpenAPI spec version: 1.3.0
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
