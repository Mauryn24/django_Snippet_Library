from django.shortcuts import render  # Importing the render function from Django shortcuts
from django.http import HttpResponse  # Importing the HttpResponse class from Django HTTP
from .models import Post  # Importing the Post model from the current directory's models module

# Sample data for demonstration (temporary)
posts = [
    {
        'author': 'MaurynG',
        'title': 'Blog Post 1',
        'content': 'My First Content',
        'date_posted': 'August 28, 2020'
    },
    {
        'author': 'MwendeG',
        'title': 'Blog Post 2',
        'content': 'My Second Content',
        'date_posted': 'August 29, 2020'
    }
]

# Create your views here.

def home(request):
    # Retrieve all posts from the database using the Post model
    context = {
        'posts': Post.objects.all()  # Querying all Post objects from the database
    }
    # Render the home.html template with the retrieved posts
    return render(request, 'blog/home.html', context)

def about(request):
    # Render the about.html template with the title 'About page'
    return render(request, 'blog/about.html', {'title': 'About page'})
