# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
import json

from article.models import Article
from users.models import UserShow
# Create your views here.


class ArticleReadView(View):
    """阅读文章"""
    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        return render(request, 'article.html', {
            'article': article,
        })


class WriteArticleView(LoginRequiredMixin, View):
    """写文章"""
    # def post(self, request):
    #     # 昵称 生日..表单提交
    #     # instance=request.user 指定当前用户
    #     user_info_form = UserInfoForm(request.POST, instance=request.user)
    #     if user_info_form.is_valid():
    #         user_info_form.save()
    #         return HttpResponse('{"status": "success"}', content_type='application/json')
    #     #        return render(request, "usercenter-info.html", {})
    #     else:
    #         return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')
    login_url = '/login/'

    def get(self, request):
        return render(request, "write_article.html", {})

    def post(self, request):
        title = request.POST.get("title", "")
        is_show = request.POST.get("is_show", "")
        sub_title = request.POST.get("sub_title", "")
        content = request.POST.get("content", "")
        category = request.POST.get("category", "")
        writer = request.user.id
        if title and content and sub_title:
            article = Article()
            article.title = title
            article.category = category
            article.is_show = is_show
            article.sub_title = sub_title
            article.content = content
            article.writer_id = writer
            article.save()
            return HttpResponse('{"status":"success", "msg":"上传成功！"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"上传失败！"}', content_type='application/json')


class AllArticlesView(LoginRequiredMixin, View):
    """文章总览"""
    login_url = '/login/'

    def get(self, request):
        # 所有文章
        all_articles = Article.objects.all().order_by("-add_time")
        # 对所有文章进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_articles, 8, request=request)

        articles = p.page(page)
        return render(request, "all_articles.html", {
            'all_articles': articles,
            # 'has_show': has_show,
        })


