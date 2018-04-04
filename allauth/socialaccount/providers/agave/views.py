import requests

from allauth.socialaccount.providers.oauth.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import AgaveProvider

class AgaveOAuth2Adapter(OAuth2Adapter):
    provider_id = AgaveProvider.id
    access_token_url = 'https://public.agaveapi.co/token'
    authorize_url = 'https://public.agaveapi.co/authorize'
    profile_url = 'https://public.agaveapi.co/profiles/v2/'

    def complete_login(self, request, app, token, **kwargs):
        print('response', kwargs['response'])
        uid = kwargs['response'].get('user_id')
        params = {
            'access_token': token.token,
        }

        resp = requests.get(self.profile_url, params=params)

        resp.raise_for_status()
        print('resp', resp.json())
        extra_data = resp.json()['result'][0]
        return self.get_provider().sociallogin_from_response(request, extra_data)

oauth2_login = OAuth2LoginView.adapter_view(AgaveOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(AgaveOAuth2Adapter)
        


