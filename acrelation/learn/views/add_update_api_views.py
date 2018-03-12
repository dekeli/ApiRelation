# coding:utf-8
import json

from django.http import HttpResponse

from learn.model.models import ApiMessage
from django.db.models import Q


# Create your views here.

def add_api_to_library(request):
    response = HttpResponse()
    data = dict()
    data["result"] = "fail"
    if request.method == "POST":
        component_owner = request.POST.get("component_owner")
        request_name = request.POST.get("request_name")
        url_name = request.POST.get("url_name")
        name = request.POST.get("name")
        api_status = request.POST.get("api_status")
        try:
            ApiMessage_object = ApiMessage(component_owner=component_owner,
                                           request_name=request_name,
                                           url_name=url_name,
                                           name=name,
                                           api_status=api_status)
            ApiMessage_object_get = ApiMessage.objects.filter(component_owner=component_owner,
                                                              request_name=request_name, url_name=url_name)
            if ApiMessage_object_get:
                data["result"] = "repeat"
            else:
                ApiMessage_object.save()
                data['result'] = 'success'
        except Exception as e:
            data["message"] = str(e)
            data["result"] = "fail"
            response = HttpResponse(status=500)
        data_json = json.dumps(data)
        response.write(data_json)
        return response

def update_api_to_library(request):
    response = HttpResponse()
    data = dict()
    data["result"] = "fail"
    if request.method == "POST":
        api_id = request.POST.get("api_id")
        component_owner = request.POST.get("edit_api_component")
        request_name = request.POST.get("edit_api_request")
        url_name = request.POST.get("edit_api_url")
        name = request.POST.get("edit_api_name")
        api_status = request.POST.get("edit_api_status")
        try:
            ApiMessage_object_get = ApiMessage.objects.filter(Q(component_owner=component_owner) & Q(request_name=request_name) & Q(url_name=url_name) & ~Q(id=api_id))
            if ApiMessage_object_get:
                data['result'] = 'repeat'
            else:
                ApiMessage.objects.filter(id=api_id).update(component_owner=component_owner,
                                                            request_name=request_name,
                                                            url_name=url_name,
                                                            name=name,
                                                            api_status=api_status)
                data['result'] = 'success'
        except Exception as e:
            data["message"] = str(e)
            data["result"] = "fail"
            response = HttpResponse(status=500)
        data_json = json.dumps(data)
        response.write(data_json)
        return response
