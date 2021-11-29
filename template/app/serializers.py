# movie_api/movies/serializers.py

from rest_framework import serializers
from .models import Weather

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather # 모델 설정
        fields = ('id','base_time','fcstTime','temp','rain') # 필드 설정