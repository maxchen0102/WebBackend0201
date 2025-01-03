from django.http import HttpResponse
from django.shortcuts import render
import os


def index(request):
    context = {
        'title': '首頁',
        'content': '歡迎來到chris的網站',
        'SECRET_KEY': os.environ.get('SECRET_KEY'),
    }

    return render(request, 'blog/index.html', context)


def hello_world(request):
    return HttpResponse("Hello, World!")


def greet_user(request, name):
    return HttpResponse(f"Hello, {name}!")
