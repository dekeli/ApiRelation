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
from learn.views import add_api_views as learn_add_api_views
from learn.views import update_api_views as learn_update_api_views

urlpatterns = [
    url(r'^$', learn_views.api_message, name='base'),
    path('show_api_list/', learn_views.api_message, name='show_api_list'),
    path('get_api_by_id/<int:api_id>', learn_update_api_views.api_id_get, name='get_api_by_id'),
    path('add_api/', learn_add_api_views.add_api_to_library, name='add_api'),
    path('admin/', admin.site.urls),
]
