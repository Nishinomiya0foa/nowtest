# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-12 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='image/default.jpg', upload_to='image/%Y/%m', verbose_name='头像'),
        ),
    ]
