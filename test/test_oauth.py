# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import os
import unittest

from docusign_esign.client.api_client import ApiClient
from docusign_esign.client.auth.oauth import OAuthToken


class TestConfig(object):
    def __init__(self, user_name=None, client_secret =None, user_id=None, password=None, integrator_key=None, host=None, recipient_email=None,
                 recipient_name=None, template_role_name=None, template_id=None, return_url=None, redirect_uri=None):
        self.user_name = user_name if user_name else "node_sdk@mailinator.com"
        self.password = password if password else "{PASSWORD}
        self.client_secret = client_secret if client_secret else "3b61ffcf-xxxx-xxxx-xxxx-d49f7d82cb55"
        self.integrator_key = integrator_key if integrator_key else "ae30ea4e-xxxx-xxxx-xxxx-fcb57d2dc4df"
        self.host = host if host else "https://demo.docusign.net/restapi"
        self.recipient_email = recipient_email if recipient_email else "node_sdk@mailinator.com"
        self.recipient_name = recipient_name if recipient_name else "node_sdk@mailinator.com"
        self.template_role_name = template_role_name if template_role_name else "node_sdk@mailinator.com"
        self.template_id = template_id if template_id else "cf2a46c2-xxxx-xxxx-xxxx-752547b1a419"
        self.return_url = return_url if return_url else "node_sdk@mailinator.com"
        self.user_id = user_id if user_id else "fcc5726c-xxxx-xxxx-xxxx-40bbbe6ca126"
        self.redirect_uri = redirect_uri if redirect_uri else "http://38a36d7b.ngrok.io"

        self.oauth_host_name = "account-d.docusign.com"
        self.private_key_file_name = "{}/keys/private.pem".format(os.path.dirname(os.path.abspath(__file__)))
        self.expires_in_hours = 1

        # this.IntegratorKeyNoConsent = "66750331-xxxx-xxxx-xxxx-6c1a413a6096";
        # this.PrivateKeyNoConsentFilename = "../../docs/privateKeyConsentReq.pem";


class TestOauth(unittest.TestCase):
    """ AccountBillingPlan unit test stubs """

    def setUp(self):
        self.test_config = TestConfig()
        self.api_client = ApiClient(oauth_host_name=self.test_config.oauth_host_name)
        self.api_client.set_base_path("https://demo.docusign.net")
        self.api_client.set_oauth_host_name(self.test_config.oauth_host_name)

    def test_oauth_uri(self):
        self.api_client.get_oauth_host_name()
        uri = self.api_client.get_authorization_uri(client_id=self.test_config.integrator_key,
                                                redirect_uri=self.test_config.redirect_uri,
                                                scopes=["signature", "impersonation"],
                                                response_type='code')
        self.assertTrue(isinstance(uri, str))
        self.api_client.rest_client.pool_manager.clear()

    def test_jwt_application(self):
        with open(self.test_config.private_key_file_name, 'r') as private_key:
            token_obj = self.api_client.request_jwt_application_token(client_id=self.test_config.integrator_key,
                                                               oauth_host_name=self.test_config.oauth_host_name,
                                                               private_key_bytes=private_key.read(),
                                                               expires_in=self.test_config.expires_in_hours)
            self.assertTrue(isinstance(token_obj, OAuthToken))
            self.api_client.rest_client.pool_manager.clear()

    def test_jwt_user(self):
        with open(self.test_config.private_key_file_name, 'r') as private_key:
            token_obj = self.api_client.request_jwt_user_token(client_id=self.test_config.integrator_key,
                                                               user_id=self.test_config.user_id,
                                                               oauth_host_name=self.api_client.get_oauth_host_name(),
                                                               private_key_bytes=private_key.read(),
                                                               expires_in=self.test_config.expires_in_hours
                                                               )
            self.assertTrue(isinstance(token_obj, OAuthToken))
            self.api_client.rest_client.pool_manager.clear()

    def test_authorization_code_login(self):
        self.api_client.get_oauth_host_name()
        uri = self.api_client.get_authorization_uri(client_id=self.test_config.integrator_key,
                                                    redirect_uri=self.test_config.redirect_uri,
                                                    scopes=["signature"],
                                                    response_type='code')
        self.assertTrue(isinstance(uri, str))

        # import webbrowser
        # from docusign_esign.client.auth.oauth.user_info import UserInfo
        # webbrowser.open(uri)
        #
        # # IMPORTANT: after the login, DocuSign will send back a fresh
        # # authorization code as a query param of the redirect URI.
        # # You should set up a route that handles the redirect call to get
        # # that code and pass it to token endpoint as shown in the next
        # # lines:
        # #
        # code = "code"
        # token_obj = self.api_client.generate_access_token(self.test_config.integrator_key, self.test_config.client_secret, code)
        # self.assertTrue(isinstance(token_obj, OAuthToken))
        #
        # self.api_client.set_access_token(token_obj)
        # user_info = self.api_client.get_user_info(token_obj.access_token)
        # self.assertTrue(isinstance(user_info, UserInfo))
        self.api_client.rest_client.pool_manager.clear()


if __name__ == '__main__':
    unittest.main()