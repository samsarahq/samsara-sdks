# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara_test
from samsara_test.models.list_addresses_response import ListAddressesResponse  # noqa: E501
from samsara_test.rest import ApiException

class TestListAddressesResponse(unittest.TestCase):
    """ListAddressesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListAddressesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara_test.models.list_addresses_response.ListAddressesResponse()  # noqa: E501
        if include_optional :
            return ListAddressesResponse(
                data = [
                    samsara_test.models.address.Address(
                        address_types = [
                            'yard'
                            ], 
                        contacts = [
                            samsara_test.models.contact_tiny_response.ContactTinyResponse(
                                id = '22408', 
                                first_name = 'Jane', 
                                last_name = 'Jones', )
                            ], 
                        external_ids = {maintenanceId=250020, payrollId=ABFS18600}, 
                        formatted_address = '350 Rhode Island St, San Francisco, CA', 
                        geofence = samsara_test.models.address_geofence.AddressGeofence(
                            circle = samsara_test.models.address_geofence_circle.AddressGeofence_circle(
                                latitude = 37.765363, 
                                longitude = 37.765363, 
                                radius_meters = 250, ), 
                            polygon = samsara_test.models.address_geofence_polygon.AddressGeofence_polygon(
                                vertices = [{latitude=37.765363, longitude=-122.403098}, {latitude=38.765363, longitude=-122.403098}, {latitude=37.765363, longitude=-123.403098}], ), ), 
                        id = '22408', 
                        latitude = 37.765363, 
                        longitude = 37.765363, 
                        name = 'Samsara HQ', 
                        notes = 'Hours of operation: 8am - 6pm; Truck entrance on the Rhode Island street side.', 
                        tags = [
                            samsara_test.models.tag_tiny_response.TagTinyResponse(
                                id = '3914', 
                                name = 'East Coast', )
                            ], )
                    ], 
                pagination = samsara_test.models.pagination_response.PaginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, )
            )
        else :
            return ListAddressesResponse(
                data = [
                    samsara_test.models.address.Address(
                        address_types = [
                            'yard'
                            ], 
                        contacts = [
                            samsara_test.models.contact_tiny_response.ContactTinyResponse(
                                id = '22408', 
                                first_name = 'Jane', 
                                last_name = 'Jones', )
                            ], 
                        external_ids = {maintenanceId=250020, payrollId=ABFS18600}, 
                        formatted_address = '350 Rhode Island St, San Francisco, CA', 
                        geofence = samsara_test.models.address_geofence.AddressGeofence(
                            circle = samsara_test.models.address_geofence_circle.AddressGeofence_circle(
                                latitude = 37.765363, 
                                longitude = 37.765363, 
                                radius_meters = 250, ), 
                            polygon = samsara_test.models.address_geofence_polygon.AddressGeofence_polygon(
                                vertices = [{latitude=37.765363, longitude=-122.403098}, {latitude=38.765363, longitude=-122.403098}, {latitude=37.765363, longitude=-123.403098}], ), ), 
                        id = '22408', 
                        latitude = 37.765363, 
                        longitude = 37.765363, 
                        name = 'Samsara HQ', 
                        notes = 'Hours of operation: 8am - 6pm; Truck entrance on the Rhode Island street side.', 
                        tags = [
                            samsara_test.models.tag_tiny_response.TagTinyResponse(
                                id = '3914', 
                                name = 'East Coast', )
                            ], )
                    ],
                pagination = samsara_test.models.pagination_response.PaginationResponse(
                    end_cursor = 'MjkY', 
                    has_next_page = True, ),
        )

    def testListAddressesResponse(self):
        """Test ListAddressesResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
