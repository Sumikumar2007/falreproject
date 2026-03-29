from django.shortcuts import render

def book(request):
    return render(request, "influencers/book.html")

def influencersdashboard(request):
    return render(request, "influencers/influencers-dashboard.html")

def influencers(request):
    return render(request, "influencers/influencers.html")