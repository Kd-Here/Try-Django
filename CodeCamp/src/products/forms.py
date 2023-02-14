from django import forms

from .models import Product

#This is using Product model but with some fields only
class ProductCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'appearance-none block w-40 bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'
        })
    )
    email = forms.EmailField()
    description = forms.CharField(
        widget = forms.TextInput(attrs={'class':'bg-gray-200 my-8 appearance-none border-2 border-gray-200 rounded w-40 py-4 px-15 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" id="inline-full-name"'})
    #Since using widget we can control html inner content and with attrs we can add style,class,id etc...
    )
    price = forms.DecimalField(
        widget=forms.TextInput(attrs={
            'class':'bg-gray-200 '
        })
    )
    # Learning how to validated the data! we will check whether our title data have certain words or not

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    #Author saids add *args and **kwargs when your are overwriting 
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get('title')
        # Here cleaned_data is built in django method which will retrive data.
        if 'xxx' in title:
            raise forms.ValidationError("this is not valid titile") 
        if '.i.' in title:
            raise forms.ValidationError("this is not valid titile") 
        return title

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        # Here cleaned_data is built in django method which will retrive data.
        if not email.endswith('edu'):
            raise forms.ValidationError("this is not valid mail") 
         
        return email

#This is raw version what happen if we want different model to store data
##################################
# We reffered from here what's widgets extracting data from html and changing html data of display using widget we can change attr which function same as html from input filed
# https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_and_retrieving_form_data
##################################

"""class RawProductForm(forms.Form):
    # This is not model form it's standard django form
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'appearance-none block w-40 bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'
        })
    )
    description = forms.CharField(
        widget = forms.TextInput(attrs={'class':'bg-gray-200 my-8 appearance-none border-2 border-gray-200 rounded w-40 py-4 px-15 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500" id="inline-full-name"'})
    #Since using widget we can control html inner content and with attrs we can add style,class,id etc...
    )
    price = forms.DecimalField(
        widget=forms.TextInput(attrs={
            'class':'bg-gray-200 '
        })
    )
"""
    