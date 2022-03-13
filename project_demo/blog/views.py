from dataclasses import fields
from pyexpat import model
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (ListView, 
                                DetailView, 
                                CreateView, 
                                UpdateView,
                                DeleteView)
from .models import Post

# creating first page "Home Page".
def home(request):
    context = {
        'posts': Post.objects.all()   # we getting our data from this method
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    # The url scheme that django search for
    # <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-id']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post 
    fields = ['title', 'Content']

    # we will override the form vaild method to make the current user able to create a post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'Content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Creating second page "About Page".
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})