"""
        URL configuration for fstr_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
from api import views
# from django.shortcuts import redirect
# router = routers.DefaultRouter()
# router.register(r'users', views.UsersApiView.as_view())
# router.register(r'coords', views.CoordsViewset)
# router.register(r'perevaladded', views.PerevalAddedViewset)
# router.register(r'images', views.ImagesViewset)
# router.register(r'areas', views.AreasViewset)
# router.register(r'perevalimages', views.PerevalImagesViewset)
# router.register(r'spractivitiestypes', views.SprActivitiesTypesViewset)


urlpatterns = [
    path("admin/", admin.site.urls),
    # path(r'', include(router.urls)),
    path(r'', views.redirect_swagger),
    path(r'users', views.UsersApiView.as_view()),
    path(r'coords', views.CoordsApiView.as_view()),
    path(r'perevaladded', views.PerevalAddedApiView.as_view()),
    path(r'perevaladded/<int:pk>', views.PerevalAddedApiView.as_view()),
    path(r'areas', views.AreasApiView.as_view()),
    path(r'images', views.ImagesApiView.as_view()),
    path(r'perevalimages', views.PerevalImagesApiView.as_view()),
    path(r'sprtypes', views.SprActivitiesTypesApiView.as_view()),
    path(r'perevaladded/<email>', views.PerevalAddedApiView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger-ui/', TemplateView.as_view(template_name='swagger-ui.html',
                                             extra_context={'schema_url': 'openapi-schema.yml'}), name='swagger-ui'),
]
