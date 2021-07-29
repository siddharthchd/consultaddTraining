from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=30, required=False)
    lastname = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required = True)
    
    class Meta:
        model = User
        fields = ("username", "firstname", "lastname", "email", "password1", "password2")

class CreateBlogForm(forms.ModelForm):
    title = forms.CharField(max_length = 100)
    content = forms.CharField(max_length = 1000)
    
    class Meta:
        model = User
        fields = ("title", "content")