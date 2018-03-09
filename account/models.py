from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=254, blank=True)
    student_id = models.CharField(max_length=9, blank=True)
    email = models.EmailField(blank=True)
    avatar = models.ImageField(upload_to='pic_folder/', default='pic_folder/__none/no-img.png')