# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-09 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180309_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='pic_folder/__none/no-img.png', upload_to='pic_folder/'),
        ),
    ]
