from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LogInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class ContactUsForm(forms.Form):
    username = forms.CharField(max_length=100, label="Full name")
    email = forms.EmailField(max_length=100, label="Email")
    message = forms.CharField(widget=forms.Textarea)