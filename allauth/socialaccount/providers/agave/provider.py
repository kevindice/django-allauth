from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class AgaveAccount(ProviderAccount):

    def extract_uid(self, data):
        print(data)
        return data['id']

    def extract_common_fields(self, data):
        pass

    def to_str(self):
        dflt = super(AgaveAccount, self).to_str()
        return dflt


class AgaveProvider(OAuth2Provider):
    id = 'agave'
    name = 'Agave'
    account_class = AgaveAccount

    def get_default_scope(self):
        return ['PRODUCTION']


provider_classes = [AgaveProvider]
