from django.shortcuts import render, redirect
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

    def get(self, request, **kwargs):
        pk = self.kwargs.get('pk')
        email = self.kwargs.get('email')
        if pk:
            pereval_added = PerevalAdded.objects.get(pk=pk)
            serializer = PerevalAddedSerializer(pereval_added)
        elif email and Users.objects.filter(email=email).exists():
            pereval_added = PerevalAdded.objects.filter(user_id__email=f'{email}')
            serializer = PerevalAddedSerializer(pereval_added, many=True)
        elif email and not Users.objects.filter(email=email).exists():
            return Response("User with this email doesn't exist", status=status.HTTP_400_BAD_REQUEST)
        else:
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

    def patch(self, request, pk):
        pereval_obj = PerevalAdded.objects.get(pk=pk)
        if pereval_obj.status == 'new':
            serializer = PerevalAddedPatchSerializer(pereval_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=0, status=status.HTTP_403_FORBIDDEN)


class AreasApiView(APIView):

    def get(self, request, *args, **kwargs):
        areas = PerevalAreas.objects.all()
        serializer = AreasSerializer(areas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {'id_parent': request.data.get('id_parent'),
                'title': request.data.get('title')}
        serializer = AreasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AreasViewset(viewsets.ViewSet):
#     queryset = PerevalAreas.objects.all()
#     serializer_class = AreasSerializer
#
#     def list(self, request):
#         queryset = PerevalAreas.objects.all()
#         serializer = AreasSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self):
#         pass


class ImagesApiView(APIView):

    def get(self, request, *args, **kwargs):
        imgs = Images.objects.all()
        serializer = ImagesSerializer(imgs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {'date_added': request.data.get('date_added'),
                'title': request.data.get('title'),
                'img': request.data.get('img')}
        serializer = ImagesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerevalImagesApiView(APIView):

    def get(self, request, *args, **kwargs):
        pereval_images = PerevalImages.objects.all()
        serializer = PerevalImagesSerializer(pereval_images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {'pereval_id': request.data.get('pereval_id'),
                'image_id': request.data.get('image_id')}
        serializer = PerevalImagesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SprActivitiesTypesApiView(APIView):

    def get(self, request, *args, **kwargs):
        sprs = SprActivitiesTypes.objects.all()
        serializer = SprActivitiesTypesSerializer(sprs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {'title': request.data.get('title')}
        serializer = SprActivitiesTypesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def redirect_swagger(*args):
    return redirect("swagger-ui")
