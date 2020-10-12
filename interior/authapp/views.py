from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth

from authapp.models import ShopUser
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm


# Create your views here.

def login(request):
    login_form = ShopUserLoginForm(data=request.POST)

    next = request.GET['next'] if 'next' in request.GET.keys() else '' # получает значение страницы, с которой был перенаправлен пользователь

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password) # проверка наличия пользователя в базе
        if user and user.is_active: # если юзер существует и он активен
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main:index'))
    
    content = {
        'page_name': 'login',
        'login_form': login_form,

        'next': next,
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    register_form = ShopUserRegisterForm(request.POST, request.FILES)

    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {
        'page_name': 'register',
        'register_form': register_form,
    }
    return render(request, 'authapp/register.html', content)


def edit(request):
    edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

    if request.method == 'POST':
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {
        'page_name': 'edit user',
        'edit_form': edit_form,
    }
    return render(request, 'authapp/edit.html', content)
