# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models

from users.models import UserProfile
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20, default='', verbose_name=u"标题")
    is_show = models.BooleanField(default=True, verbose_name=u"是否展示")
    sub_title = models.CharField(max_length=80, default='', verbose_name=u"副标题")
    writer = models.ForeignKey(UserProfile, verbose_name=u"作者")
    category = models.CharField(choices=(("sb", "随笔"), ("rj", "日记"), ("yj", "游记")), max_length=2, verbose_name=u"分类",
                                default="sb")
    content = models.TextField(verbose_name=u"内容")
    content_show = models.CharField(max_length=150, verbose_name=u"展示内容", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
