# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


@python_2_unicode_compatible
class ApiMessage(models.Model):
    name = models.CharField('接口名称', max_length=250, null=True, blank=True)
    url_name = models.CharField('路由信息', max_length=250)
    request_name = models.CharField('请求方式', max_length=10)
    component_owner = models.CharField('从属服务', max_length=250)
    api_status = models.BooleanField('是否在用', default=True)

    def __str__(self):
        return u'%s %s %s %s %s' % (self.name, self.url_name, self.request_name, self.component_owner)
