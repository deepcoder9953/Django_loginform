from django.shortcuts import render, redirect
from django.http import HttpResponse
from loginpage import models
from .models import WangUser

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email') 

        error_name = []
        user_list = models.WangUser.objects.filter(username=username)

        if user_list.exists():
            error_name = "The user already exists"
            return render(request, 'register.html', {'error_name': error_name})
        else:
            new_user = models.WangUser.objects.create(username=username, password=password, email=email)
            new_user.save()

            return redirect('login')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        obj_user = models.WangUser.objects.filter(username=username,password=password)

        if obj_user:
            request.session['user'] = username
            request.session.set_expiry(300)
            return redirect('index')
    
        error = 'wrong password and username'
        return render(request, 'login.html', {'error':error})

    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['user']

    except:
        return redirect('login')
    return redirect('login') 
    
    
def index(request):
    username = request.session.get('user')
    return render(request, 'index.html', {'username': username})