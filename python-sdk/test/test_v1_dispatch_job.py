# coding: utf-8

"""
    Samsara API

    <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api-legacy).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api-legacy) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).   # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import samsara
from samsara.models.v1_dispatch_job import V1DispatchJob  # noqa: E501
from samsara.rest import ApiException

class TestV1DispatchJob(unittest.TestCase):
    """V1DispatchJob unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1DispatchJob
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = samsara.models.v1_dispatch_job.V1DispatchJob()  # noqa: E501
        if include_optional :
            return V1DispatchJob(
                arrived_at_ms = 1462881998034, 
                completed_at_ms = 1462881998034, 
                dispatch_route_id = 55, 
                documents = [
                    samsara.models.v1_dispatch_job_document_info.V1DispatchJobDocumentInfo(
                        driver_id = 1234, 
                        id = '2018_42424242', )
                    ], 
                driver_id = 444, 
                en_route_at_ms = 1462881998034, 
                estimated_arrival_ms = 1462881998034, 
                fleet_viewer_url = 'https://cloud.samsara.com/fleet/viewer/job/fleet_viewer_token', 
                group_id = 101, 
                id = 773, 
                job_state = 'JobState_Arrived', 
                skipped_at_ms = 1462881998034, 
                vehicle_id = 112, 
                destination_address = '123 Main St, Philadelphia, PA 19106', 
                destination_address_id = 67890, 
                destination_lat = 123.456, 
                destination_lng = 37.459, 
                destination_name = 'ACME Inc. Philadelphia HQ', 
                notes = 'Ensure crates are stacked no more than 3 high.', 
                scheduled_arrival_time_ms = 1462881998034, 
                scheduled_departure_time_ms = 1462881998034
            )
        else :
            return V1DispatchJob(
                dispatch_route_id = 55,
                id = 773,
                job_state = 'JobState_Arrived',
                scheduled_arrival_time_ms = 1462881998034,
        )

    def testV1DispatchJob(self):
        """Test V1DispatchJob"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
