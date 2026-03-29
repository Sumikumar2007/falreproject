from django.urls import path
from accounts.views import join, login, profile

urlpatterns = [
    path("login/", login, name="login"),
    path("join/", join, name="join"),
    path("profile/", profile, name="profile"),
]