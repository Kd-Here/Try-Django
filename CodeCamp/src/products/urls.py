from django.urls import path
from .views import (
    product_details,product_created,dyanmic_lookup_view,
    product_delete,prdouct_list
)

app_name='products'
urlpatterns = [

    # For products app 
    path('',product_details),

    #This is path of form product
    path('create/',product_created),

    path('<int:id>/',dyanmic_lookup_view,name='product-details'),
    # http://127.0.0.1:8000/products/9899/ #try this url it will give DoesNotExist since till now we don't have that object to give simplified error use HandleDoesNotExist
    path('products/<int:id>/delete/',product_delete),
    path('list/',prdouct_list),
]