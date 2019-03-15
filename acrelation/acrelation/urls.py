"""acrelation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from learn.views import views as learn_views
from learn.views import add_update_api_views as learn_add_update_api_views
from learn.views import add_update_relation_views as learn_add_update_relation_views
from learn.views import api_change_views as learn_api_change_views
from learn.views import api_test_views as learn_api_test_views

urlpatterns = [
    url(r'^$', learn_views.search_api_message, name='search_api_list'),
    path('search_api/', learn_views.search_api_message, name='search_api_list'),
    path('show_api_list/', learn_views.api_message, name='show_api_list'),
    path('add_api/', learn_add_update_api_views.add_api_to_library, name='add_api'),
    path('update_api/', learn_add_update_api_views.update_api_to_library, name='update_api'),
    path('show_relation_list/', learn_add_update_relation_views.api_relation, name='show_relation_list'),
    path('show_change_list/', learn_api_change_views.api_change_log, name='show_change_list'),
    path('test_api/', learn_api_test_views.api_test_lib, name='test_api'),
    path('admin/', admin.site.urls),
]
