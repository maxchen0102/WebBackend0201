from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': '首頁',
        'content': '歡迎來到chris的網站'
    }

    return render(request, 'blog/index.html', context)
