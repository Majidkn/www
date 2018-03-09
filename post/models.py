from django.conf import settings
from django.db import models

# Create your models here.
from account.models import User


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField(max_length=280)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField(max_length=100, null=False, blank=False)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class DisLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)