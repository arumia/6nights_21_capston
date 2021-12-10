# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
# movie_api/movies/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import WeatherSerializer
from .models import Weather

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

def working(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = '가입하지 않은 아이디이거나,<br>잘못된 비밀번호입니다.'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    @action(detail=False, methods=['post'])
    def delete_all(self, request):
        Weather.objects.all().delete()
        return Response('success')

    # @action(detail=False, methods=['get'])
    # def get_weather(self, request):
    #     queryset = Weather.objects.all().values("fcstTime", "temp", "rain")
    #     serializer = WeatherSerializer()
    #     return Response(serializer_class.data)