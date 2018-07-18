# -*- coding: utf-8 -*-
__author__ = 'brian'
__date__ = '2018/7/11 0011 17:05'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Suggestion


class BaseSetting(object):
    """主题"""
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """页面设计 抬头 页尾  菜单样式"""
    site_title = "我的博客"
    site_footer = "myblog - blog"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class SuggestionAdmin(object):
    list_display = ['name', 'content', 'add_time']
    search_fields = ['name', 'content']
    list_filter = ['name', 'content', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Suggestion, SuggestionAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)