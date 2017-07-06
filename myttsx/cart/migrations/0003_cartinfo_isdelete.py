# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20170705_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartinfo',
            name='isdelete',
            field=models.BooleanField(default=False),
        ),
    ]
