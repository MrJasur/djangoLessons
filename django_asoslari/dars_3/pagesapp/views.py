from django.shortcuts import render
from django.views.generic import TemplateView #TemplateView class chaqirib olindi

# Create your views here.

#bu yerda HomePageView TemplateView dan voris olyabdi
class HomePageView(TemplateView):  #qachonki HomePageView class iga murojat qilganda
    template_name = 'home.html'    #bu class home.html ga murojat qiladi


class AboutPageView(TemplateView):
    template_name = 'about.html'


class MainPageView(TemplateView):
    template_name = 'asosiy.html'

class SingUpPageView(TemplateView):
    template_name = 'signup.html'