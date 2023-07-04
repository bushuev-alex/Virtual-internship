from django.contrib import admin
from api.models import *
# from modeltranslation.admin import TranslationAdmin


admin.site.register(Users)
admin.site.register(Coords)
admin.site.register(PerevalAdded)
admin.site.register(PerevalAreas)
admin.site.register(Images)
admin.site.register(PerevalImages)
admin.site.register(SprActivitiesTypes)

