from django.shortcuts import render
from .models import Article
# Create your views here.


def blog_page(request):
    con = {}
    return render(request,'articles/article_list.html',con)

def display_All(req):
    ob = Article.objects.all()
    con = {
        'blogList':ob
    }
    return render(req,'articles/article_list.html',con)

def dynamic_display(req,num):
    obj = Article.objects.get(id=num)
    con = {
        'ball':obj
    }
    return render(req,'articles/details.html',con)
