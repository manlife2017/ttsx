from django.shortcuts import render
from .models import GoodsInfo, GoodsType
from django.core.paginator import Paginator, Page
from user.models import UserInfo
from cart.models import CartInfo
# Create your views here.


def index(request):
    name = request.session.get('u_name', 0)
    u_id = request.session.get('u_id', 0)
    types = GoodsType.objects.all()
    carts = CartInfo.objects.filter(cuser__exact=u_id, isdelete=False).count()
    list = []
    for item in types:
        goods = GoodsInfo.goods.filter(gtype=item).order_by('-gmoods')[0:4]
        list.append(goods)
    content = {
        'left_display': 0,
        'name': name,
        'u_id': u_id,
        'glists': list,
        'cartcount': carts
    }
    return render(request, 'index.html', content)

# 不同种类的商品
def list(request, gid, pid, omethod):
    gtype = GoodsType.objects.filter(id=gid)
    moodslist = GoodsInfo.goods.filter(gtype_id=gid).order_by('-gmoods')[0:2]
    gt_title = gtype[0].typename
    order_title = ['默认', '价格', '人气']
    if omethod == '1':
        glists = GoodsInfo.goods.filter(gtype_id=gid).order_by('id')
    elif omethod == '2':
        glists = GoodsInfo.goods.filter(gtype_id=gid).order_by('-gprice')
    elif omethod == '3':
        glists = GoodsInfo.goods.filter(gtype_id=gid).order_by('-gmoods')
    paginator = Paginator(glists, 10)
    page = paginator.page(pid)
    index_list = paginator.page_range
    p_list = page.object_list
    content = {
        'pindex': pid,
        'plist': p_list,
        'blist': index_list,
        'page': page,
        'gtitle': gt_title,
        'omethod': int(omethod),
        'moodslist': moodslist,
        'order_title': order_title
    }
    name = request.session.get('u_name', 0)
    if name != 0:
        u_id = request.session.get('u_id', 0)
        u = UserInfo.objects.get(id__exact=u_id)
        content['name'] = name
        content['u_id'] = u_id
        content['u'] = u
        carts = CartInfo.objects.filter(cuser__exact=u_id, isdelete=False).count()
        content['cartcount'] = carts
    return render(request, 'goods/list.html', content)


# 商品详情
def goodinfo(request, gid):
    good = GoodsInfo.goods.filter(id__exact=gid)[0]
    good.gmoods += 1
    good.save()
    moodslist = GoodsInfo.goods.filter(gtype_id=good.gtype_id).order_by('-gmoods')[0:2]
    content = {
        'good': good,
        'moodslist': moodslist
    }
    name = request.session.get('u_name', 0)
    if name != 0:
        u_id = request.session.get('u_id', 0)
        u = UserInfo.objects.get(id__exact=u_id)
        content['name'] = name
        content['u_id'] = u_id
        content['u'] = u
        carts = CartInfo.objects.filter(cuser__exact=u_id, isdelete=False).count()
        content['cartcount'] = carts
        browselists = request.COOKIES.get('browselists', '')
        print(browselists)
        if browselists != '':
            lists = browselists.split('*')
            if gid not in lists:
                lists.insert(0, gid)
                browselists = '*'.join(lists[0:5])
        else:
            lists = []
            lists.insert(0, gid)
            browselists = '*'.join(lists)
        res = render(request, 'goods/detail.html', content)
        res.set_cookie('browselists', browselists)
    else:
        res = render(request, 'goods/detail.html', content)
    return res


