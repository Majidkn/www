# -*- coding: utf-8 -*-
import time
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

# Create your views here.
from account.forms import SignUpForm, LoginForm


def signup(request):
    message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_ = form.save(commit=False)
            user_.is_active = True
            user_.save()
            # created_user = authenticate(username=form.cleaned_data['username'],
            #                             password=form.cleaned_data['password1'])
            # login(request, created_user)

            return redirect('login')
        else:
            message = "اطلاعات نامعتبر است"

    else:
        form = SignUpForm()

    return render(request, 'account/_signup.html', {'form': form, 'message': message})


def login(request):
    message = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponse('شما با موفقیت لاگین شدید')
            else:
                message = "نام کاربری یا گذرواژه اشتباه است"
    else:
        form = LoginForm()

    return render(request, 'account/_login.html', {'form': form, 'message': message})


def profile(request):
    current_user = request.user

    return render(request, 'account/_profile.html', {
        'user': current_user
    })
