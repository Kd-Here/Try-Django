from django.shortcuts import render

# Create your views here.

#Views function is to take request and give response
# request -> response
# It is for request handler  

from django.http import HttpResponse
def say_hello(request):
    # Pull data from db
    # transform 
    # send email
    x = calculate()
    y = 77
    return render(request,'hello.html',{'name':'Kdhere'})


def calculate():
    x = 1
    y = 2 
    return x