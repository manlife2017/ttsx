from django.db import models
from user.models import UserInfo
from goods.models import GoodsInfo


# Create your models here.
class CartInfo(models.Model):
    cuser = models.ForeignKey(UserInfo)
    cgood = models.ForeignKey(GoodsInfo)
    gcount = models.IntegerField(default=0)
    isdelete = models.BooleanField(default=False)

    class Meta(object):
        db_table = 'cartinfo'