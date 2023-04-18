from django.urls import path, include

from .views import GoogleLogin, FacebookConnect, TwitterConnect

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("register/", include("dj_rest_auth.registration.urls")),
    path("google/", GoogleLogin.as_view(), name="google_login"),
    path("facebook/connect/", FacebookConnect.as_view(), name="facebook_connect"),
    path("twitter/connect/", TwitterConnect.as_view(), name="twitter_connect"),
]
