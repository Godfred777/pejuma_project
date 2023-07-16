from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pejuma_app/Landingpage.html')

def about(request):
    return render(request, 'pejuma_app/about.html')

def signup(request):
    return render(request, 'pejuma_app/signup.html')

def signin(request):
    return render(request, 'pejuma_app/signin.html')

def contact_us(request):
    return render(request, 'pejuma_app/contactUs.html')

def register(request):
    return render(request, 'pejuma_app/register.html')

def terms_and_conditions(request):
    return render(request, 'pejuma_app/Terms&conditions.html')

def catergoriesList(request):
    return render(request, 'pejuma_app/categoriesList.html')

def dashboard(request):
    return render(request, 'pejuma_app/dashboard.html')