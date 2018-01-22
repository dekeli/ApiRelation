# Generated by Django 2.0 on 2018-01-16 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='接口名称')),
                ('url_name', models.CharField(max_length=250, verbose_name='路由信息')),
                ('request_name', models.CharField(max_length=10, verbose_name='请求方式')),
                ('component_owner', models.CharField(max_length=250, verbose_name='从属服务')),
                ('api_status', models.BooleanField(default=True, verbose_name='是否在用')),
                ('api_call', models.BigIntegerField(default=0, verbose_name='调用量')),
            ],
        ),
    ]
