# -*- coding: utf-8 -*-
__author__ = 'brian'
__date__ = '2018/7/11 0011 14:57'


from django.conf.urls import url, include
from .views import ArticleReadView, WriteArticleView, AllArticlesView

urlpatterns = [
    # 文章阅读
    url(r'^read/(?P<article_id>\d+)$', ArticleReadView.as_view(), name="article_read"),
    # 写文章
    url(r'^write/$', WriteArticleView.as_view(), name="write_article"),
    # 所有文章
    url(r'^all/$', AllArticlesView.as_view(), name="all_article"),
]