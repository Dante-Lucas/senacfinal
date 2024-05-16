from django.shortcuts import render,redirect
from .models import User
from .backend import MyBackend
from django.urls import reverse
from django.http import HttpResponse,HttpRequest
from django.contrib import auth

# Create your views here.
def register(request:HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        template_name = "registration/cadastro.html"
        return render(request,template_name)
    elif request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('repeat_password')

        users = User.objects.filter(username=username,email=email)

        if users.exists():
            return HttpResponse('usuário já existe')
        try:
            user=User.objects.create_user(username=username,email=email,password=confirm_password)
            return redirect(reverse(login))
        except:
            return HttpResponse('não foi') 

def login(request:HttpRequest) -> HttpResponse:
    if request.method == 'GET':
    
        template_name = "registration/login.html"
        return render(request,template_name)
    elif request.method == 'POST':
    
        username = request.POST.get('name')
        password = request.POST.get('password')

        users =auth.authenticate(request,username=username,password=password)
        if users:
            auth.login(request,users)
            return redirect('/home/dashboard')
    template_name = "registration/login.html"
    return render(request,template_name)


