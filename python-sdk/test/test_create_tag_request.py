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
from samsara.models.create_tag_request import CreateTagRequest  # noqa: E501
from samsara.rest import ApiException

class TestCreateTagRequest(unittest.TestCase):
    """CreateTagRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateTagRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.create_tag_request.CreateTagRequest()  # noqa: E501
        if include_optional :
            return CreateTagRequest(
                addresses = [
                    '23502866574'
                    ], 
                assets = [
                    '23502866574'
                    ], 
                drivers = [
                    '23502866574'
                    ], 
                machines = [
                    '23502866574'
                    ], 
                name = 'California', 
                parent_tag_id = '4815', 
                sensors = [
                    '23502866574'
                    ], 
                vehicles = [
                    '23502866574'
                    ]
            )
        else :
            return CreateTagRequest(
                name = 'California',
        )

    def testCreateTagRequest(self):
        """Test CreateTagRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
