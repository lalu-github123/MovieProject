from django import forms
from . models import film1

class MovieForm(forms.ModelForm):
    class Meta:
        model = film1
        fields=['name','year','desc','img']
