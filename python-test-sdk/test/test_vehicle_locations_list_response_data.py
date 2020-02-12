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
from samsara_test.models.vehicle_locations_list_response_data import VehicleLocationsListResponseData  # noqa: E501
from samsara_test.rest import ApiException

class TestVehicleLocationsListResponseData(unittest.TestCase):
    """VehicleLocationsListResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleLocationsListResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara_test.models.vehicle_locations_list_response_data.VehicleLocationsListResponseData()  # noqa: E501
        if include_optional :
            return VehicleLocationsListResponseData(
                id = '123456789', 
                name = 'Midwest Truck #4', 
                locations = [
                    samsara_test.models.vehicle_location.VehicleLocation(
                        latitude = 122.142, 
                        longitude = -93.343, 
                        heading = 120.0, 
                        reverse_geo = samsara_test.models.vehicle_location_reverse_geo.VehicleLocationReverseGeo(
                            formatted_location = '16 N Fair Oaks Ave, Pasadena, CA 91103', ), 
                        speed = 48.3, 
                        time = '2019-05-03T04:30:31.492Z', )
                    ]
            )
        else :
            return VehicleLocationsListResponseData(
                id = '123456789',
                name = 'Midwest Truck #4',
                locations = [
                    samsara_test.models.vehicle_location.VehicleLocation(
                        latitude = 122.142, 
                        longitude = -93.343, 
                        heading = 120.0, 
                        reverse_geo = samsara_test.models.vehicle_location_reverse_geo.VehicleLocationReverseGeo(
                            formatted_location = '16 N Fair Oaks Ave, Pasadena, CA 91103', ), 
                        speed = 48.3, 
                        time = '2019-05-03T04:30:31.492Z', )
                    ],
        )

    def testVehicleLocationsListResponseData(self):
        """Test VehicleLocationsListResponseData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
