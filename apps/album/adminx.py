# -*- coding: utf-8 -*-
__author__ = 'brian'
__date__ = '2018/7/11 0011 17:11'


import xadmin

from .models import Album


class AlbumAdmin(object):
    list_display = ['image', 'name', 'desc', 'tag', 'add_time']
    search_fields = ['image', 'name', 'desc', 'tag']
    list_filter = ['image', 'name', 'desc', 'tag', 'add_time']


xadmin.site.register(Album, AlbumAdmin)

