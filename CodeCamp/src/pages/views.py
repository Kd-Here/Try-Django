from django.shortcuts import render
# To return custom built home page, Use http response
from django.http import HttpResponse

# Create your views here.
def contact_view1(request,*args,**kwargs): #*args,**kwargs this bcoz we need some arguments
    return render(request,'contact.html',{})


def home_view(request,*args,**kwargs): #*args,**kwargs this bcoz we need some functional arguments
    my_context = {
        'TodayDate':3,
        'Toadymonth':"feb",
        'Todayyear':2023,
        'ad': [122,22,23,242,45,66,77,88,99],
        'myhtml':"<h1>Hello World </h1>"
    }
    return render(request,'startpage.html',my_context)

def contact_view(request,*args,**kwargs): #*args,**kwargs this bcoz we need some arguments
    print(request.user) #This is for authentication purpose 
    return HttpResponse("<h1>Contact pages</h1>")

    # This is simialr with render


def mainHome_view(request,*args,**kwargs):
    return render(request,'home.html',{})
    # bcoz of render we return a page without actually giving the file it's simply render the content
