# coding: utf-8

"""
    Samsara API

    <style type=\"text/css\"> n {     padding: 1em;     width: 100%;     display: block;     margin: 28px 0; } n.info {     background-color: rgba(0, 51, 160, 0.1); } n.warning {     background-color: #fdf6e3; } i:before {     margin-right: 6px; } nh {     font-size: 1.5rem;     font-weight: 700;     line-height: 1.1;     display: block; } nb {     margin-top: 10px;     padding-left: 22px;     display: block; } </style>  # Overview  <n class=\"info\"> <nh> <i class=\"fa fa-info-circle\"></i> Something new! </nh> <nb> Welcome Samsara's new and improved API. Check out our FAQ [here](https://developers.samsara.com/docs/introducing-our-next-generation-api) to see what's changed and learn how to get started.<br> <br> Want to access the legacy API docs? You can find them [here](https://www.samsara.com/api).<br> <br> *Note: Because this is a new set of APIs, we have not transitioned all endpoints over to this standard. Endpoints that still use the legacy standards are indicated in the reference documentation. If you can't find an API that you're looking for, we encourage you to look for it in our [legacy API docs](https://www.samsara.com/api) as we continue to transition all endpoints over. Check back here for updates!*<br> <br> Submit your feedback [here](https://forms.gle/r4bs6HQshQAvBuwv6)! </nb> </n>  Samsara provides API endpoints so that you can build powerful applications and custom solutions with sensor data. Samsara has endpoints available to track and analyze sensors, vehicles, and entire fleets.  The Samsara API is a [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer). It uses standard [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) authentication, verbs, and response codes, and it returns [JSON](http://www.json.org/) response bodies. If you're familiar with what you can build with a REST API, then this will be your go-to API reference.  Visit [developers.samsara.com](https://developers.samsara.com) to find getting started guides and an API overview.  If you have any questions, reach out to us at [support@samsara.com](mailto:support@samsara.com).  ## Endpoints  All our APIs can be accessed through HTTP requests to URLs like:  ``` https://api.samsara.com/<endpoint> ```  For EU customers, this URL will be:  ``` https://api.eu.samsara.com/<endpoint> ```  <n class=\"warning\"> <nh> <i class=\"fa fa-exclamation-circle\"></i> Note </nh> <nb> Legacy endpoints will have the URL: `https://api.samsara.com/v1/<endpoint>` or `https://api.eu.samsara.com/v1/<endpoint>` </nb> </n>  ## Authentication  To authenticate your API request you will need to include your secret token. You can manage your API tokens in the [Dashboard](https://cloud.samsara.com). They are visible under `Settings->Organization->API Tokens`.  Your API tokens carry many privileges, so be sure to keep them secure. Do not share your secret API tokens in publicly accessible areas such as GitHub, client-side code, and so on.  Authentication to the API is performed via Bearer Token in the HTTP Authorization header. Provide your API token as the `access_token` value in an `Authorization: Bearer` header. You do not need to provide a password:  ```curl Authorization: Bearer {access_token} ```  All API requests must be made over [HTTPS](https://en.wikipedia.org/wiki/HTTPS). Calls made over plain HTTP or without authentication will fail.  ## Common Patterns  You can find more info about request methods, response codes, error codes, versioning, pagination, timestamps, and mini-objects [here](https://developers.samsara.com/docs/common-structures).   # noqa: E501

    OpenAPI spec version: 2019-09-13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AddressResponseCore(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address_types': 'list[str]',
        'formatted_address': 'str',
        'name': 'str',
        'notes': 'str'
    }

    attribute_map = {
        'address_types': 'addressTypes',
        'formatted_address': 'formattedAddress',
        'name': 'name',
        'notes': 'notes'
    }

    def __init__(self, address_types=None, formatted_address=None, name=None, notes=None):  # noqa: E501
        """AddressResponseCore - a model defined in Swagger"""  # noqa: E501
        self._address_types = None
        self._formatted_address = None
        self._name = None
        self._notes = None
        self.discriminator = None
        if address_types is not None:
            self.address_types = address_types
        if formatted_address is not None:
            self.formatted_address = formatted_address
        if name is not None:
            self.name = name
        if notes is not None:
            self.notes = notes

    @property
    def address_types(self):
        """Gets the address_types of this AddressResponseCore.  # noqa: E501

        Reporting location type associated with the address (used for ELD reporting purposes).  # noqa: E501

        :return: The address_types of this AddressResponseCore.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_types

    @address_types.setter
    def address_types(self, address_types):
        """Sets the address_types of this AddressResponseCore.

        Reporting location type associated with the address (used for ELD reporting purposes).  # noqa: E501

        :param address_types: The address_types of this AddressResponseCore.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["yard", "shortHaul"]  # noqa: E501
        if not set(address_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `address_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(address_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._address_types = address_types

    @property
    def formatted_address(self):
        """Gets the formatted_address of this AddressResponseCore.  # noqa: E501

        The full street address for this address/geofence, as it might be recognized by Google Maps.  # noqa: E501

        :return: The formatted_address of this AddressResponseCore.  # noqa: E501
        :rtype: str
        """
        return self._formatted_address

    @formatted_address.setter
    def formatted_address(self, formatted_address):
        """Sets the formatted_address of this AddressResponseCore.

        The full street address for this address/geofence, as it might be recognized by Google Maps.  # noqa: E501

        :param formatted_address: The formatted_address of this AddressResponseCore.  # noqa: E501
        :type: str
        """

        self._formatted_address = formatted_address

    @property
    def name(self):
        """Gets the name of this AddressResponseCore.  # noqa: E501

        Name of the address.  # noqa: E501

        :return: The name of this AddressResponseCore.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddressResponseCore.

        Name of the address.  # noqa: E501

        :param name: The name of this AddressResponseCore.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this AddressResponseCore.  # noqa: E501

        Notes about the address.  # noqa: E501

        :return: The notes of this AddressResponseCore.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AddressResponseCore.

        Notes about the address.  # noqa: E501

        :param notes: The notes of this AddressResponseCore.  # noqa: E501
        :type: str
        """

        self._notes = notes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AddressResponseCore, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddressResponseCore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other