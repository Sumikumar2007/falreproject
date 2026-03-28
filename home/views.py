from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home/index.html")

def dashboard(request):
    return render(request,"dashboard.html")

def getstart(request):
    return render (request,"getstart.html")

def get_started(request):
    return render(request, 'home/get_started.html')