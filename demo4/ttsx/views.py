from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
import re

# Create your views here.
def index(request):
    return render(request,"ttsx/index.html")
    # return HttpResponse("chenggong")

# 注册
def register(request):
    if request.method =="POST":
        # 获取表单内容
        # 错误列表
        err = []
        name= request.POST.get("user_name")
        pwd = request.POST.get("pwd")
        cpwd = request.POST.get("cpwd")
        email = request.POST.get("email")
        print(name,pwd,cpwd,email)

        # 与数据库对比
        user = User()
        user.name = name
        user.pwd = pwd
        user.cpwd = cpwd
        user.email = email
        username = User.objects.filter(name=name)
        useremail = User.objects.filter(email=email)
        if (name and pwd and cpwd and email):
            if not username:
                print("username")
                if len(pwd) >= 6 and len(pwd) <= 11:
                    print("pwd")
                    if pwd == cpwd:
                        print("cpwd")
                        if not useremail:
                            # 保存表单数据
                            print("useremail")
                            user.save()
                            return render(request, "ttsx/login.html")
                        else:
                            return render(request, "ttsx/register.html", {"err4": "请重新输入邮箱"})


                    else:
                        return render(request, "ttsx/register.html", {"err3": "两次密码不一致"})
                else:
                    return render(request, "ttsx/register.html", {"err2": "密码不符合规定"})
            else:
                return render(request, "ttsx/register.html", {"err1": "该用户已注册"})
        else:
            return render(request, "ttsx/register.html", {"err": "请按要求将下列选项填写完整"})
    else:
        return render(request,"ttsx/register.html")

# 登陆
def login(request):
    if request.method=="POST":
        # 获取用户名
        name = request.POST.get("username")
        pwd = request.POST.get("pwd")
        # 与数据库进行比对
        user = User.objects.filter(name=name,pwd=pwd).first()
        print(user)
        if user:
            res= HttpResponseRedirect("/index/")
            # 设置session登陆
            request.session["username"] = name
            return res
        elif user == None:
            return render(request,"ttsx/login.html",{"err":"用户名或密码错误"})
    return render(request,"ttsx/login.html")

# 安全退出
def logout(request):
    # 登陆  得到cookie
    res = HttpResponseRedirect("/login/")
    # 清除cookie
    # res.delete_cookie("username")
    #清除session
    request.session.flush()
    return res