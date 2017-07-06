# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20170704_1738'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('gcount', models.IntegerField(default=0)),
                ('cgood', models.ForeignKey(to='goods.GoodsInfo')),
                ('cuser', models.ForeignKey(to='user.UserInfo')),
            ],
        ),
    ]
