# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from lxml import etree
import requests
import time
import json

from article.models import Article
from album.models import Album
from .forms import LoginForm, UploadPhotoForm, UserInfoForm
from .models import UserProfile, Suggestion, UserShow
# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(View):
    def get(self, request):
        """主页面展示"""
        # 爬取Acfun 囧图链接
        url = 'http://www.acfun.cn/u/2648570.aspx'
        data = requests.get(url).text
        s = etree.HTML(data)
        joke_title = s.xpath('//*[@id="listArticle"]/div[1]/figure[1]/a/@title')[0]
        joke_href = s.xpath('//*[@id="listArticle"]/div[1]/figure[1]/a/@href')[0]

        # 照片展示
        photo1 = Album.objects.filter(is_show=True).order_by("-add_time")[0]
        photo2 = Album.objects.filter(is_show=True).order_by("-add_time")[1]
        photo3 = Album.objects.filter(is_show=True).order_by("-add_time")[2]

        # 文章展示
        articles = Article.objects.filter(is_show=True).order_by("-add_time")[:4]

        # 日期
        date_time = time.strftime("%Y-%m-%d")

        return render(request, "index.html", {
            'joke_title': joke_title,
            'joke_href': joke_href,
            'photo1': photo1,
            'photo2': photo2,
            'photo3': photo3,
            'articles': articles,
            'date_time': date_time,
        })


class LogoutView(View):
    """登出"""
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class LoginView(View):
    """登录"""
    def get(self, request):
        login_form = LoginForm()
        return render(request, "login.html", {
            "login_form": login_form
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "login.html", {
                    "msg": "用户名或密码错误",
                })
        else:
            return render(request, "login.html", {
                "login_form": login_form,
            })


class SuggestionView(View):
    """用户评论页"""
    def get(self, request):
        # 获取所有建议
        all_contents = Suggestion.objects.all().order_by("-add_time")
        # 对所有建议进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_contents, 5, request=request)

        contents = p.page(page)

        return render(request, "suggestion.html", {
            'all_contents': contents,
        })

    def post(self, request):
        """添加留言"""
        name = request.POST.get("name", "")
        contents = request.POST.get("content", "")
        if contents:
            user_contents = Suggestion()
            user_contents.name = name
            user_contents.content = contents
            user_contents.save()
            return HttpResponse('{"status":"success", "msg":"留言成功！"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"留言失败！"}', content_type='application/json')


class UserCenterView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request):
        return render(request, "usercenter.html", {

        })

    def post(self, request):
        photo_form = UploadPhotoForm(request.POST, request.FILES)
        # photo_now = request.FILES.get("image")
        if photo_form.is_valid():
            photo = photo_form.cleaned_data['photo']
            request.user.photo = photo
            request.user.save()
            return HttpResponse("{'status':'success'}", content_type='application/json')

        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')


class AddShowView(View):
    """添加展示， 取消展示"""
    def post(self, request):
        is_show = request.POST.get('is_show', 0)
        the_article = Article()
        if is_show:
            the_article.is_show = 0
            return HttpResponse('{"status": "success", "msg": "取消展示"}', content_type='application/json')
        else:
            the_article.is_show = 1
            return HttpResponse('{"status": "success", "msg": "添加展示"}', content_type='application/json')

        # # 取出 两个数据
        # show_id = request.POST.get('show_id', 0)
        # show_type = request.POST.get('show_type', 0)
        #
        # # if not request.user.is_authenticated():
        # #     # 用户未登录
        # #     return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type='application/json')
        #
        # exist_records = UserShow.objects.filter(show_id=int(show_id), show_type=int(show_type))
        # if exist_records:
        #     # 如果记录存在 需求为取消收藏
        #     exist_records.delete()
        #     # # 并将收藏数 -1
        #     # if int(fav_type) == 1:
        #     #     course = Course.objects.get(id=int(fav_id))
        #     #     course.fav_nums -= 1
        #     #     if course.fav_nums < 0:
        #     #         course.fav_nums = 0
        #     #     course.save()
        #     # elif int(fav_type) == 2:
        #     #     course_org = CourseOrg.objects.get(id=int(fav_id))
        #     #     course_org.fav_nums -= 1
        #     #     if course_org.fav_nums < 0:
        #     #         course_org.fav_nums = 0
        #     #     course_org.save()
        #     # elif int(fav_type) == 3:
        #     #     teacher = Teacher.objects.get(id=int(fav_id))
        #     #     teacher.fav_nums -= 1
        #     #     if teacher.fav_nums < 0:
        #     #         teacher.fav_nums = 0
        #     #     teacher.save()
        #
        #     return HttpResponse('{"status": "success", "msg": "收藏"}', content_type='application/json')
        #
        # else:
        #     user_show = UserShow()
        #     if int(show_id) > 0 and int(show_type) > 0:
        #         # user_show.user = request.user
        #         user_show.show_id = int(show_id)
        #         user_show.show_type = int(show_type)
        #         user_show.save()
        #         # # 将收藏数 +1
        #         # if int(fav_type) == 1:
        #         #     course = Course.objects.get(id=int(fav_id))
        #         #     course.fav_nums += 1
        #         #     course.save()
        #         # elif int(fav_type) == 2:
        #         #     course_org = CourseOrg.objects.get(id=int(fav_id))
        #         #     course_org.fav_nums += 1
        #         #     course_org.save()
        #         # elif int(fav_type) == 3:
        #         #     teacher = Teacher.objects.get(id=int(fav_id))
        #         #     teacher.fav_nums += 1
        #         #     teacher.save()
        #         return HttpResponse('{"status": "success", "msg": "已收藏"}', content_type='application/json')
        #     else:
        #         return HttpResponse('{"status": "fail", "msg": "收藏失败"}', content_type='application/json')