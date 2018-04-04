from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import AgaveProvider

urlpatterns = default_urlpatterns(AgaveProvider)
