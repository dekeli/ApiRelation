# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from ..models import ApiMessage
from django.core.paginator import Paginator
import json

# Create your views here.
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
    response = HttpResponse()
    data = dict()
    data["result"] = "fail"
    apidata = {}
    if request.method == "POST":
        try:
            search_data = {
                "component_owner": request.POST.get("component_owner"),
                "request_name": request.POST.get("request_name"),
                "url_name": request.POST.get("url_name")
            }
            kwargs = get_kwarg(search_data)
            apis = ApiMessage.objects.filter(**kwargs)
            current_page = request.GET.get("page", 1)
            pages = Paginator(apis, 10)
            apis = pages.page(current_page)
            apidata["apis"] = apis
            apidata["pages"] = pages
            data['result'] = 'success'
        except Exception as e:
            data["message"] = str(e)
            data["result"] = "fail"
            response = HttpResponse(status=500)
        data_json = json.dumps(data)
        response.write(data_json)
        return response
