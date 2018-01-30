import requests

from allauth.socialaccount import app_settings
from .provider import CILogonProvider
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)


class CILogonOAuth2Adapter(OAuth2Adapter):
    provider_id = CILogonProvider.id
    provider_base_url = 'https://cilogon.org'
    
    access_token_url = '{0}/oauth2/token'.format(provider_base_url)
    authorize_url = '{0}/authorize'.format(provider_base_url)
    profile_url = '{0}/oauth2/profile'.format(provider_base_url)
    email_url = '{0}/oauth2/email'.format(provider_base_url)
    userinfo_url = '{0}/oauth2/email'.format(provider_base_url)

    def complete_login(self, request, app, token, **kwargs):
        response = requests.get(
            self.profile_url,
            params={'access_token': token})
        extra_data = response.json()
        
        return self.get_provider().sociallogin_from_response(
            request, extra_data
        )


oauth2_login = OAuth2LoginView.adapter_view(CILogonOAuth2Adapter)
oauth2_callback = OAuth2LoginView.adapter_view(CILogonOAuth2Adapter)
