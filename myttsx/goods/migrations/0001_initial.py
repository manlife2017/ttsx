# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('gname', models.CharField(max_length=30)),
                ('gprice', models.DecimalField(default=0.0, decimal_places=2, max_digits=10)),
                ('gunti', models.CharField(max_length=20, default='500g')),
                ('gmoods', models.IntegerField(default=0)),
                ('gsurplus', models.IntegerField(default=1000)),
                ('gintro', models.CharField(max_length=100)),
                ('gdescription', models.TextField()),
                ('gimg', models.ImageField(upload_to='goods/')),
                ('gbigimg', models.ImageField(upload_to='goods/')),
            ],
            options={
                'db_table': 'goodsinfo',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('typename', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'goodstype',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='goods.GoodsType'),
        ),
    ]
