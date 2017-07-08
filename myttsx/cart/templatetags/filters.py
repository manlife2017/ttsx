# -*- coding:utf-8 -*-
from django.template import Library
import math
register = Library()


@register.filter
def list_get(value, index):
    return value[index-1]


@register.filter
def list_splice(value, number):
    if number >=3:
        s = number - 3
        end = number + 2
        return value[s:end]
    else:
        return value[0:5]
