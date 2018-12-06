from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse, TestCase

from .provider import JupyterHubProvider


class JupyterHubTests(OAuth2TestsMixin, TestCase):
    provider_id = JupyterHubProvider.id

    def get_mocked_response(self):
        return MockedResponse(200, """
        {
        "status": "success",
        }
        """)
