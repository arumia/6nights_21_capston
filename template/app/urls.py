# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views


urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    path("rfid/", views.rfid, name="rfid"),
    path("job/", views.job, name="job"),
    path("job-list.html", views.job_list, name="job_list"),
    path("geosave/<int:id>/", views.geosave, name="geosave"),
    path("farmsave/<int:id>/", views.farmsave, name="farmsave"),
    path("delete/<int:id>/", views.delete, name="delete"),
    re_path(r'^.*\.*', views.pages, name='pages'),

]
