from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .serializers import WeatherSerializer
from .models import Weather

# Create your views here.
class ListApiView(ListAPIView):
    serializer_class = WeatherSerializer
    queryset = Weather.objects.all()
