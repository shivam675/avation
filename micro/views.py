from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import ContactForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from projects.models import Project, Division, Tag
from .models import Contact



# Create your views here.

# base teemplate rendering
def base(request):
    return render(request, 'micro/base.html')


def aboutus(request):
    return render(request, 'micro/aboutus.html')



def home(request):
    projects = Project.objects.all()
    # get_object_or_404()
    divs = Division.objects.all()
    tags = Tag.objects.filter()
    return render(request, 'micro/home.html', {'projects':projects, 'divs':divs, 'tags':tags})

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

@login_required
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




def ContactCreate(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            number = request.POST.get('number')
            message = request.POST.get('message')
            obj = Contact.objects.create(first_name=first_name, last_name=last_name, number=number, message=message)
            obj.save()
            return redirect('thanks')
        else:
            form = ContactForm()
            return render(request, 'micro/contact_form.html',{ 'error': 'Something went wrong. Please try again !' ,'comment_form':form})
    else:
        form = ContactForm()
        return render(request, 'micro/contact_form.html',{'comment_form':form})

def thanks(request):
    return render(request, 'micro/thanks.html')
