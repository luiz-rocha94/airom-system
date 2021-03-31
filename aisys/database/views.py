from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .utils import heart_failure_model


class HeartFailureModel(View):
    def get(self, request):
        #verificar os parâmetros obrigatórios.
        result = heart_failure_model(request.GET.dict())
        return JsonResponse(result)
