from django import forms

class SignUpForm(forms.Form):
    pass

class LogInForm(forms.Form):
    pass

class ContactUsForm(forms.Form):
    username = forms.CharField(max_length=100, label="Full name")
    email = forms.EmailField(max_length=100, label="Email")
    message = forms.CharField(widget=forms.Textarea)