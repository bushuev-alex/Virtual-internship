from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *
from api.models import *


class UsersApiView(APIView):

    def get(self, request, *args, **kwargs):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {'email': request.data.get('email'),
                'phone': request.data.get('phone'),
                'name': request.data.get('name')}
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoordsApiView(APIView):

    def get(self, request, *args, **kwargs):
        coords = Coords.objects.all()
        serializer = CoordsSerializer(coords, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {'latitude': request.data.get('latitude'),
                'longitude': request.data.get('longitude'),
                'height': request.data.get('height')}
        serializer = CoordsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerevalAddedApiView(APIView):

    def get(self, request, *args, **kwargs):
        pereval_added = PerevalAdded.objects.all()
        serializer = PerevalAddedSerializer(pereval_added, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {'user_id': request.data.get('user_id'),
                'beautyTitle': request.data.get('beautyTitle'),
                'title': request.data.get('title'),
                'other_titles': request.data.get('other_titles'),
                'level': request.data.get('level'),
                'connect': request.data.get('connect'),
                'date_added': request.data.get('date_added'),
                'add_first_time': request.data.get('add_first_time'),
                'coord_id': request.data.get('coord_id'),
                'status': request.data.get('status')}
        serializer = PerevalAddedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImagesViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalImagesViewset(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = PerevalImagesSerializer


class SprActivitiesTypesViewset(viewsets.ModelViewSet):
    queryset = SprActivitiesTypes.objects.all()
    serializer_class = SprActivitiesTypesSerializer
