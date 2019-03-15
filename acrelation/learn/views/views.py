# coding:utf-8
from django.shortcuts import render
from django.core.paginator import Paginator

from ..model.models import ApiMessage


# Create your views here.
def top_page(request):
    return render(request, 'base.html')

def api_message(request):
    apidata = {}
    apis = ApiMessage.objects.all()
    current_page = request.GET.get("page", 1)
    pages = Paginator(apis, 10)
    apis = pages.page(current_page)
    apidata["apis"] = apis
    apidata["pages"] = pages
    return render(request, 'api_message.html', apidata)


def get_kwarg(data={}):
    kwargs = {}
    if data:
        for (k, v) in data.items():
            if v is not None and v != "":
                kwargs[k] = v
    return kwargs

def search_api_message(request):
    apidata = {}
    search_data = {
        "component_owner": request.GET.get("component_owner"),
        "request_name": request.GET.get("request_name"),
        "url_name": request.GET.get("url_name")
    }
    kwargs = get_kwarg(search_data)
    apis = ApiMessage.objects.filter(**kwargs)
    current_page = request.GET.get("page", 1)
    pages = Paginator(apis, 10)
    apis = pages.page(current_page)
    apidata["apis"] = apis
    apidata["pages"] = pages
    return render(request, 'api_message.html', apidata)
