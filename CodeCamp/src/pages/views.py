from django.shortcuts import render
# To return custom built home page, Use http response
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args,**kwargs): #*args,**kwargs this bcoz we need some functional arguments
    return render(request,'startpage.html',{})

def contact_view(request,*args,**kwargs): #*args,**kwargs this bcoz we need some arguments
    print(request.user) #This is for authentication purpose 
    return HttpResponse("<h1>Contact pages</h1>")

    # This is simialr with render

def contact_view1(request,*args,**kwargs): #*args,**kwargs this bcoz we need some arguments
    return render(request,'contact.html',{})

def mainHome_view(request,*args,**kwargs):
    return render(request,'home.html',{})
    # bcoz of render we return a page without actually giving the file it's simply render the content
