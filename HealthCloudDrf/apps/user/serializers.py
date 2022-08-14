#!/usr/bin/python3 
# encoding: utf-8 

"""
@version: v1.0
@author: ligui
@contact: 1947346653@qq.com
@site: https://www.cnblogs.com/c-x-a
@software: PyCharm
@file: serializers.py.py
@time: 2022/8/14 14:38
"""
from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo

        exclude = ['is_delete']
        extra_kwarg = {
            'age': {'min_value': 0, 'max_value': 200}
        }

    # 追加对象级别的校验
    # def validate(self, data):
    #     if 'test' not in data['name'].lower() and data['name']:
    #         raise serializers.ValidationError('用户名必须包含test')
    #     return data
