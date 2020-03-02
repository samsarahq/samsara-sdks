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


class SafetyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1get_driver_safety_score(self, driver_id, start_ms, end_ms, **kwargs):  # noqa: E501
        """Fetch driver safety score  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch the safety score for the driver.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_driver_safety_score(driver_id, start_ms, end_ms, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int driver_id: ID of the driver. Must contain only digits 0-9. (required)
        :param int start_ms: Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. (required)
        :param int end_ms: Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1DriverSafetyScoreResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1get_driver_safety_score_with_http_info(driver_id, start_ms, end_ms, **kwargs)  # noqa: E501

    def v1get_driver_safety_score_with_http_info(self, driver_id, start_ms, end_ms, **kwargs):  # noqa: E501
        """Fetch driver safety score  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch the safety score for the driver.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_driver_safety_score_with_http_info(driver_id, start_ms, end_ms, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int driver_id: ID of the driver. Must contain only digits 0-9. (required)
        :param int start_ms: Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. (required)
        :param int end_ms: Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1DriverSafetyScoreResponse, status_code(int), headers(HTTPHeaderDict))
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
                    " to method v1get_driver_safety_score" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'driver_id' is set
        if self.api_client.client_side_validation and ('driver_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['driver_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `driver_id` when calling `v1get_driver_safety_score`")  # noqa: E501
        # verify the required parameter 'start_ms' is set
        if self.api_client.client_side_validation and ('start_ms' not in local_var_params or  # noqa: E501
                                                        local_var_params['start_ms'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `start_ms` when calling `v1get_driver_safety_score`")  # noqa: E501
        # verify the required parameter 'end_ms' is set
        if self.api_client.client_side_validation and ('end_ms' not in local_var_params or  # noqa: E501
                                                        local_var_params['end_ms'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end_ms` when calling `v1get_driver_safety_score`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'driver_id' in local_var_params:
            path_params['driverId'] = local_var_params['driver_id']  # noqa: E501

        query_params = []
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
            '/v1/fleet/drivers/{driverId}/safety/score', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1DriverSafetyScoreResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1get_vehicle_harsh_event(self, vehicle_id, timestamp, **kwargs):  # noqa: E501
        """Fetch harsh events  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch harsh event details for a vehicle.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_vehicle_harsh_event(vehicle_id, timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int vehicle_id: ID of the vehicle. Must contain only digits 0-9. (required)
        :param int timestamp: Timestamp in milliseconds representing the timestamp of a harsh event. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1VehicleHarshEventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1get_vehicle_harsh_event_with_http_info(vehicle_id, timestamp, **kwargs)  # noqa: E501

    def v1get_vehicle_harsh_event_with_http_info(self, vehicle_id, timestamp, **kwargs):  # noqa: E501
        """Fetch harsh events  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch harsh event details for a vehicle.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_vehicle_harsh_event_with_http_info(vehicle_id, timestamp, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int vehicle_id: ID of the vehicle. Must contain only digits 0-9. (required)
        :param int timestamp: Timestamp in milliseconds representing the timestamp of a harsh event. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1VehicleHarshEventResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['vehicle_id', 'timestamp']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1get_vehicle_harsh_event" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'vehicle_id' is set
        if self.api_client.client_side_validation and ('vehicle_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['vehicle_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `vehicle_id` when calling `v1get_vehicle_harsh_event`")  # noqa: E501
        # verify the required parameter 'timestamp' is set
        if self.api_client.client_side_validation and ('timestamp' not in local_var_params or  # noqa: E501
                                                        local_var_params['timestamp'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `timestamp` when calling `v1get_vehicle_harsh_event`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vehicle_id' in local_var_params:
            path_params['vehicleId'] = local_var_params['vehicle_id']  # noqa: E501

        query_params = []
        if 'timestamp' in local_var_params and local_var_params['timestamp'] is not None:  # noqa: E501
            query_params.append(('timestamp', local_var_params['timestamp']))  # noqa: E501

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
            '/v1/fleet/vehicles/{vehicleId}/safety/harsh_event', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1VehicleHarshEventResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1get_vehicle_safety_score(self, vehicle_id, start_ms, end_ms, **kwargs):  # noqa: E501
        """Fetch vehicle safety scores  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch the safety score for the vehicle.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_vehicle_safety_score(vehicle_id, start_ms, end_ms, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int vehicle_id: ID of the vehicle. Must contain only digits 0-9. (required)
        :param int start_ms: Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. (required)
        :param int end_ms: Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: V1VehicleSafetyScoreResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.v1get_vehicle_safety_score_with_http_info(vehicle_id, start_ms, end_ms, **kwargs)  # noqa: E501

    def v1get_vehicle_safety_score_with_http_info(self, vehicle_id, start_ms, end_ms, **kwargs):  # noqa: E501
        """Fetch vehicle safety scores  # noqa: E501

        <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> This endpoint is still on our legacy API. </nh> </n>  Fetch the safety score for the vehicle.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1get_vehicle_safety_score_with_http_info(vehicle_id, start_ms, end_ms, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int vehicle_id: ID of the vehicle. Must contain only digits 0-9. (required)
        :param int start_ms: Timestamp in milliseconds representing the start of the period to fetch, inclusive. Used in combination with endMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. (required)
        :param int end_ms: Timestamp in milliseconds representing the end of the period to fetch, inclusive. Used in combination with startMs. Total duration (endMs - startMs) must be greater than or equal to 1 hour. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(V1VehicleSafetyScoreResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['vehicle_id', 'start_ms', 'end_ms']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1get_vehicle_safety_score" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'vehicle_id' is set
        if self.api_client.client_side_validation and ('vehicle_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['vehicle_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `vehicle_id` when calling `v1get_vehicle_safety_score`")  # noqa: E501
        # verify the required parameter 'start_ms' is set
        if self.api_client.client_side_validation and ('start_ms' not in local_var_params or  # noqa: E501
                                                        local_var_params['start_ms'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `start_ms` when calling `v1get_vehicle_safety_score`")  # noqa: E501
        # verify the required parameter 'end_ms' is set
        if self.api_client.client_side_validation and ('end_ms' not in local_var_params or  # noqa: E501
                                                        local_var_params['end_ms'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end_ms` when calling `v1get_vehicle_safety_score`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vehicle_id' in local_var_params:
            path_params['vehicleId'] = local_var_params['vehicle_id']  # noqa: E501

        query_params = []
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
            '/v1/fleet/vehicles/{vehicleId}/safety/score', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1VehicleSafetyScoreResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
