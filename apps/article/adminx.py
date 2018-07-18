# -*- coding: utf-8 -*-
__author__ = 'brian'
__date__ = '2018/7/11 0011 17:08'


import xadmin

from .models import Article


class ArticleAdmin(object):
    list_display = ['title', 'sub_title', 'writer', 'category', 'add_time']
    search_fields = ['title', 'sub_title', 'writer', 'category']
    list_filter = ['title', 'sub_title', 'writer', 'category', 'add_time']


xadmin.site.register(Article, ArticleAdmin)