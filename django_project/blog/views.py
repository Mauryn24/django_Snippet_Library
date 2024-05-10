from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render  # Importing the render function from Django shortcuts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post  # Importing the Post model from the current directory's models module


# Create your views here.

def home(request):
    # Retrieve all posts from the database using the Post model
    context = {
        'posts': Post.objects.all()  # Querying all Post objects from the database
    }
    # Render the home.html template with the retrieved posts
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # changing order of posts to show from latest to oldest
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
   
class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    # Render the about.html template with the title 'About page'
    return render(request, 'blog/about.html', {'title': 'About page'})
