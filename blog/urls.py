# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello_world, name='hello'),
    path('greet/<str:name>/', views.greet_user, name='greet'),
]