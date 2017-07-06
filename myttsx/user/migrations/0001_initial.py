# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('passwd', models.CharField(max_length=40)),
                ('eamil', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('youbian', models.CharField(max_length=6, null=True)),
                ('addressee', models.CharField(max_length=20, null=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
