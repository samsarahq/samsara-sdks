# coding: utf-8

"""
    Samsara API

    This is the Samsara API.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from samsara.api_client import ApiClient
from samsara.exceptions import (
    ApiTypeError,
    ApiValueError
)


class HoursOfServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1get_fleet_drivers_hos_daily_logs(self, driver_id, **kwargs):  # noqa: E501
        """Get daily HOS logs for a specific driver  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get summarized daily Hours of Service charts for a specified driver.  The response will contain a list of `days`, where each entry in the list is the driver's summarized hours of service for that entire day.  The time range for a \"day\" is defined by the `driver`'s `eldDayStartHour`. By default, this is `0`, which indicates the `driver`'s \"day\" is from midnight to midnight in the `driver`'s respective `timezone`. This value is configurable per driver.  The `startMs` and `endMs` parameters indicate start and end for the date range you'd like to query. These parameters are inclusive. This means that the response will include the \"day\" that contains `startMs` and the \"day\" that contains `endMs`. For example:  Let's say a `driver`'s `eldDayStartHour` is `0` and their timezone is `America/Chicago`.  If `startMs` was `1576080000000` (December 11, 2019 10:00:00 AM America/Chicago) and an `endMs` was `1576166400000` (December 12, 2019 10:00:00 AM America/Los_Angeles), then the response will contain a two `day` entries: [December 11, 2019 12:00:00 AM America/Chicago to December 12, 2019 12:00:00 AM America/Chicago], and [December 12, 2019 12:00:00 AM America/Chicago to December 13, 2019 12:00:00 AM America/Chicago].  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_fleet_drivers_hos_daily_logs(driver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int driver_id: ID of the driver with HOS logs. (required)
        :param InlineObject hos_logs_param:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1DriverDailyLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1get_fleet_drivers_hos_daily_logs_with_http_info(driver_id, **kwargs)  # noqa: E501

    def v1get_fleet_drivers_hos_daily_logs_with_http_info(self, driver_id, **kwargs):  # noqa: E501
        """Get daily HOS logs for a specific driver  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get summarized daily Hours of Service charts for a specified driver.  The response will contain a list of `days`, where each entry in the list is the driver's summarized hours of service for that entire day.  The time range for a \"day\" is defined by the `driver`'s `eldDayStartHour`. By default, this is `0`, which indicates the `driver`'s \"day\" is from midnight to midnight in the `driver`'s respective `timezone`. This value is configurable per driver.  The `startMs` and `endMs` parameters indicate start and end for the date range you'd like to query. These parameters are inclusive. This means that the response will include the \"day\" that contains `startMs` and the \"day\" that contains `endMs`. For example:  Let's say a `driver`'s `eldDayStartHour` is `0` and their timezone is `America/Chicago`.  If `startMs` was `1576080000000` (December 11, 2019 10:00:00 AM America/Chicago) and an `endMs` was `1576166400000` (December 12, 2019 10:00:00 AM America/Los_Angeles), then the response will contain a two `day` entries: [December 11, 2019 12:00:00 AM America/Chicago to December 12, 2019 12:00:00 AM America/Chicago], and [December 12, 2019 12:00:00 AM America/Chicago to December 13, 2019 12:00:00 AM America/Chicago].  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_fleet_drivers_hos_daily_logs_with_http_info(driver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int driver_id: ID of the driver with HOS logs. (required)
        :param InlineObject hos_logs_param:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1DriverDailyLogResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['driver_id', 'hos_logs_param']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1get_fleet_drivers_hos_daily_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'driver_id' is set
        if self.api_client.client_side_validation and ('driver_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['driver_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `driver_id` when calling `v1get_fleet_drivers_hos_daily_logs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'driver_id' in local_var_params:
            path_params['driver_id'] = local_var_params['driver_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hos_logs_param' in local_var_params:
            body_params = local_var_params['hos_logs_param']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/fleet/drivers/{driver_id}/hos_daily_logs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1DriverDailyLogResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1get_fleet_hos_authentication_logs(self, driver_id, start_ms, end_ms, **kwargs):  # noqa: E501
        """Get HOS signin and signout  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the HOS (hours of service) signin and signout logs for the specified driver. The response includes 4 fields that are now deprecated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_fleet_hos_authentication_logs(driver_id, start_ms, end_ms, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int driver_id: Driver ID to query. (required)
        :param int start_ms: Beginning of the time range, specified in milliseconds UNIX time. (required)
        :param int end_ms: End of the time range, specified in milliseconds UNIX time. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1HosAuthenticationLogsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1get_fleet_hos_authentication_logs_with_http_info(driver_id, start_ms, end_ms, **kwargs)  # noqa: E501

    def v1get_fleet_hos_authentication_logs_with_http_info(self, driver_id, start_ms, end_ms, **kwargs):  # noqa: E501
        """Get HOS signin and signout  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the HOS (hours of service) signin and signout logs for the specified driver. The response includes 4 fields that are now deprecated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_fleet_hos_authentication_logs_with_http_info(driver_id, start_ms, end_ms, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int driver_id: Driver ID to query. (required)
        :param int start_ms: Beginning of the time range, specified in milliseconds UNIX time. (required)
        :param int end_ms: End of the time range, specified in milliseconds UNIX time. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1HosAuthenticationLogsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['driver_id', 'start_ms', 'end_ms']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1get_fleet_hos_authentication_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'driver_id' is set
        if self.api_client.client_side_validation and ('driver_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['driver_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `driver_id` when calling `v1get_fleet_hos_authentication_logs`")  # noqa: E501
        # verify the required parameter 'start_ms' is set
        if self.api_client.client_side_validation and ('start_ms' not in local_var_params or  # noqa: E501
                                                        local_var_params['start_ms'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `start_ms` when calling `v1get_fleet_hos_authentication_logs`")  # noqa: E501
        # verify the required parameter 'end_ms' is set
        if self.api_client.client_side_validation and ('end_ms' not in local_var_params or  # noqa: E501
                                                        local_var_params['end_ms'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end_ms` when calling `v1get_fleet_hos_authentication_logs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'driver_id' in local_var_params and local_var_params['driver_id'] is not None:  # noqa: E501
            query_params.append(('driverId', local_var_params['driver_id']))  # noqa: E501
        if 'start_ms' in local_var_params and local_var_params['start_ms'] is not None:  # noqa: E501
            query_params.append(('startMs', local_var_params['start_ms']))  # noqa: E501
        if 'end_ms' in local_var_params and local_var_params['end_ms'] is not None:  # noqa: E501
            query_params.append(('endMs', local_var_params['end_ms']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/fleet/hos_authentication_logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1HosAuthenticationLogsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1get_fleet_hos_logs(self, hos_logs_param, **kwargs):  # noqa: E501
        """Get HOS logs for a specific driver  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the HOS (hours of service) logs for the specified driver. This method returns all the HOS statuses that the driver was in during this time period.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_fleet_hos_logs(hos_logs_param, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InlineObject1 hos_logs_param: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1HosLogsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1get_fleet_hos_logs_with_http_info(hos_logs_param, **kwargs)  # noqa: E501

    def v1get_fleet_hos_logs_with_http_info(self, hos_logs_param, **kwargs):  # noqa: E501
        """Get HOS logs for a specific driver  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the HOS (hours of service) logs for the specified driver. This method returns all the HOS statuses that the driver was in during this time period.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_fleet_hos_logs_with_http_info(hos_logs_param, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param InlineObject1 hos_logs_param: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1HosLogsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['hos_logs_param']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1get_fleet_hos_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'hos_logs_param' is set
        if self.api_client.client_side_validation and ('hos_logs_param' not in local_var_params or  # noqa: E501
                                                        local_var_params['hos_logs_param'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hos_logs_param` when calling `v1get_fleet_hos_logs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'hos_logs_param' in local_var_params:
            body_params = local_var_params['hos_logs_param']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/fleet/hos_logs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1HosLogsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1get_fleet_hos_logs_summary(self, **kwargs):  # noqa: E501
        """Get current HOS status for all drivers  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the current HOS status for all drivers. Note that this includes inactive as well as active drivers. You may need to upgrade your API token to version 2019-07-31 or later to leverage response pagination. [See here](https://kb.samsara.com/hc/en-us/articles/360026132972-Upgrading-API-Tokens)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_fleet_hos_logs_summary(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str after: Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter.
        :param float limit: Pagination parameter indicating the number of results to return in this request. Used in conjunction with 'after'.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1HosLogsSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1get_fleet_hos_logs_summary_with_http_info(**kwargs)  # noqa: E501

    def v1get_fleet_hos_logs_summary_with_http_info(self, **kwargs):  # noqa: E501
        """Get current HOS status for all drivers  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Get the current HOS status for all drivers. Note that this includes inactive as well as active drivers. You may need to upgrade your API token to version 2019-07-31 or later to leverage response pagination. [See here](https://kb.samsara.com/hc/en-us/articles/360026132972-Upgrading-API-Tokens)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_fleet_hos_logs_summary_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str after: Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter.
        :param float limit: Pagination parameter indicating the number of results to return in this request. Used in conjunction with 'after'.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1HosLogsSummaryResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['after', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1get_fleet_hos_logs_summary" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'after' in local_var_params and local_var_params['after'] is not None:  # noqa: E501
            query_params.append(('after', local_var_params['after']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/fleet/hos_logs_summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1HosLogsSummaryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
