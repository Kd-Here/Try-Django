# In this file you should map urls to our views functions
from django.urls import path
from . import views 

# Here we given url configration for all apps.
# Playground is a app in views we created a response what will deliver to client
# In urls we are mapping response with url so playground/hello is url which is mapped for say_hello which is response


urlpatterns = [
    # THis is was first urlpatterns array which has url name along it return response
    # path('playground/hello/',views.say_hello)
    
    # Since we added playground in urls.py of storefront urlspattern arry any url or request made by client for url palyground/hello will served by views.say_hello
    # Thus we removed palyground from url since our storefront has playground/ url it will map this to playground/hello
    path('hello/',views.say_hello)
]