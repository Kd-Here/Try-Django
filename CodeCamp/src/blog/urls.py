from django.urls import path
from django.urls import include
from .views import blog_page,display_All,dynamic_display


app_name='blog'

urlpatterns = [
    path('first',blog_page),
    path('list',display_All),
    path('<int:num>/',dynamic_display)
]