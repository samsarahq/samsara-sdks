# coding: utf-8

"""
    Samsara API

    Integrate your data with the Samsara API, customize the Samsara experience, and join a community of developers building with Samsara.  # noqa: E501

    The version of the OpenAPI document: 2019-11-19
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import samsara
from samsara.api.contacts_api import ContactsApi  # noqa: E501
from samsara.rest import ApiException


class TestContactsApi(unittest.TestCase):
    """ContactsApi unit test stubs"""

    def setUp(self):
        self.api = samsara.api.contacts_api.ContactsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_contact(self):
        """Test case for create_contact

        Create a contact  # noqa: E501
        """
        pass

    def test_delete_contact_by_id(self):
        """Test case for delete_contact_by_id

        Delete a contact  # noqa: E501
        """
        pass

    def test_get_contact_by_id(self):
        """Test case for get_contact_by_id

        Retrieve a contact  # noqa: E501
        """
        pass

    def test_get_contacts(self):
        """Test case for get_contacts

        List all contacts  # noqa: E501
        """
        pass

    def test_update_contact_by_id(self):
        """Test case for update_contact_by_id

        Update a contact  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
