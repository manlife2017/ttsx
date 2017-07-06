from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    passwd = models.CharField(max_length=40)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=20, null=True)
    youbian = models.CharField(max_length=6, null=True)
    addressee = models.CharField(max_length=20, null=True)
    isdelete = models.BooleanField(default=False)

    class Meta(object):
        db_table = 'userinfo'