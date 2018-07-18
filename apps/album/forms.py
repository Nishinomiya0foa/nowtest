# _*_ coding:utf-8 _*_
__author__ = 'brian'
__date__ = '2018/7/17 0017 17:35'
from django import forms

from .models import Album


class UploadAlbumForm(forms.ModelForm):
    # 上传照片
    class Meta:
        model = Album
        fields = ['image']