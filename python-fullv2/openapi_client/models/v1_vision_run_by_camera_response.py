# coding: utf-8

"""
    Samsara API

    <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).   # noqa: E501

    The version of the OpenAPI document: 2019-11-19
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class V1VisionRunByCameraResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'camera_id': 'int',
        'ended_at_ms': 'int',
        'inspection_results': 'list[V1VisionRunByCameraResponseInspectionResults]',
        'is_ongoing': 'bool',
        'program': 'V1VisionRunByCameraResponseProgram',
        'run_summary': 'V1VisionRunByCameraResponseRunSummary',
        'started_at_ms': 'int'
    }

    attribute_map = {
        'camera_id': 'cameraId',
        'ended_at_ms': 'endedAtMs',
        'inspection_results': 'inspectionResults',
        'is_ongoing': 'isOngoing',
        'program': 'program',
        'run_summary': 'runSummary',
        'started_at_ms': 'startedAtMs'
    }

    def __init__(self, camera_id=None, ended_at_ms=None, inspection_results=None, is_ongoing=None, program=None, run_summary=None, started_at_ms=None, local_vars_configuration=None):  # noqa: E501
        """V1VisionRunByCameraResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._camera_id = None
        self._ended_at_ms = None
        self._inspection_results = None
        self._is_ongoing = None
        self._program = None
        self._run_summary = None
        self._started_at_ms = None
        self.discriminator = None

        if camera_id is not None:
            self.camera_id = camera_id
        if ended_at_ms is not None:
            self.ended_at_ms = ended_at_ms
        if inspection_results is not None:
            self.inspection_results = inspection_results
        if is_ongoing is not None:
            self.is_ongoing = is_ongoing
        if program is not None:
            self.program = program
        if run_summary is not None:
            self.run_summary = run_summary
        if started_at_ms is not None:
            self.started_at_ms = started_at_ms

    @property
    def camera_id(self):
        """Gets the camera_id of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The camera_id of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: int
        """
        return self._camera_id

    @camera_id.setter
    def camera_id(self, camera_id):
        """Sets the camera_id of this V1VisionRunByCameraResponse.


        :param camera_id: The camera_id of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: int
        """

        self._camera_id = camera_id

    @property
    def ended_at_ms(self):
        """Gets the ended_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The ended_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: int
        """
        return self._ended_at_ms

    @ended_at_ms.setter
    def ended_at_ms(self, ended_at_ms):
        """Sets the ended_at_ms of this V1VisionRunByCameraResponse.


        :param ended_at_ms: The ended_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: int
        """

        self._ended_at_ms = ended_at_ms

    @property
    def inspection_results(self):
        """Gets the inspection_results of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The inspection_results of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: list[V1VisionRunByCameraResponseInspectionResults]
        """
        return self._inspection_results

    @inspection_results.setter
    def inspection_results(self, inspection_results):
        """Sets the inspection_results of this V1VisionRunByCameraResponse.


        :param inspection_results: The inspection_results of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: list[V1VisionRunByCameraResponseInspectionResults]
        """

        self._inspection_results = inspection_results

    @property
    def is_ongoing(self):
        """Gets the is_ongoing of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The is_ongoing of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_ongoing

    @is_ongoing.setter
    def is_ongoing(self, is_ongoing):
        """Sets the is_ongoing of this V1VisionRunByCameraResponse.


        :param is_ongoing: The is_ongoing of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: bool
        """

        self._is_ongoing = is_ongoing

    @property
    def program(self):
        """Gets the program of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The program of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: V1VisionRunByCameraResponseProgram
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this V1VisionRunByCameraResponse.


        :param program: The program of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: V1VisionRunByCameraResponseProgram
        """

        self._program = program

    @property
    def run_summary(self):
        """Gets the run_summary of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The run_summary of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: V1VisionRunByCameraResponseRunSummary
        """
        return self._run_summary

    @run_summary.setter
    def run_summary(self, run_summary):
        """Sets the run_summary of this V1VisionRunByCameraResponse.


        :param run_summary: The run_summary of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: V1VisionRunByCameraResponseRunSummary
        """

        self._run_summary = run_summary

    @property
    def started_at_ms(self):
        """Gets the started_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501


        :return: The started_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501
        :rtype: int
        """
        return self._started_at_ms

    @started_at_ms.setter
    def started_at_ms(self, started_at_ms):
        """Sets the started_at_ms of this V1VisionRunByCameraResponse.


        :param started_at_ms: The started_at_ms of this V1VisionRunByCameraResponse.  # noqa: E501
        :type: int
        """

        self._started_at_ms = started_at_ms

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1VisionRunByCameraResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VisionRunByCameraResponse):
            return True

        return self.to_dict() != other.to_dict()