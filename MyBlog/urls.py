# -*- coding: utf-8 -*-
"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from MyBlog.settings import MEDIA_ROOT
from users.views import IndexView, LoginView, SuggestionView, UserCenterView, LogoutView, AddShowView
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name="index"),
    # 登录
    url('^login/$', LoginView.as_view(), name="login"),
    # 登出
    url('^logout/$', LogoutView.as_view(), name="logout"),
    # 添加展示
    url(r'^add_show/$', AddShowView.as_view(), name="add_show"),
    # 用户留言
    url('^suggestion/$', SuggestionView.as_view(), name="suggestion"),
    # 用户中心
    url('^usercenter/$', UserCenterView.as_view(), name="user_center"),

    # 配置上传文件的访问处理函数
    url(r'^image/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 验证码
    url(r'^captcha/', include('captcha.urls')),
    # article信息urls转发
    url(r'^article/', include('article.urls', namespace="article")),
    # album信息urls转发
    url(r'^album/', include('album.urls', namespace="album")),
]
