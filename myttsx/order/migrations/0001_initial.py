# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20170705_2042'),
        ('user', '0002_auto_20170704_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('odatetime', models.DateTimeField(auto_now=True)),
                ('ostate', models.IntegerField(default=0)),
                ('onumber', models.CharField(max_length=20)),
                ('oprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('opay', models.IntegerField(default=0)),
                ('ouser', models.ForeignKey(to='user.UserInfo')),
            ],
            options={
                'db_table': 'orderinfo',
            },
        ),
        migrations.CreateModel(
            name='OrderWithCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('ocart', models.ForeignKey(to='cart.CartInfo')),
                ('oid', models.ForeignKey(to='order.OrderInfo')),
            ],
            options={
                'db_table': 'orderwithcart',
            },
        ),
    ]
