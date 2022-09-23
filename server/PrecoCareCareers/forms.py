from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control bg-light py-3'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control  bg-light py-3'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control  bg-light py-3'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control  bg-light py-3'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']