from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class CILogonAccount(ProviderAccount):
    def to_str(self):
        return self.account.extra_data.get('name',
                super(CILogonAccount, self).to_str())
    
class CILogonProvider(OAuth2Provider):
    id = 'cilogon'
    name = 'CILogon'
    account_class = CILogonAccount

    def get_default_scope(self):
        scope = ['profile']
        if app_settings.QUERY_EMAIL:
            scope.append('email')
        return scope


provider_classes = [CILogonProvider]
