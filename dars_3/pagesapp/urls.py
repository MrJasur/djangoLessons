from django.urls import path
from .views import HomePageView, AboutPageView, MainPageView, SingUpPageView


urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'), #bu yerda, HomePageView(urls.py da korganimiz TemplateView dan voris olgandik) TemplateView ning .as_view() method dan foydalanyabdi
    path('about/', AboutPageView.as_view(), name='about'),
    path('main/', MainPageView.as_view(), name='asosiy'),
    path('signup/', SingUpPageView.as_view(), name='signup'),
]