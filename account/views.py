# -*- coding: utf-8 -*-
import time
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

# Create your views here.
from account.forms import SignUpForm, LoginForm, NewPostForm
from account.models import User
from post.models import Post, Comment, Like, DisLike


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
                if user.is_staff or user.is_superuser:
                    return redirect('admin')
                else:
                    return redirect('home')
            else:
                message = "*نام کاربری یا گذرواژه اشتباه است"
    else:
        form = LoginForm()

    return render(request, 'account/_login.html', {'form': form, 'message': message})


def profile(request, username):
    # current_user = request.user
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user_id=user.id)
    for post in posts:
        comments = Comment.objects.filter(post_id=post.id)
        likes = Like.objects.filter(post_id=post.id)
        dislikes = DisLike.objects.filter(post_id=post.id)
        post.comments = len(comments)
        post.likes = len(likes)
        post.dislikes = len(dislikes)
    return render(request, 'account/_profile.html', {
        'user': user,
        'posts': posts,
    })

def new_post(request):
        if request.method == 'POST':
            form = NewPostForm(request.POST)
            if form.is_valid():
                body = form.cleaned_data['body']
                post = Post(body=body, user=request.user)
                post.save()
                return redirect('/account/'+request.user.username)
        else:
            form = NewPostForm()
        return render(request, 'account/_new_post.html', {'form': form})
