# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from .models import ApiMessage

# Create your models here.
@python_2_unicode_compatible
class ApiRelationMix(models.Model):
    re_component_name = models.CharField('调用接口的组件名称', max_length=250)
    re_component_director = models.IntegerField('负责人联系方式')
    api_message = models.ManyToManyField(ApiMessage)  # 关联接口库表
    use_message = models.CharField('调用说明', max_length=500, null=True, blank=True)

    def __str__(self):
        return u'%s %s %s %s' % (self.re_component_name, self.re_component_director, self.api_message,
                                 self.api_change_history)



