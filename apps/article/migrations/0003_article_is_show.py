# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-13 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_content_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='是否展示'),
        ),
    ]