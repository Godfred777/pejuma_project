from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactUsForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'pejuma_app/Landingpage.html')

def about(request):
    return render(request, 'pejuma_app/about.html')

@csrf_exempt
def contact_us(request):
    try:
        if request.method == "POST":
            contact_form = ContactUsForm(request.POST)
            if contact_form.is_valid():
                return HttpResponse('Success...')
        else:
            contact_form = ContactUsForm()
        return render(request, 'pejuma_app/contactUs.html', {"form":contact_form}) 
    except:
        return HttpResponse('Something went wrong')

def register(request):
    return render(request, 'pejuma_app/register.html')
    
def terms_and_conditions(request):
    return render(request, 'pejuma_app/Terms&conditions.html')

def catergoriesList(request):
    return render(request, 'pejuma_app/categoriesList.html')

def dashboard(request):
    return render(request, 'pejuma_app/dashboard.html')