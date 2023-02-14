from django.urls import path
from django.urls import include
# from .views import blog_page,display_All,dynamic_display

from .views import (
    ArticleListView,ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView
)

app_name='articles'
urlpatterns = [

    path('<int:id>/update/',ArticleUpdateView.as_view(), name='article-update'),
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/',ArticleCreateView.as_view(), name='article-create'),

    # This is default way pk means primary key
    # path('<int:pk>/',ArticleDetailView.as_view(), name='article-list'),
    path('<int:id>/',ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/delete/',ArticleDeleteView.as_view(), name='article-delete'),

]   

#For function's u used this type of url with path 
"""
urlpatterns = [
    path('first',blog_page),
    path('list',display_All),
    path('<int:id>/',dynamic_display,name='blogs_art_page'),
]
"""