from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pejuma_app-home'),
    path('about', views.about, name='pejuma_app-about'),
    path('signup', views.signup, name='pejuma_app-signup'),
    path('signin', views.signin, name='pejuma_app-signin'),
    path('register', views.register, name='pejuma_app-register'),
    path('login', views.login, name='pejuma_app-login'),
    path('contact', views.contact_us, name='pejuma_app-contactUs'),
    path('t&c', views.terms_and_conditions, name='pejuma_app-Terms&Conditions'),
    path('catergoriesList', views.catergoriesList, name='pejuam_app-catergoriesList'),
    path('dashboard', views.dashboard, name='pejuma_app-dashboard')
]