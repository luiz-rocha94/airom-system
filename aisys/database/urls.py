from django.urls import path, include
from rest_framework import routers
from .api import viewsets

route = routers.DefaultRouter()
route.register(r'usedcar', viewsets.UsedCarViewSet, basename='used-car')

urlpatterns = [
    path('', include(route.urls)),
]
