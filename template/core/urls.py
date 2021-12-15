# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from rest_framework import routers
from app.views import WeatherViewSet

router = routers.DefaultRouter()
router.register('weather', WeatherViewSet) # prefix = movies , viewset = MovieViewSet
router.register('work', WorkViewSet) # prefix = movies , viewset = MovieViewSet

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path('api/', include(router.urls)),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls"))             # UI Kits Html files
]
