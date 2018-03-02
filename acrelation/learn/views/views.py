# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from ..models import ApiMessage
from django.core.paginator import Paginator

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
