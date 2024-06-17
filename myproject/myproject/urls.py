from django.urls import path
from django.shortcuts import render

def home(request):
    return render(request, template_name='index.html')

def about(request):
    return render(request, 'about.html')

urlpatterns = [
    path('', home ),
    path('about/', about),
]