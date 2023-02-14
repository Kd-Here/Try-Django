from django.shortcuts import render
from .models import Product 


from .forms import ProductCreateForm #, RawProductForm
# Create your views here.
# This is for custom form 

def product_created(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
    # else:
    #     return render(request,"product/details.html",{}) 
    context = {
        'form' : form
    }
    return render(request,"product/create.html",context)

#This is for your custom made form,

# def product_created(request):

#     if request.method == "POST":
#         title = request.POST.get('title')
#         #Product.objects.create(title=my_title)
#         print(title)
#     context = {}   
#     return render(request,"product/create.html",context)

##################################

#This is for your custom made form,

##################################
"""def product_created(request):
    my_form = RawProductForm() #Created a instance of RawProductForm which is raw dajngo form
    if request.method == "POST": #checking whether method is post since by default it' get
        my_form = RawProductForm(request.POST)    # We passed request.POST in instance which means our class can access it's value try to print what is request.POST

        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data )  #Here **indicates there can 'n' number of arguments(userform data) coming from user from frontend
    context = {
        "form" : my_form
    }   
    return render(request,"product/create.html",context)
"""


def product_details(request):
    initial_data = {
        'title' : 'Ny is the land'
    }
    obj = Product.objects.get(id=1)
    form = ProductCreateForm(request.POST or None,initial=initial_data,instance=obj)

    # context = {
    #     'title' : obj.title,
    #     'summary' : obj.summary,
    #     'description':obj.description,
    # }
    # Instead of passing every attribute of obj in variable you can create a variable and pass it as context and called it in template with context.key

    #Inside context we passed a dict consisting inner dictof object
    context = {
        'form' : form
    }
    return render(request,"product/details.html",context)
    #Now we have created templates inside our products


##########
##########
#Dynamic content changin using dynamic url routing
##########
##########


# Also handling event if certain page is not existed

#1) This is first method to handle it
from django.shortcuts import get_object_or_404

#2) Second method to handle it by try block
from django.http import Http404

def dyanmic_lookup_view(request,id):
    obj = Product.objects.get(id=id)
    # 1)
    # obj = get_object_or_404(Product,id=id)

    #2) 
    # try: 
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        'object' : obj
    }

    return render(request,'product/details.html',context)


from django.shortcuts import render, redirect
def product_delete(Request,id):
    obj = Product.objects.get(id=id)
    if Request.method == "POST":
        obj.delete()
        return redirect('../../')

    context = {
        'bo' :obj
    }
    return render(Request,'product/delete.html',context)

def prdouct_list(req):
    queryset = Product.objects.all() #methods show all product in list
    cont = {
        'listofObj' : queryset
    }
    return render(req,'product/product_list.html',cont)