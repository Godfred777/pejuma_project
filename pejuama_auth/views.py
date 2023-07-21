from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LogInForm

# Create your views here.
@csrf_exempt
def signup(request):
    try:
        if request.method == "POST":
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                return HttpResponse('Success...')
        else:
            signup_form = SignUpForm()
            return render(request, 'pejuma_app/signup.html', {"form":signup_form})
    except:
        return HttpResponse('Something went wrong...')
    
@csrf_exempt
def signin(request):
    try:
        if request.method == "POST":
            signin_form = LogInForm(request.POST)
            if signin_form.is_valid():
                return redirect('/dashboard')
        else:
            signin_form = LogInForm()
            return render(request, 'pejuma_app/signin.html', {"form":signin_form})
    except:
        return HttpResponse("<h1>Something went wrong")
    
def signout(request):
    return render(request, 'Landingpage.html')