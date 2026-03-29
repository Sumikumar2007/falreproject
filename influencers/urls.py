
from django.urls import path
from influencers.views import book, influencersdashboard, influencers

urlpatterns = [
    path("book/", book, name="book"),
    path("influencers-dashboard/", influencersdashboard, name="influencers_dashboard"),
    path("influencers/", influencers, name="influencers"),
]