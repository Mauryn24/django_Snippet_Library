from django.shortcuts import render  # Importing the render function from Django shortcuts
from .models import Post  # Importing the Post model from the current directory's models module


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
