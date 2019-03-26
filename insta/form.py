from django import forms
from .models import Image,Profile,Comment

    
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','profile','likes','pub_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user']       