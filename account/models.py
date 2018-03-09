from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=254, blank=True)
    student_id = models.CharField(max_length=9, blank=True)
    email = models.EmailField(blank=True)
    study_field = models.CharField(max_length=254, blank=True)


class StudyField(models.Model):
    name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name.encode('utf-8')
