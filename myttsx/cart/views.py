from django.shortcuts import render
from user.check_user_login import checked
from user.models import UserInfo
from django.http import JsonResponse
from goods.models import GoodsInfo
from .models import CartInfo

# Create your views here.
@checked
def mycart(request):
    name = request.session.get('u_name', 0)
    u_id = request.session.get('u_id', 0)
    u = UserInfo.objects.get(id__exact=u_id)
    carts = CartInfo.objects.filter(cuser_id=u_id, isdelete=False)
    content = {
        'left_display': 1,
        'name': name,
        'u_id': u_id,
        'u': u,
        'carts': carts
    }
    return render(request, 'cart/cart.html', content)


# 购物车添加
def goodtocart(request):
    content = {}
    name = request.session.get('u_name', '')
    if name == '':
        content['name_error'] = 1
    else:
        content['name_error'] = 0
        get = request.GET
        gid = get.get('gid')
        count = get.get('count')
        uid = request.session.get('u_id')
        u = UserInfo.objects.filter(pk__exact=uid)[0]
        g = GoodsInfo.goods.filter(pk__exact=gid)[0]
        try:
            c = CartInfo.objects.filter(cgood__exact=g, cuser__exact=u, isdelete=False)
            if len(c) > 0:
                content['is_in_cart'] = 1
                cart = c[0]
                cart.gcount += int(count)
                cart.save()
            else:
                content['is_in_cart'] = 0
                cart = CartInfo()
                cart.cuser = u
                cart.cgood = g
                cart.gcount = int(count)
                cart.save()
            content['code'] = 1
        except Exception as res:
            print(res)
            content['code'] = 0
    return JsonResponse(content)


# 修改购物车数量
def ed_count(request):
    try:
        cid = request.POST.get('c_id')
        count = request.POST.get('count')
        c = CartInfo.objects.filter(id__exact=cid)[0]
        c.gcount = count
        c.save()
        return JsonResponse({'code': 1})
    except Exception as res:
        print(res)
        return JsonResponse({'code': 0})


# 删除商品
def del_good(request):
    try:
        cid = request.POST.get('c_id')
        print(cid)
        cart = CartInfo.objects.filter(id__exact=cid)[0]
        print(cart)
        cart.delete()
        return JsonResponse({'code': 1})
    except Exception as res:
        print(res)
        return JsonResponse({'code': 0})
