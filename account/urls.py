from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.HomeView, name='base'),
    # url(r'^home', views.HomeView, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^(?P<username>[\w-]+)', views.profile, name='profile'),
]
