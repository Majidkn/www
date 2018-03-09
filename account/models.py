from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from post.models import Post


class User(AbstractUser):
    name = models.CharField(max_length=254, blank=True)
    student_id = models.CharField(max_length=9, blank=True)
    email = models.EmailField(blank=True)
    study_field = models.CharField(max_length=254, blank=True)
    avatar = models.ImageField(upload_to='pic_folder/', default='pic_folder/__none/no-img.png')


class StudyField(models.Model):
    name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

