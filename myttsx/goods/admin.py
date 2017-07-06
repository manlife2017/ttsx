from django.contrib import admin
from .models import GoodsType, GoodsInfo
# Register your models here.
admin.site.register(GoodsInfo)
admin.site.register(GoodsType)