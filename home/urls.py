from django.urls import path

from . import views
urlpatterns = [
    path("",views.home),
    #path("/dashboard",dashboard),
    #path("/getstart",getstart)


]
