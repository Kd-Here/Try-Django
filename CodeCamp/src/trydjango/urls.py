"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# See above function view how to import view from file and map with url follow both step
# Step 1 :- Imported 
# from pages import views #Since we can have many views in different app it's better to have general approach for it
from pages.views import home_view,contact_view,mainHome_view,contact_view1


urlpatterns = [
    path('admin/', admin.site.urls),
    # Step 2:- Update the path
    path('',home_view,name='home_view'),

    # So url and path is working as when a url is type in server it will looked through views available and the path having url as stored that will return as response

    path('contact/',contact_view),
    # When a user creates any html request of url our django seraches for url pattern if present it returns a response

    # Don't forget to always add the function you wanted to import
    path('conts/',contact_view1),

    
    path('index',mainHome_view),

]
