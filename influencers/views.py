from django.shortcuts import render

# Create your views here.
def book(request):
    return render(request,"influencers/book.html")

def influencersdashboard(request):
    return render(request,"influencers/influencersdashboard.html")

def influencers(request):
    return render (request,"influencers/influencers.html")