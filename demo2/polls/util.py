from django.http import HttpResponse,HttpResponseRedirect
# 验证登录装饰器，没有登录时完成需求，所有的url都要自动跳转登陆页面
def checklogin(fun):
    def check(request,*args):
        # yongcookie取
        # un =request.COOKIES.get("username")
        # 通过session获取
        un = request.session.get("username")
        if un:
            return fun(request,*args)
        else:
            return HttpResponseRedirect("/polls/login/")
    return check

# md5加密
import hashlib

def md5value(s):
    md5 = hashlib.md5()
    md5.update(s)
    return md5.hexdigest()
#对单个值进行加密
def mdfive2():
    sign = "123"
    print(md5value(sign))

if __name__ == '__main__':
    mdfive2()
