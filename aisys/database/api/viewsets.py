from django.db.models.query import QuerySet
from rest_framework import viewsets
from .. import models
from . import serializers


class FilterViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        """
        GET method
        """
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            try:
                queryset = queryset.filter(**self.request.GET.dict())
            except:
                queryset = queryset.none()
        return queryset


class HeartFailureViewSet(FilterViewSet):
    queryset = models.HeartFailure.objects.all()
    serializer_class = serializers.HeartFailureSerializer
