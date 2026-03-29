from django.shortcuts import render

def home(request):
    return render(request, "home/index.html")

def get_started(request):
    return render(request, "home/get-started.html")