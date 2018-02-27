# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from ..models import ApiMessage
from django.core.paginator import Paginator
import json

# Create your views here.
def api_id_get(request, api_id):
    ApiIdMessage_db = ApiMessage.objects.get(id=api_id)
    context = {"api_id": ApiIdMessage_db}
    return render(request, 'base.html', context)

def update_api_to_library(request):
    response = HttpResponse()
    data = dict()
    data["result"] = "fail"
    if request.method == "PUT":
        component_owner = request.PUT.get("component_owner")
        request_name = request.PUT.get("request_name")
        url_name = request.PUT.get("url_name")
        name = request.PUT.get("name")
        api_status = request.PUT.get("api_status")
        try:
            ApiMessage_object = ApiMessage(component_owner=component_owner,
                                           request_name=request_name,
                                           url_name=url_name,
                                           name=name,
                                           api_status=api_status)
            ApiMessage_object.save()
            data['result'] = 'success'
        except Exception as e:
            data["message"] = str(e)
            data["result"] = "fail"
            response = HttpResponse(status=500)
        data_json = json.dumps(data)
        response.write(data_json)
        return response
