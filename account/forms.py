from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import User
from django.forms.models import ModelForm


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=254, label='Name')
    student_id = forms.CharField(max_length=254, label='Student ID')
    email = forms.EmailField(help_text='Required.')
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, )
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput, )

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'student_id', 'password1', 'password2')
