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


class MemberSharedItems(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, envelopes=None, error_details=None, templates=None, user=None):
        """
        MemberSharedItems - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'envelopes': 'list[SharedItem]',
            'error_details': 'ErrorDetails',
            'templates': 'list[TemplateSharedItem]',
            'user': 'UserInfo'
        }

        self.attribute_map = {
            'envelopes': 'envelopes',
            'error_details': 'errorDetails',
            'templates': 'templates',
            'user': 'user'
        }

        self._envelopes = envelopes
        self._error_details = error_details
        self._templates = templates
        self._user = user

    @property
    def envelopes(self):
        """
        Gets the envelopes of this MemberSharedItems.
        

        :return: The envelopes of this MemberSharedItems.
        :rtype: list[SharedItem]
        """
        return self._envelopes

    @envelopes.setter
    def envelopes(self, envelopes):
        """
        Sets the envelopes of this MemberSharedItems.
        

        :param envelopes: The envelopes of this MemberSharedItems.
        :type: list[SharedItem]
        """

        self._envelopes = envelopes

    @property
    def error_details(self):
        """
        Gets the error_details of this MemberSharedItems.

        :return: The error_details of this MemberSharedItems.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this MemberSharedItems.

        :param error_details: The error_details of this MemberSharedItems.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def templates(self):
        """
        Gets the templates of this MemberSharedItems.
        

        :return: The templates of this MemberSharedItems.
        :rtype: list[TemplateSharedItem]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """
        Sets the templates of this MemberSharedItems.
        

        :param templates: The templates of this MemberSharedItems.
        :type: list[TemplateSharedItem]
        """

        self._templates = templates

    @property
    def user(self):
        """
        Gets the user of this MemberSharedItems.

        :return: The user of this MemberSharedItems.
        :rtype: UserInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this MemberSharedItems.

        :param user: The user of this MemberSharedItems.
        :type: UserInfo
        """

        self._user = user

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
