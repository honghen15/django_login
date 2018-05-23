
# Create your views here.
import re
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(request)
        if user:
            login(request, user)
            #print(request.GET['next'])
            if request.GET.get('next', None):

                pass
                # return HttpResponseRedirect(reverse('photos'))
            print(request.user)
            request.session.modified = True
            request.session['username'] = username
            request.session['password'] = password
            #return HttpResponseRedirect('/test/')
            print(request.session['username'])
            print(request.session['password'] )
            return HttpResponseRedirect(reverse('index'))
        else:
            context['error'] = 'Provide valid credentials!!'
            return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', context)


# ================linebot相關功能已經彙整到一個py當中================


# 試用login logout

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(request)
        if user:
            login(request, user)
            print(request.GET['next'])
            if request.GET.get('next', None):

                pass
                # return HttpResponseRedirect(reverse('photos'))
            print(request.user)
            request.session.modified = True
            request.session['username'] = username
            request.session['password'] = password
            #return HttpResponseRedirect('/test/')
            print(request.session['username'])
            print(request.session['password'] )
            return HttpResponseRedirect('/index/')
        else:
            context['error'] = 'Provide valid credentials!!'
            return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', context)

@csrf_exempt
def success(request):
    context = {}
    context['user'] = request.user
    #return render(request, 'auth/success.html', context )
    return render(request, 'auth/success.html', locals())

def user_logout(request):
    print(request)
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('index'))


# @login_required
def home(request):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    # else:
    #     return render(request, 'home.html', locals())
    # context = {}
    # context['user'] = request.user
    return render(request, 'home.html')
    # return render(request, 'home.html', locals())