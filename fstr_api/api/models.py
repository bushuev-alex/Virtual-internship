from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    email = models.EmailField(unique=True)
    name = models.TextField()


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()


class PerevalAdded(models.Model):
    STATUS = [('new', 'новый'),
              ('pending', 'ожидает_модерации'),
              ('accepted', 'принят'),
              ('rejected', 'отклонен')
              ]

    LEVELS = [("winter", ""),
              ("summer", "1А"),
              ("autumn", "1А"),
              ("spring", "")
              ]

    user_id = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    beautyTitle = models.TextField(default="")
    title = models.TextField(default="")
    other_titles = models.TextField(default="")
    level = models.TextField(default="", choices=LEVELS)
    connect = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=True)
    add_first_time = models.DateTimeField(null=True)
    coord_id = models.ForeignKey(Coords, null=True, on_delete=models.SET_NULL)
    status = models.CharField(default='new', choices=STATUS)


class PerevalAreas(models.Model):
    id_parent = models.IntegerField(null=True)
    title = models.TextField(default="")


class Images(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.TextField(default="")
    img = models.BinaryField()


class PerevalImages(models.Model):
    pereval_id = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Images, on_delete=models.CASCADE)


class SprActivitiesTypes(models.Model):
    title = models.TextField(default="")
