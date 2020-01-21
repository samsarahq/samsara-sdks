# coding: utf-8

"""
    Samsara API

    <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api-legacy).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api-legacy) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).   # noqa: E501

    The version of the OpenAPI document: 2019-12-12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class V1Document(object):
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
        'document_type': 'str',
        'driver_created_at_ms': 'int',
        'driver_id': 'int',
        'fields': 'list[V1DocumentField]',
        'id': 'str',
        'org_id': 'int',
        'server_created_at_ms': 'int',
        'server_updated_at_ms': 'int',
        'vehicle_id': 'int',
        'dispatch_job_id': 'int',
        'notes': 'str',
        'state': 'str'
    }

    attribute_map = {
        'document_type': 'documentType',
        'driver_created_at_ms': 'driverCreatedAtMs',
        'driver_id': 'driverId',
        'fields': 'fields',
        'id': 'id',
        'org_id': 'orgId',
        'server_created_at_ms': 'serverCreatedAtMs',
        'server_updated_at_ms': 'serverUpdatedAtMs',
        'vehicle_id': 'vehicleId',
        'dispatch_job_id': 'dispatchJobId',
        'notes': 'notes',
        'state': 'state'
    }

    def __init__(self, document_type=None, driver_created_at_ms=None, driver_id=None, fields=None, id=None, org_id=None, server_created_at_ms=None, server_updated_at_ms=None, vehicle_id=None, dispatch_job_id=None, notes=None, state='Required', local_vars_configuration=None):  # noqa: E501
        """V1Document - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._document_type = None
        self._driver_created_at_ms = None
        self._driver_id = None
        self._fields = None
        self._id = None
        self._org_id = None
        self._server_created_at_ms = None
        self._server_updated_at_ms = None
        self._vehicle_id = None
        self._dispatch_job_id = None
        self._notes = None
        self._state = None
        self.discriminator = None

        self.document_type = document_type
        self.driver_created_at_ms = driver_created_at_ms
        self.driver_id = driver_id
        self.fields = fields
        self.id = id
        self.org_id = org_id
        self.server_created_at_ms = server_created_at_ms
        self.server_updated_at_ms = server_updated_at_ms
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id
        self.dispatch_job_id = dispatch_job_id
        self.notes = notes
        if state is not None:
            self.state = state

    @property
    def document_type(self):
        """Gets the document_type of this V1Document.  # noqa: E501

        Descriptive name of this type of document.  # noqa: E501

        :return: The document_type of this V1Document.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this V1Document.

        Descriptive name of this type of document.  # noqa: E501

        :param document_type: The document_type of this V1Document.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and document_type is None:  # noqa: E501
            raise ValueError("Invalid value for `document_type`, must not be `None`")  # noqa: E501

        self._document_type = document_type

    @property
    def driver_created_at_ms(self):
        """Gets the driver_created_at_ms of this V1Document.  # noqa: E501

        The time in Unix epoch milliseconds that the document is created on the driver app.  # noqa: E501

        :return: The driver_created_at_ms of this V1Document.  # noqa: E501
        :rtype: int
        """
        return self._driver_created_at_ms

    @driver_created_at_ms.setter
    def driver_created_at_ms(self, driver_created_at_ms):
        """Sets the driver_created_at_ms of this V1Document.

        The time in Unix epoch milliseconds that the document is created on the driver app.  # noqa: E501

        :param driver_created_at_ms: The driver_created_at_ms of this V1Document.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and driver_created_at_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `driver_created_at_ms`, must not be `None`")  # noqa: E501

        self._driver_created_at_ms = driver_created_at_ms

    @property
    def driver_id(self):
        """Gets the driver_id of this V1Document.  # noqa: E501

        ID of the driver for whom the document is submitted  # noqa: E501

        :return: The driver_id of this V1Document.  # noqa: E501
        :rtype: int
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """Sets the driver_id of this V1Document.

        ID of the driver for whom the document is submitted  # noqa: E501

        :param driver_id: The driver_id of this V1Document.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and driver_id is None:  # noqa: E501
            raise ValueError("Invalid value for `driver_id`, must not be `None`")  # noqa: E501

        self._driver_id = driver_id

    @property
    def fields(self):
        """Gets the fields of this V1Document.  # noqa: E501

        The fields associated with this document.  # noqa: E501

        :return: The fields of this V1Document.  # noqa: E501
        :rtype: list[V1DocumentField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this V1Document.

        The fields associated with this document.  # noqa: E501

        :param fields: The fields of this V1Document.  # noqa: E501
        :type: list[V1DocumentField]
        """
        if self.local_vars_configuration.client_side_validation and fields is None:  # noqa: E501
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def id(self):
        """Gets the id of this V1Document.  # noqa: E501

        ID of the document  # noqa: E501

        :return: The id of this V1Document.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1Document.

        ID of the document  # noqa: E501

        :param id: The id of this V1Document.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this V1Document.  # noqa: E501

        Organization ID that the document & driver who submitted the doc belongs to  # noqa: E501

        :return: The org_id of this V1Document.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this V1Document.

        Organization ID that the document & driver who submitted the doc belongs to  # noqa: E501

        :param org_id: The org_id of this V1Document.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def server_created_at_ms(self):
        """Gets the server_created_at_ms of this V1Document.  # noqa: E501

        The time in Unix epoch milliseconds that the document is created on the server.  # noqa: E501

        :return: The server_created_at_ms of this V1Document.  # noqa: E501
        :rtype: int
        """
        return self._server_created_at_ms

    @server_created_at_ms.setter
    def server_created_at_ms(self, server_created_at_ms):
        """Sets the server_created_at_ms of this V1Document.

        The time in Unix epoch milliseconds that the document is created on the server.  # noqa: E501

        :param server_created_at_ms: The server_created_at_ms of this V1Document.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and server_created_at_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `server_created_at_ms`, must not be `None`")  # noqa: E501

        self._server_created_at_ms = server_created_at_ms

    @property
    def server_updated_at_ms(self):
        """Gets the server_updated_at_ms of this V1Document.  # noqa: E501

        The time in Unix epoch milliseconds that the document is updated on the server.  # noqa: E501

        :return: The server_updated_at_ms of this V1Document.  # noqa: E501
        :rtype: int
        """
        return self._server_updated_at_ms

    @server_updated_at_ms.setter
    def server_updated_at_ms(self, server_updated_at_ms):
        """Sets the server_updated_at_ms of this V1Document.

        The time in Unix epoch milliseconds that the document is updated on the server.  # noqa: E501

        :param server_updated_at_ms: The server_updated_at_ms of this V1Document.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and server_updated_at_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `server_updated_at_ms`, must not be `None`")  # noqa: E501

        self._server_updated_at_ms = server_updated_at_ms

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this V1Document.  # noqa: E501

        VehicleID of the driver at document creation.  # noqa: E501

        :return: The vehicle_id of this V1Document.  # noqa: E501
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this V1Document.

        VehicleID of the driver at document creation.  # noqa: E501

        :param vehicle_id: The vehicle_id of this V1Document.  # noqa: E501
        :type: int
        """

        self._vehicle_id = vehicle_id

    @property
    def dispatch_job_id(self):
        """Gets the dispatch_job_id of this V1Document.  # noqa: E501

        ID of the Samsara dispatch job for which the document is submitted  # noqa: E501

        :return: The dispatch_job_id of this V1Document.  # noqa: E501
        :rtype: int
        """
        return self._dispatch_job_id

    @dispatch_job_id.setter
    def dispatch_job_id(self, dispatch_job_id):
        """Sets the dispatch_job_id of this V1Document.

        ID of the Samsara dispatch job for which the document is submitted  # noqa: E501

        :param dispatch_job_id: The dispatch_job_id of this V1Document.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and dispatch_job_id is None:  # noqa: E501
            raise ValueError("Invalid value for `dispatch_job_id`, must not be `None`")  # noqa: E501

        self._dispatch_job_id = dispatch_job_id

    @property
    def notes(self):
        """Gets the notes of this V1Document.  # noqa: E501

        Notes submitted with this document.  # noqa: E501

        :return: The notes of this V1Document.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this V1Document.

        Notes submitted with this document.  # noqa: E501

        :param notes: The notes of this V1Document.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and notes is None:  # noqa: E501
            raise ValueError("Invalid value for `notes`, must not be `None`")  # noqa: E501

        self._notes = notes

    @property
    def state(self):
        """Gets the state of this V1Document.  # noqa: E501

        The condition of the document created for the driver. Can be either `Required` or `Submitted`, if no value is specified, `state` defaults to `Required`. `Required` documents are pre-populated documents for the Driver to fill out in the Driver App.  # noqa: E501

        :return: The state of this V1Document.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this V1Document.

        The condition of the document created for the driver. Can be either `Required` or `Submitted`, if no value is specified, `state` defaults to `Required`. `Required` documents are pre-populated documents for the Driver to fill out in the Driver App.  # noqa: E501

        :param state: The state of this V1Document.  # noqa: E501
        :type: str
        """
        allowed_values = ["Required", "Submitted"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, V1Document):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Document):
            return True

        return self.to_dict() != other.to_dict()
