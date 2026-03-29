from django.shortcuts import render

def login(request):
    return render(request, "accounts/login.html")

def join(request):
    return render(request, "accounts/join.html")

def profile(request):
    return render(request, "accounts/profile.html")