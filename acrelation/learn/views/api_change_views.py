# coding:utf-8
from django.shortcuts import render
from django.core.paginator import Paginator
from ..model.api_relation_models import ApiRelationMix
from ..model.models import ApiMessage


# Create your views here.
def api_change_log(request):
    return render(request, 'api_change.html')