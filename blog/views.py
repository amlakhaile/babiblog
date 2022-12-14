from django.shortcuts import render
from .models import Post

posts = [
    {
        'author' : 'babi',
        'title' : 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'December 7, 2022'
    },
    {
        'author' : 'hafi',
        'title' : 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'December 8, 2022'
    }
]

def home(request):
    context = {
       'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
