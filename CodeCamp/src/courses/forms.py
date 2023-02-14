from django import forms

from .models import Course


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title'
        ]
# Custom validation method checking some inpu tshould not present in title
    # def clean_<field_name>(self):
    #     raise error
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'xxx':
            raise forms.ValidationError("This is not a valid title")
        return title