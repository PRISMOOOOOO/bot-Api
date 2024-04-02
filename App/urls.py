from django.urls import path,include

from .views import ListApiView

urlpatterns = [
    path("weather/",ListApiView.as_view())
]