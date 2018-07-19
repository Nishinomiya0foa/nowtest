# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name=u"昵称", default='')
    photo = models.ImageField(upload_to="image/%Y/%m", default="", max_length=100, verbose_name=u"头像")
    desc = models.CharField(max_length=100, verbose_name=u"个性签名", default='')

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register", u"注册"), ("forget", u"找回密码"), ("update_email", u"修改邮箱")),
                                 max_length=30, verbose_name=u"验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")  # now后面要把（）去掉  这样才是实例化的时间 否则是class的时间

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Suggestion(models.Model):
    name = models.CharField(max_length=16, verbose_name=u"名字", default="")
    content = models.CharField(max_length=200, verbose_name=u"内容", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户留言"
        verbose_name_plural = verbose_name


class UserShow(models.Model):
    show_id = models.IntegerField(default=0, verbose_name=u"数据ID")
    show_type = models.IntegerField(choices=((1, "照片"), (2, "文章")), default=1, verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"展示内容"
        verbose_name_plural = verbose_name



