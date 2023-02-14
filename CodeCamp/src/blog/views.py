from django.shortcuts import render,get_object_or_404
from .models import Article

# Create your views here.

#If you used fucntion based url this is what the way to do it.
#But for the class based view there is other way just try it.
"""
def blog_page(request):
    con = {}
    return render(request,'articles/article_list.html',con)

def display_All(req):
    obd= Article.objects.all()
    cin = {
        'blogList':obd
    }
    return render(req,'articles/article_list.html',cin)

def dynamic_display(req,id):
    obj = Article.objects.get(id=id)
    con = {
        'ball':obj
    }
    return render(req,'articles/details.html',con)
"""

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)
#This are the built in django views made of class

from .forms import ArticleModelForm
from .models import Article
from django.urls import reverse

# Create & Update view are similar just remember to pass correct view inside class
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()  

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_delete.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()  

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()   #Template should in format of 
            #<appname>/<modelname>_list.html i.e # <blog>/<article>_list.html
    #That's it we don't even need to add return render call or nything

class ArticleDetailView(DetailView):
    template_name = 'articles/article_details.html'
    #queryset = Article.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


# Delete view is similar to detail view
class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    # At delete our object is directly removed from db it's does n't move us to different page
    # Thus we have this function
    def get_success_url(self):
        return reverse('articles:article-list')