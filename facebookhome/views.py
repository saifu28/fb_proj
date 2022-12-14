from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render (request, 'facebook_template/homepage.html')

def signup(request):
    return render (request, 'facebook_template/signup.html')

def page(request):
    return render (request, 'facebook_template/page.html')

