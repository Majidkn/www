from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<post_id>[\w-]+)', views.post, name='post'),
]