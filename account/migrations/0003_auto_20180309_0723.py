# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-09 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180309_0700'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='study_field',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
