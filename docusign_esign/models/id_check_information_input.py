# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IdCheckInformationInput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address_information_input=None, dob_information_input=None, ssn4_information_input=None, ssn9_information_input=None):
        """
        IdCheckInformationInput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address_information_input': 'AddressInformationInput',
            'dob_information_input': 'DobInformationInput',
            'ssn4_information_input': 'Ssn4InformationInput',
            'ssn9_information_input': 'Ssn9InformationInput'
        }

        self.attribute_map = {
            'address_information_input': 'addressInformationInput',
            'dob_information_input': 'dobInformationInput',
            'ssn4_information_input': 'ssn4InformationInput',
            'ssn9_information_input': 'ssn9InformationInput'
        }

        self._address_information_input = address_information_input
        self._dob_information_input = dob_information_input
        self._ssn4_information_input = ssn4_information_input
        self._ssn9_information_input = ssn9_information_input

    @property
    def address_information_input(self):
        """
        Gets the address_information_input of this IdCheckInformationInput.

        :return: The address_information_input of this IdCheckInformationInput.
        :rtype: AddressInformationInput
        """
        return self._address_information_input

    @address_information_input.setter
    def address_information_input(self, address_information_input):
        """
        Sets the address_information_input of this IdCheckInformationInput.

        :param address_information_input: The address_information_input of this IdCheckInformationInput.
        :type: AddressInformationInput
        """

        self._address_information_input = address_information_input

    @property
    def dob_information_input(self):
        """
        Gets the dob_information_input of this IdCheckInformationInput.

        :return: The dob_information_input of this IdCheckInformationInput.
        :rtype: DobInformationInput
        """
        return self._dob_information_input

    @dob_information_input.setter
    def dob_information_input(self, dob_information_input):
        """
        Sets the dob_information_input of this IdCheckInformationInput.

        :param dob_information_input: The dob_information_input of this IdCheckInformationInput.
        :type: DobInformationInput
        """

        self._dob_information_input = dob_information_input

    @property
    def ssn4_information_input(self):
        """
        Gets the ssn4_information_input of this IdCheckInformationInput.

        :return: The ssn4_information_input of this IdCheckInformationInput.
        :rtype: Ssn4InformationInput
        """
        return self._ssn4_information_input

    @ssn4_information_input.setter
    def ssn4_information_input(self, ssn4_information_input):
        """
        Sets the ssn4_information_input of this IdCheckInformationInput.

        :param ssn4_information_input: The ssn4_information_input of this IdCheckInformationInput.
        :type: Ssn4InformationInput
        """

        self._ssn4_information_input = ssn4_information_input

    @property
    def ssn9_information_input(self):
        """
        Gets the ssn9_information_input of this IdCheckInformationInput.

        :return: The ssn9_information_input of this IdCheckInformationInput.
        :rtype: Ssn9InformationInput
        """
        return self._ssn9_information_input

    @ssn9_information_input.setter
    def ssn9_information_input(self, ssn9_information_input):
        """
        Sets the ssn9_information_input of this IdCheckInformationInput.

        :param ssn9_information_input: The ssn9_information_input of this IdCheckInformationInput.
        :type: Ssn9InformationInput
        """

        self._ssn9_information_input = ssn9_information_input

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
