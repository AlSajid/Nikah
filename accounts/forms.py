from django import forms
from accounts.models import userProfile

class userProfileForm(forms.ModelForm):
    dateOfBirth = forms.DateField(widget=forms.TextInput(
        attrs={'type':'date'}
    ))
    class Meta:
        model = userProfile
        exclude = ('user',)