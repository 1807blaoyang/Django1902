from django.shortcuts import render
from .models import Poll,Choice,User
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
# 匠装饰器引入
from .util import checklogin
import hashlib
import re

# Create your views here.
# 在前端验证cookie ，如果没有，将返回登陆页
@checklogin
def index(request):
    un = request.session.get("username")
    # 获取cookie
    # un = request.COOKIES.get("username")
    #获取session
    # un = request.session.get("username")
    # if un:
        # 获得投票项目列表
    latest_poll_list = Poll.objects.all()
        # 构造上下文，将投票项目列表传输到模板
    context = {'latest_poll_list': latest_poll_list,'username': un}
        # 渲染
    return render(request, 'polls/index.html', context)
    # else:
    #     return HttpResponseRedirect('/polls/login/')
def detail(request,id):
    # 由问题的id指定获得了问题对象
    question = Poll.objects.get(pk=id)
    # 如果是post请求，则真正提交，并更改数据库
    if request.method == "POST":
        # 获得选项的id
        c_id = request.POST["choice"]
        print(c_id)
        # 获得选项对象
        choice = Choice.objects.get(pk=c_id)
        # 投票加一
        choice.votes +=1
        # 保存数据
        choice.save()
        return HttpResponseRedirect("/polls/result/%s"%(id,))
    return render(request, 'polls/detail.html', {'question': question})
# 显示投票结果
def result(request,id):
    # return HttpResponse("结果")
    question = Poll.objects.get(pk=id)
    context = {"question":question}
    return render(request,"polls/result.html",context)

# 登陆  在后端验证
def login(request):
    if request.method=="POST":
        # 获取用户名
        name = request.POST.get("username")
        pwd = request.POST.get("pwd")

        # 验证用户名和密码  在数据库中筛选查询
        if len(User.objects.filter(name=name,pwd=pwd))!=0:
            # return HttpResponse("登陆成功！")   登陆成功后，存储cookie相关
            res = HttpResponseRedirect("/polls/index/")
            # 设置cookie登陆
            # res.set_cookie("username",name)
            # 设置session登陆
            request.session["username"] = name
            return res
        else:
            return render(request,"polls/login.html",{"err":"用户名或密码错误"})
    return render(request, "polls/login.html",)
# 安全退出
def logout(request):
    # 登陆  得到cookie
    res = HttpResponseRedirect("/polls/login/")
    # 清除cookie
    # res.delete_cookie("username")
    #清除session
    request.session.flush()
    return res


#     # md5加密
# def md5value(s):
#     md5 = hashlib.md5()
#     md5.update(s)
#     return md5.hexdigest()
#     # 对单个值进行加密
# def mdfive2():
#     global pwd
#     sign = pwd
#     md5value(sign)
# if __name__ == '__main__':
#     mdfive2()

# 注册
def register(request):
    global pwd

    if request.method =="POST":
        name = request.POST.get("username")
        pwd = request.POST.get("pwd")
        if len(name)!=0 and len(pwd)!=0:
            username = User.objects.filter(name=name)
            user = User()
            user.name = name
            user.pwd = pwd
            if len(username) == 0:
                # 正则验证非法字符
                if not re.search(u'^[_a-zA-Z0-9\u4e00-\u9fa5]+$', username):

                    return render(request, "polls/register.html", {"err": "不能包含非法字符（!,@,#,$,%...）！！"})
                else:
                    # 将注册数据保存到数据库
                    user.save()
                    # 跳转至登陆页面

                    return HttpResponseRedirect('/polls/login/')

            else:
                return render(request, "polls/register.html", {"err": "用户名已存在！！"})
        else:
            return render(request,"polls/register.html",{"err":"请输入！"})
    else:
        return render(request,"polls/register.html")

