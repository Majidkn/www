# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# coding=utf8

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.models import ModelForm

from account.models import User, StudyField


# from django.forms.models import ModelForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    # name = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
    student_id = forms.CharField(max_length=9, widget=forms.TextInput(
        attrs={'placeholder': 'شماره دانشجویی'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه'}), )
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'تکرار گذرواژه'}), )
    study_field = forms.ModelChoiceField(queryset=StudyField.objects.all(), )

    def clean_email(self):
        email = self.cleaned_data['email']
        if str(email).split('@')[1] != 'ut.ac.ir':
            raise forms.ValidationError("ایمیل باید با @ut.ac.ir تمام شود")
        return email

    def clean_password1(self):
        special_character = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+']
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']

        password = self.cleaned_data['password1']

        if not any(x in password for x in special_character) or not any(char.isdigit() for char in password) or not any(
                        x in password for x in alphabet):
            raise forms.ValidationError("رمزعبور باید دارای کارکترهای ویژه باشد")
        return password

    def clean_student_id(self):
        student_id = self.cleaned_data['student_id']
        if len(student_id) != 9:
            raise forms.ValidationError("باید ۹ تا باشه")
        return student_id

    class Meta:
        model = User
        fields = ('username', 'email', 'student_id', 'password1', 'password2', 'study_field')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class NewPostForm(forms.Form):
    body = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'بنویسید...'}))

    class Meta:
        model = User
        fields = 'body'
