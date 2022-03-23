from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('ism', 'familiya', 'tel', 'email', 'xabar', 'author')
    success_url = reverse_lazy('home')
