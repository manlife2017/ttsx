# -*- coding:utf-8 -*-
from django.template import Library
register = Library()


@register.filter
def list_get(value, index):
    return value[index-1]
