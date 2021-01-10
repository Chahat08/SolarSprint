from django.shortcuts import render
from .forms import UserForm, UserGameInfoForm
from .models import User, UserGameInfo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'solarsprint/home.html', {})

#def login(request):
    #return render(request, 'solarsprint/login.html', {})


def log_in(request):
    return render(request,'solarsprint/login.html', {})

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('account_details'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        game_form = UserGameInfoForm(data=request.POST)
        #profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and game_form.is_valid():#and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            game_info = game_form.save(commit=False)
            game_info.user = user
            #profile = profile_form.save(commit=False)
            #profile.user = user
            #if 'profile_pic' in request.FILES:
             #   print('found it')
              #  profile.profile_pic = request.FILES['profile_pic']
            #profile.save()
            registered = True
        else:
            print(user_form.errors)#,profile_form.errors)
    else:
        user_form = UserForm()
        #profile_form = UserProfileInfoForm()
    return render(request,'solarsprint/registration.html',
                          {'user_form':user_form,
                           #'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('account_details'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'solarsprint/login.html', {})

def account_details(request):
    if request.method=='GET':
        print("in get")
        game_info = UserGameInfo(request.GET)
        return render(request, 'solarsprint/account.html', {'game_info':game_info})
    else:
        print("in else")
        return render(request, 'solarsprint/login.html', {})

def prithvia(request):
    return render(request, 'solarsprint/game.html', {'planet':'prithvia'})
def galnerth(request):
    return render(request, 'solarsprint/game.html', {'planet':'nirus'})
def nirus(request):
    return render(request, 'solarsprint/game.html', {'planet':'galnerth'})

def explore_planets(request):
    return render(request, 'solarsprint/explore_planets.html', {})

def explore_sprinters(request):
    return render(request, 'solarsprint/explore_sprinters.html', {})

