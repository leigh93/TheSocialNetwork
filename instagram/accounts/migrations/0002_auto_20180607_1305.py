# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='My Name', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profpic',
            field=models.ImageField(default='logo.png', upload_to='profile_images'),
        ),
    ]
