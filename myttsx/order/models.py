from django.db import models
from user.models import UserInfo
from cart.models import CartInfo
from datetime import datetime
# Create your models here.


class OrderInfo(models.Model):
    ouser = models.ForeignKey(UserInfo)
    odatetime = models.DateTimeField(auto_now=True)
    ostate = models.IntegerField(default=0)
    onumber = models.CharField(max_length=20)
    oprice = models.DecimalField(decimal_places=2, max_digits=10)
    opay = models.IntegerField(default=0)

    class Meta(object):
        db_table = 'orderinfo'


class OrderWithCart(models.Model):
    oid = models.ForeignKey(OrderInfo)
    ocart = models.ForeignKey(CartInfo)

    class Meta(object):
        db_table = 'orderwithcart'