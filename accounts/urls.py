from django.urls import path

from accounts.views import join,login,profile
urlpatterns = [
    path("/login ",login),
    path("/join",join),
    path("/profile",profile)
]
