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

import samsara
from samsara.models.vehicle_location_time import VehicleLocationTime  # noqa: E501
from samsara.rest import ApiException

class TestVehicleLocationTime(unittest.TestCase):
    """VehicleLocationTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VehicleLocationTime
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.vehicle_location_time.VehicleLocationTime()  # noqa: E501
        if include_optional :
            return VehicleLocationTime(
            )
        else :
            return VehicleLocationTime(
        )

    def testVehicleLocationTime(self):
        """Test VehicleLocationTime"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
