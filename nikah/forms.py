from django import forms
from nikah.models import post

class postForm(forms.ModelForm):
    
    class Meta:
        model = post
        fields = ['title','details',]