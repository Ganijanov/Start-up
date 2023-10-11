from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from main import models
from . import serializers as ser
from rest_framework.views import APIView
from rest_framework import generics, filters, status
from datetime import timedelta, datetime
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination


class UserListView(APIView):

    def get(self, request):
        user = models.User.objects.filter(status=2)
        user_ser = ser.UserSerializer(user, many = True)
        return Response(user_ser.data)


class UserDetailView(APIView):

    def get_queryset(self, pk):
        user = models.User.objects.get(pk=pk)
        
        return user

    def get(self, request, pk):
        user_ser = ser.UserSerializer(self.get_queryset(pk = pk))
        blog_ser = ser.BlogSerializer(models.Blog.objects.filter(author = self.get_queryset(pk=pk)), many = True)
        helpless_ser = ser.HelplessSerializer(models.Helpless.objects.filter(created_by = self.get_queryset(pk=pk)), many = True)
        return Response({
            'user':user_ser.data,
            'blogs':blog_ser.data,
            'helpless-list':helpless_ser.data
        })


class HelplessListView(APIView):

    def get_queryset(self):
        helpless = models.Helpless.objects.all()
        # name = self.request.query_params.get('name')
        # city_id = self.request.query_params.get('city_id')
        # jshshr = self.request.query_params.get('jshshr')
        # help_type_id = self.request.query_params.get('help_type_id')

        # if name:
        #     helpless.filter(name__icontains=name)
        # if city_id:
        #     helpless.filter(city__id=city_id)
        # if jshshr:
        #     helpless.filter(jshshr__icontains=jshshr)
        # if help_type_id:
        #     helpless.filter(help_type__id=help_type_id)
        

        helpless_list = []
        for i in helpless:
            helpless_info = {
                'id': i.id,
                'name': i.name,
                'last_name': i.last_name,
                'city': i.city.title,
                'birthday': i.birthday,
                'created': i.created,
                'help_type': ser.HelpTypeSerializer(i.help_type.all(), many = True).data,
                'images': ser.HelplessMediaSerializer(models.HelplessMedia.objects.filter(helpless = i), many = True).data
            }
            helpless_list.append(helpless_info)

        return helpless_list

    def get(self, request):
        return Response(self.get_queryset())


class HelplessDetailView(APIView):

    def get_queryset(self, pk):
        helpless = models.Helpless.objects.get(pk=pk)
        return helpless

    def get(self, request, pk):
        helpless = ser.HelplessSerializer(self.get_queryset(pk=pk)).data
        h_media = ser.HelplessMediaSerializer(models.HelplessMedia.objects.filter(helpless = self.get_queryset(pk = pk)), many = True).data
        return Response([helpless, {'images':h_media}])
    

class BlogListView(APIView):

    def get_queryset(self):
        blog = models.Blog.objects.all()
        blog_list = []

        for i in blog:
            blog_info = {
                'title': i.title,
                'author': i.author.username,
                'created':i.created,
                'img': ser.BlogMediaSerializer(models.BlogMedia.objects.filter(blog = i)[:2 ], many = True).data
            }
            
            blog_list.append(blog_info)
        return blog_list

    def get(self, request):
        return Response(self.get_queryset())
    

class BlogDetailView(APIView):

    def get_queryset(self, pk):
        blog = models.Blog.objects.get(pk = pk)
        return blog
    
    def get(self, request, pk):
        blog_ser = ser.BlogSerializer(self.get_queryset(pk = pk)).data
        b_media = ser.BlogMediaSerializer(models.BlogMedia.objects.filter(blog = self.get_queryset(pk = pk)), many = True).data
        return Response([blog_ser, b_media])
    
