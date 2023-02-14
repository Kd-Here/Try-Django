from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2,max_digits=1000)
    summary = models.TextField(default="This was awesome course!") 
    featured = models.BooleanField(null=True,blank=True)

    
    def get_absoulte_url(self):
        """this is not a dyanmic url function bcoz if we change products/ map in url 
        here it will also change so to make it dyanmic use name
       # return f'/products/{self.id}/'      
       # #when this function is called it will return the base url with id"""


        """
        #This is a dynamic way of creating url
        Try to make change in urls.py 
        instead of path('products/<int:id>/',dyanmic_lookup_view,name='product-details'),
            use     path('p/<int:id>/',dyanmic_lookup_view,name='product-details'),
            see we change the path and our template is using ahref for that path so bcoz of changes in one this will also do requried changes
        """
        return reverse('products:product-details',kwargs={"id":self.id})