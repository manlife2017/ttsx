# -*- coding:utf-8 -*-
class LoginMiddleware(object):
    # 初始化
    def __init__(self):
        print('接受请求时')

    # 处理请求前
    def process_request(self, request):
        path = request.get_full_path()
        if path not in ['/user/login/',
                        '/user/register/',
                        '/user/useradd/',
                        '/user/check_login/',
                        '/user/quiter/',
                        ]:
            request.session['lastpath'] = path


    # 处理试图前
    def process_views(self, request, view_func, view_args, view_kwargs):
        pass

    # 处理模板响应前
    def process_template_request(self, request, response):
        pass

    # 处理响应前
    def process_response(self, request, response):
        return response

    # 出现异常
    def process_exception(self, request, exception):
        pass
