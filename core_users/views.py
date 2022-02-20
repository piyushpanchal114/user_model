from django.shortcuts import render
from django.http import HttpResponse
from . models import User

# Create your views here.

def login_form(request):
    return render(request, 'home.html')

def signup_form(request):
    return render(request, 'sign_up.html')

def users_detail(request):
    user = User.objects.all()
    return render(request, 'users.html', {'users': user})

