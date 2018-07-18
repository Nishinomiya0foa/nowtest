# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.base import ContentFile
import os

from .models import Album
from .forms import UploadAlbumForm
from MyBlog import settings

# Create your views here.


# class UploadAlbumView(LoginRequiredMixin, View):
#     """上传照片"""
#     login_url = '/login/'
#
#     def post(self, request):
#         image_form = UploadAlbumForm(request.POST, request.FILES)
#
#         if image_form.is_valid():
#             image = image_form.cleaned_data['image']
#             the_album = Album.objects.get()
#             the_album.image = image
#             the_album.save()
#             return HttpResponse('{"status": "success"}', content_type='application/json')
#         else:
#             return HttpResponse('{"status": "fail"}', content_type='application/json')


class WriteAlbumView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "write_album.html", {})

    def post(self, request):
        name = request.POST.get("name", "")
        image = request.FILES.get("image", "")
        tag = request.POST.get("tag", "")
        desc = request.POST.get("desc", "")
        is_show = request.POST.get("is_show", "")
        writer = request.user.id
        if image and name and desc:
            the_album = Album()
            the_album.name = name
            the_album.image = image
            the_album.tag = tag
            the_album.desc = desc
            if is_show == "不展示":
                the_album.is_show = 0
            else:
                the_album.is_show = 1
            the_album.writer_id = writer
            the_album.save()
            # image.save()
            return HttpResponse('{"status":"success", "msg":"上传成功！"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"上传失败！"}', content_type='application/json')


class AllAlbumsView(LoginRequiredMixin, View):
    """所有照片展示"""
    login_url = '/login/'

    def get(self, request):
        # 所有照片
        all_albums = Album.objects.all().order_by("-add_time")

        # 对所有照片进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_albums, 4, request=request)

        albums = p.page(page)

        return render(request, "all_albums.html", {
            'all_albums': albums,
        })

