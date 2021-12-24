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
from .serializers import WeatherSerializer, WorkSerializer
from .models import Weather, Work
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from pirc522 import RFID
from .tasks import getgps
import json

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
        print(load_template)
        if request.path.split('/')[-2].isdigit():
            work = Work.objects.get(int(request.path.split('/')[-2]))
            context['work'] = work
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def job_list(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        print(load_template)
        work_list = Work.objects.order_by('-id')
        print(work_list)
        # context = {'work_list': work_list}
        context['segment'] = load_template
        # print(context)
        context['work_list'] = work_list
        print(context)
        html_template = loader.get_template(load_template)

        # return render(request, 'job-list.html', context)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

# @login_required(login_url="/login/")
# def farmland_info(request, job_id):
#


@csrf_exempt
def rfid(request):
    rdr = RFID()
    dic = {}
    error = True
    while error:
        rdr.wait_for_tag()
        (error, tag_type) = rdr.request()
        if not error:
            print("Tag detected")
            (error, uid) = rdr.anticoll()
            print("UID: " + str(uid))
            print(type(uid))
    # Calls GPIO cleanup
    rdr.irq.clear()
    rdr.cleanup()
    dic["uid"] = ', '.join(map(str, uid))
    return JsonResponse(dic)


@login_required(login_url="/login/")
def job(request):
    result = {}
    success, lat, lon = getgps()
    if success:
        body = json.loads(request.body)
        uid = body['uid']
        user = request.user
        work = Work(uid=uid, lat=lat, lng=lon, worker=user)
        work.save()
    result['success'] = success
    return JsonResponse(result)

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

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    @action(detail=False, methods=['post'])
    def delete_all(self, request):
        Work.objects.all().delete()
        return Response('success')