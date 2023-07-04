from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import *
from api.models import *


class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CoordViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class PerevalAddedViewest(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer


class ImagesViewest(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalImagesViewest(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = PerevalImagesSerializer


class SprActivitiesTypesViewest(viewsets.ModelViewSet):
    queryset = SprActivitiesTypes.objects.all()
    serializer_class = SprActivitiesTypesSerializer
