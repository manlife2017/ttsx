from django.shortcuts import render
from goods.models import GoodsInfo
from user.models import UserInfo
from user.check_user_login import checked
from cart.models import CartInfo
from .models import  OrderInfo, OrderWithCart
from django.http import JsonResponse
from datetime import datetime, timedelta
from time import time
from django.db import transaction
# Create your views here.
# 订单提交
@checked
def place_order(request):
    name = request.session.get('u_name', 0)
    u_id = request.session.get('u_id', 0)
    u = UserInfo.objects.get(id__exact=u_id)
    content = {
        'left_display': 1,
        'name': name,
        'u_id': u_id,
        'u': u,
    }
    carts = []
    gid = request.GET.get('gid', '')
    if gid != '':
        count = request.GET.get('count', 0)
        g = GoodsInfo.goods.filter(pk=gid)[0]
        c = CartInfo.objects.filter(cgood__exact=g, cuser__exact=u, isdelete=False)
        if len(c) > 0:
            cart = c[0]
            cart.gcount += int(count)
            cart.save()
        else:
            cart = CartInfo()
            cart.cuser = u
            cart.cgood = g
            cart.gcount = int(count)
            cart.save()
        carts.append(cart)
    else:
        cids = request.GET.get('oids', '')
        cid_list = cids.split('*')[:-1]
        for i in cid_list:
            c = CartInfo.objects.filter(pk=int(i))[0]
            carts.append(c)
    content['carts'] = carts
    return render(request, 'order/place_order.html', content)


# 生成订单 采用数据库事务处理避免不报错
@transaction.atomic
def create_order(request):
    try:
        sid = transaction.savepoint()
        post = request.POST
        # 获取id
        u_id = request.session.get('u_id', 0)
        u = UserInfo.objects.get(id__exact=u_id)
        carts = post.get('carts')
        paymethod = post.get('paymethod')
        carts = carts.split('*')[:-1]
        cartlist = []
        sumprice = 0
        for i in carts:
            cart = CartInfo.objects.get(id=i)
            price = cart.cgood.gprice
            count = cart.gcount
            sumprice += price*count
            cartlist.append(cart)
        order = OrderInfo()
        print(order.id)
        order.ouser = u
        order.odatetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
        order.onumber = ''
        order.oprice = sumprice
        order.save()
        for cart in cartlist:
            o2c = OrderWithCart()
            o2c.ocart = cart
            o2c.oid = order
            o2c.save()
            cart.isdelete = True
            cart.save()
        order.onumber = str(order.id).zfill(20)
        order.save()
        transaction.savepoint_commit(sid)
        return JsonResponse({'code': 1})
    except Exception as res:
        print(res)
        transaction.savepoint_rollback(sid)
        return JsonResponse({'code': 0})
