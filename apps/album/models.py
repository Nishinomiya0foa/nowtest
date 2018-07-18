# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models

from users.models import UserProfile

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=14, verbose_name=u"照片名", default="")
    image = models.ImageField(upload_to="album/%Y/%m", verbose_name=u"照片", max_length=100)
    is_show = models.BooleanField(default=True, verbose_name=u"是否展示")
    writer = models.ForeignKey(UserProfile, verbose_name=u"作者", default="2")
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    tag = models.CharField(max_length=20, verbose_name=u"标签")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"相册"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
