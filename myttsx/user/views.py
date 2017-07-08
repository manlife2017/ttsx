from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from hashlib import sha1
from .models import UserInfo
from goods.models import GoodsInfo
from order.models import OrderInfo
import datetime
from .check_user_login import checked
from django.core.paginator import Paginator, Page


# Create your views here.
def login(request):
    # lastpath = request.GET.get('lastpath', '')
    # if lastpath != '':
    #     request.session['lastpath'] = lastpath
    name = request.COOKIES.get('uname', '')
    content = {
        'name': name,
        'top': 0
    }
    return render(request, 'user/login.html', content)


def register(request):
    content = {
        'top': 0
    }
    return render(request, 'user/register.html', content)


# 检测用户是否存在
def check_user(requset):
    get = requset.GET
    name = get.get('name')
    if len(UserInfo.objects.filter(name__exact=name)) > 0:
        return JsonResponse({'code': 1})
    else:
        return JsonResponse({'code': 0})


# 创建用户
def useradd(request):
    post = request.POST
    user_name = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')
    allow = post.get('allow')
    sha1_pwd = sha1(pwd.encode()).hexdigest()
    u = UserInfo()
    u.name = user_name
    u.passwd = sha1_pwd
    u.email = email
    u.save()
    res = redirect('/user/login/')
    return res


# 用户登录判断
def check_login(request):
    post = request.POST
    name = post.get('username')
    pwd = post.get('pwd')
    checkbox = post.get('checkbox', 0)
    sha_pwd = sha1(pwd.encode()).hexdigest()
    u = UserInfo.objects.filter(name__exact=name)
    content = {}
    if checkbox != 0:
        # res.set_cookie('uname', name, expires=datetime.datetime.now() + datetime.timedelta(days=14))
        content['name'] = name
    if len(u) > 0:
        if u[0].passwd == sha_pwd:
            request.session['u_name'] = u[0].name
            request.session['u_id'] = u[0].id
            # path = request.session.get('lastpath', '')
            # if path != '':
            #     print(path)
            #     del request.session['lastpath']
            #     res = redirect(path)
            #
            # else:
            path = request.session.get('lastpath')
            print(path)
            res = redirect(path)
            if checkbox != 0:
                res.set_cookie('uname', name, expires=datetime.datetime.now()+ datetime.timedelta(days=14))
            return res
        else:
            content['pw_error'] = '密码错误'
            content['top'] = 0
            return render(request, 'user/login.html', content)
    else:
        content['u_error'] = '用户名错误'
        content['top'] = 0
        return render(request, 'user/login.html', content)


# 用户退出
def quiter(request):
    del request.session['u_name']
    del request.session['u_id']
    return redirect('/')


# 个人中心
@checked
def info(request):
    name = request.session.get('u_name', 0)
    u_id = request.session.get('u_id', 0)
    u = UserInfo.objects.get(id__exact=u_id)
    browselists = request.COOKIES.get('browselists', '')
    lists = browselists.split('*')[:-1]
    glists = []
    for i in lists:
        g = GoodsInfo.goods.filter(id=i)[0]
        glists.append(g)
    content = {
        'left_display': 1,
        'name': name,
        'u_id': u_id,
        'u': u,
        'glist': glists
    }
    return render(request, 'user/user_center_info.html', content)


@checked
def uorder(request, pindex):
    name = request.session.get('u_name', 0)
    u_id = request.session.get('u_id', 0)
    u = UserInfo.objects.get(id__exact=u_id)
    content = {
        'left_display': 1,
        'name': name,
        'u_id': u_id,
        'u': u,
    }
    orders = OrderInfo.objects.filter(ouser_id=u_id).order_by('-odatetime')
    paginator = Paginator(orders, 2)
    index_list = paginator.page_range
    page = paginator.page(pindex)
    pagelist = page.object_list
    content['pagelist'] = pagelist
    content['page'] = page
    content['index_list'] = index_list
    return render(request, 'user/user_center_order.html', content)


@checked
def usite(request):
    name = request.session.get('u_name', 0)
    u_id = request.session.get('u_id', 0)
    u = UserInfo.objects.get(id__exact=u_id)
    content = {
        'left_display': 1,
        'name': name,
        'u_id': u_id,
        'u': u
    }
    return render(request, 'user/user_center_site.html', content)

# 修改收货地址
def editinfos(request):
    post = request.POST
    addressee = post.get('addressee')
    address = post.get('address')
    youbian = post.get('youbian')
    phone = post.get('phone')
    u_id = request.session.get('u_id', 0)
    u = UserInfo.objects.get(id__exact=u_id)
    u.phone = phone
    u.youbian = youbian
    u.addressee = addressee
    u.address = address
    u.save()
    return redirect('/user/usite/')
