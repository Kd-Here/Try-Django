from django import forms
from .models import Article
from django.urls import reverse
class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'author',
        ]

    
    