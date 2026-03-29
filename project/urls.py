from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Sirf include use kar, upar wali direct view line hata de
    path('', include('home.urls')), 
    
    path('accounts/', include('accounts.urls')),
    path('influencers/', include('influencers.urls')),
]