# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
# 验证账号是否登入


def checked(fn):
    def check_login(request, *args, **kwargs):
        try:
            u_id = request.session.get('u_id', '')
            u_name = request.session.get('u_name', '')
            if u_name != '':
                return fn(request, *args, **kwargs)
            else:
                res = redirect('/user/login/')
                # request.session['lastpath'] = request.get_full_path()
                return res
        except Exception as res:
            print(res)
    return check_login
