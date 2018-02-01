from django import http
# 中间件示例，打印中间件执行语句


class BookMiddleware(object):# 本书的中间件
    def process_request(self, request):
        pass
         # print("Middleware executed")
        # print("中间件执行")
# 分别处理收到的请求和发出去的相应，要理解中间件的原理。


class AnotherMiddleware(object):# 另一个中间件
    def process_request(self, request):
        pass
        #print("Another middleware executed")
        # print('另一个中间件执行')

    def process_response(self, request, response): # 过程的响映
        #print("AnotherMiddleware process_response executed")
        # print('另一个中间件process_response执行')
        return response

# 记录用户访问的url地址


class UrlPathRecordMiddleware(object):
    # 记录用户访问的url地址
    EXCLUDE_URLS = ['/users/login/', '/users/logout/', '/users/register/']
    # 1./user/ 记录 url_path = /user/
    # 2./user/login/ url_path = /user/
    # 3./user/login_check/  url_path = /user/

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        # 当用户请求的地址不在排除的列表中，同时不是ajax的get请求
        if request.path not in UrlPathRecordMiddleware.EXCLUDE_URLS and not request.is_ajax() and request.method == 'GET':
            request.session['url_path'] = request.path
BLOCKED_IPS = []
# 拦截在BLOCKED_IPS中的IP


#封锁IP中间件
class BlockedIpMiddleware(object):
    def process_request(self, request):
        if request.META['REMOTE_ADDR'] in BLOCKED_IPS:
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')