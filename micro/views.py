from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import ProfileForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

# base teemplate rendering
def base(request):
    return render(request, 'micro/base.html')


def aboutus(request):
    return render(request, 'micro/aboutus.html')
    


def home(request):
    # projects = Project.objects.all()
    return render(request, 'micro/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'micro/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('setprofile')
            except IntegrityError:
                return render(request, 'micro/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'micro/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})


def set_user_profile(request):
    if request.method == 'GET':
        return render(request, 'micro/set_user_profile.html', {'pro_form':ProfileForm()})
    else:
        try:
            form = ProfileForm(request.POST)
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.name = request.user
            new_profile.save()
            return redirect('home')
        except ValueError:
            return render(request, 'micro/set_user_profile.html', {'pro_form':ProfileForm(), 'error':'Bad data passed in. Try again.'})






def loginuser(request):
    if request.method == 'GET':
        return render(request, 'micro/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'micro/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')
