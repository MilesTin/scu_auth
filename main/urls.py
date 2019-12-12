from django.urls import include, path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("login",login),
    path("getCaptcha", getCaptcha),
    path("logout", logout),
    path("getCookies", get_cookies)
]

