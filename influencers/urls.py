from django.urls import path

from influencers.views import book,influencersdashboard,influencers
urlpatterns = [
    path("/book ",book),
    path("/influencersdashboard",influencersdashboard),
    path("/influencers",influencers)
]
