# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from .models import ApiMessage

# Create your models here.
@python_2_unicode_compatible
class ApiChangeLog(models.Model):
    api_message = models.ForeignKey(ApiMessage, on_delete=models.CASCADE)  # 关联接口库
    api_change = models.CharField('接口变更说明', max_length=500)
    api_send_status = models.BooleanField('是否下发', default=True)
    change_time = models.DateTimeField('接口变更时间')

    def __str__(self):
        return u'%s %s %s %s' % (self.api_message, self.api_change, self.api_send_status, self.change_time)



