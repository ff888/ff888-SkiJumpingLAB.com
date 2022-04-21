from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Jakub',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '21 April 2022'
    },
    {
        'author': 'JK',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '21 April 2022'
    }
]


def statistics(request):
    return render(request, 'ski_statistics/home.html', {'title': 'Statistics'})


def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'ski_statistics/blog.html', context)


def about(request):
    return render(request, 'ski_statistics/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'ski_statistics/ contact.html', {'title': 'Contact'})
