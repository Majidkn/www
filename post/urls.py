from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<post_id>[\w-]+)/like', views.like_post, name='like_post'),
    url(r'^(?P<post_id>[\w-]+)/dislike', views.dislike_post, name='dislike_post'),
    url(r'^(?P<post_id>[\w-]+)/delete', views.delete_post, name='delete_post'),
    url(r'^(?P<post_id>[\w-]+)$', views.post, name='post'),

]