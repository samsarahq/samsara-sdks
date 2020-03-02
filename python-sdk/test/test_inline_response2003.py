# coding: utf-8

"""
    Samsara API

    This is the Samsara API.  # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara
from samsara.models.inline_response2003 import InlineResponse2003  # noqa: E501
from samsara.rest import ApiException

class TestInlineResponse2003(unittest.TestCase):
    """InlineResponse2003 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2003
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.inline_response2003.InlineResponse2003()  # noqa: E501
        if include_optional :
            return InlineResponse2003(
                vehicles = [
                    samsara.models.v1_vehicle_maintenance.V1VehicleMaintenance(
                        id = 112, 
                        j1939 = samsara.models.v1_vehicle_maintenance_j1939.V1VehicleMaintenance_j1939(
                            check_engine_light = samsara.models.v1_vehicle_maintenance_j1939_check_engine_light.V1VehicleMaintenance_j1939_checkEngineLight(
                                emissions_is_on = True, 
                                protect_is_on = True, 
                                stop_is_on = True, 
                                warning_is_on = True, ), 
                            diagnostic_trouble_codes = [
                                samsara.models.v1_vehicle_maintenance_j1939_diagnostic_trouble_codes.V1VehicleMaintenance_j1939_diagnosticTroubleCodes(
                                    fmi_id = 56, 
                                    fmi_text = '0', 
                                    occurrence_count = 56, 
                                    spn_description = '0', 
                                    spn_id = 56, 
                                    tx_id = 56, )
                                ], ), 
                        passenger = samsara.models.v1_vehicle_maintenance_passenger.V1VehicleMaintenance_passenger(), )
                    ]
            )
        else :
            return InlineResponse2003(
        )

    def testInlineResponse2003(self):
        """Test InlineResponse2003"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()