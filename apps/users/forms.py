# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2018/7/13 0013 17:36'

"""表单"""
from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误！"})


class UploadPhotoForm(forms.ModelForm):
    #
    class Meta:
        model = UserProfile
        fields = ['photo']