from django.urls import path, include
from rest_framework import routers

from .api import viewsets

route = routers.DefaultRouter()
route.register(r'heart_failure', viewsets.HeartFailureViewSet, basename='heart-failure')

urlpatterns = [
    path('', include(route.urls)),
]
