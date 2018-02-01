from .provider import CILogonProvider
from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

urlpatterns = default_urlpatterns(CILogonProvider)
print(urlpatterns)
