# -*- coding: utf-8 -*-
__author__ = 'brian'
__date__ = '2018/7/11 0011 15:44'


from django.conf.urls import url, include
from .views import WriteAlbumView, AllAlbumsView

urlpatterns = [
    # 文章阅读
    # url(r'^read/(?P<article_id>\d+)$', ArticleReadView.as_view(), name="article_read"),
    # 写相册
    url(r'^write/$', WriteAlbumView.as_view(), name="write_album"),
    # 照片上传
    # url(r'^album/upload/$', UploadAlbumView.as_view(), name="album_upload"),

    # 所有相册
    url(r'^all/$', AllAlbumsView.as_view(), name="all_albums"),
]