#!/usr/bin/python3 
# encoding: utf-8 

"""
@version: v1.0
@author: ligui
@contact: 1947346653@qq.com
@site: https://www.cnblogs.com/c-x-a
@software: PyCharm
@file: urls.py.py
@time: 2022/8/14 15:39
"""
from django.urls import path
from .views import *


urlpatterns = [
    path('info/', UserViewSet.as_view({'get':'list'})),
    path('login/', UserViewSet.as_view({'post':'login'})),
    path('validVcode/', UserViewSet.as_view({'post':'validVCode'})),
    path('userInfo/<phone>/', UserViewSet.as_view({'get':'retrieve', 'put': 'update', 'delete':'destroy'}))
]