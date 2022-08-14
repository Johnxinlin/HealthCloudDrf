from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_400_BAD_REQUEST

from user.models import UserInfo
from user.serializers import UserSerializers
from rest_framework import viewsets


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        user = UserInfo.objects.all()
        serializer = UserSerializers(user, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception='True')
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, phone):
        try:
            print(type(phone))
            user = UserInfo.objects.get(phone=phone)
        except UserInfo.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = UserSerializers(user)
        return Response(serializer.data)

    def update(self, request, phone):
        try:
            user = UserInfo.objects.get(phone=phone)
        except UserInfo.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = UserSerializers(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def destroy(self, request, phone):
        try:
            user = UserInfo.objects.get(phone=phone)
        except UserInfo.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def login(self, request):
        try:
            print(request.data)
            phone = request.data['phone']
            password = request.data['password']
            user = UserInfo.objects.get(phone=phone, password=password)
        except UserInfo.DoesNotExist:
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(status=HTTP_200_OK)

    def validVCode(self, request):
        vCode = request.data['vCode']
        print(request.data)
        dic = request.data
        dic.pop('vCode')
        print(dic)
        if vCode == '888888':
            serializer = UserSerializers(data=dic)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(HTTP_200_OK)
        else:
            return Response(HTTP_400_BAD_REQUEST)


