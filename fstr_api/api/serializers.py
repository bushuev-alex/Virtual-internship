from api.models import *
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'phone', 'name', ]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height', ]


class PerevalAddedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['user_id', 'beautyTitle', 'title', 'other_titles', 'level', 'connect', 'date_added', 'add_first_time',
                  'coord_id', 'status']


class PerevalAddedPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['beautyTitle', 'title', 'other_titles', 'level', 'connect', 'coord_id', 'status']


class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAreas
        fields = ['id_parent', 'title', ]


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['date_added', 'title', 'img', ]


class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ['pereval_id', 'image_id', ]


class SprActivitiesTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprActivitiesTypes
        fields = ['title', ]
