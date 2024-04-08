from django.shortcuts import render
from django.http import HttpResponse

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
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About page'})
