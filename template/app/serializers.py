# movie_api/movies/serializers.py

from rest_framework import serializers
from .models import Weather, Work

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather # 모델 설정
        fields = ('id','basetime','fcstTime','temp','rain') # 필드 설정

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work  # 모델 설정
        fields = ('id', 'uid', 'workTime', 'lat', 'lat', 'worker')  # 필드 설정