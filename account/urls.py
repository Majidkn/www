from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from account.forms import LoginForm
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^$', views.HomeView, name='base'),
    # url(r'^home', views.HomeView, name='home'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login', views.login, name='login'),
    url(r'^new_post', views.new_post, name='new_post'),
    url(r'^(?P<username>[\w-]+)', views.profile, name='profile'),
]
