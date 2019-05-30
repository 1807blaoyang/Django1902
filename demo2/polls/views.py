from django.shortcuts import render,get_object_or_404
from .models import Poll,Choice,User
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

# 将配置发送邮件的setting文件导入
from django.conf import settings
# 将发送邮件的扩展模块导入，send是发送邮件，   EM是一个让邮件支持HTML显示的模块
from django.core.mail import send_mail,EmailMultiAlternatives
# 验证码需要使用的模块
from PIL import ImageDraw,Image,ImageFont
import random,io
# 将装饰器引入
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
        # 验证验证码
        # 从表中获取验证码
        verifycode = request.POST.get("verify")
        if verifycode == request.session.get("verifycode"):
            # 验证用户名和密码  在数据库中筛选查询
            # user = get_object_or_404(User,username=name,pwd=pwd)
            # 获取不到不报错
            user = User.objects.filter(name=name, pwd=pwd).first()
            if user:
                if user.is_active == 1:

                    # return HttpResponse("登陆成功！")   登陆成功后，存储cookie相关
                    res = HttpResponseRedirect("/polls/index/")
                    # 设置cookie登陆
                    # res.set_cookie("username",name)
                    # 设置session登陆
                    request.session["username"] = name
                    return res
                else:
                    return render(request, "polls/login.html", {"err": "请激活！"})
            else:
                return render(request, "polls/login.html", {"err": "用户名或密码错误"})
        else:
            return render(request,"polls/login.html",{"err":"验证码输入错误！"})
    else:
        return render(request, "polls/login.html")
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
        # 获取用户的信息
        name = request.POST.get("username")
        pwd = request.POST.get("pwd")
        email = request.POST.get("email")
        if len(name)!=0 and len(pwd)!=0:
            # 获取表单数据
            user = User()
            user.name = name
            user.pwd = pwd
            # 与数据库进行匹配,获取该用户
            user1 = User.objects.filter(name=name)
            # 如果得到
            if user1:
                # # 正则验证非法字符
                # if not re.search(u'^[_a-zA-Z0-9\u4e00-\u9fa5]+$', username):
                return render(request, "polls/register.html", {"err": "用户名已存在！"})
            else:

                # 根据表单上的数据创建一个用户
                user.save()
                # 将这个用户筛选出来,对象是个queryset集合，所以可用.first()方法   或者[0],来取到具体的对象
                user2 = User.objects.filter(name=name,pwd=pwd).first()
                # 注册用户后改为为非激活
                user2.is_active=False
                # 将注册数据保存到数据库
                user2.save()
                # 发送邮件
                # 四个参数
                try:
                    body = "<a herf='http://127.0.0.1:8000/polls/active/%s/'>点击此激活您的账户</a>"%(user2.id)
                    msg=EmailMultiAlternatives("感谢您使用本产品！请激活！", "<a herf='http://127.0.0.1:8000/polls/active/%s/'>点击此激活您的账户</a>"%(user2.id),settings.DEFAULT_FROM_EMAIL,[email])
                    # 指定以HTML格式发送
                    msg.content_subtype="html"
                    msg.send()
                    print("激活成功！")
                    # 跳转至登陆页面
                    return HttpResponseRedirect('/polls/login/')

                except Exception:
                    print("出错！")

        # else:
        #     return render(request, "polls/register.html", {"err": "用户名已存在！！"})
        else:
            return render(request,"polls/register.html",{"err":"请输入！"})
    else:
        return render(request,"polls/register.html")

# 当点击邮件时，正文上的超链接（路由）。  调用此方法
def active(request,id):
    # 获得点击邮件激活的用户
    user=get_object_or_404(User,pk=id)
    user.is_active = True
    # 保存
    user.save()
    return HttpResponseRedirect('/polls/login/')


# 登录使用验证码
def verify(request):
    # 自定义背景色，随机生成
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100),
               )
    width = 100
    heigth = 25

    # 创建画面对象
    img = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔
    draw = ImageDraw.Draw(img)
    # 绘制噪点
    for i in range(0, 100):
        # 绘制区域，利用横纵坐标
        xy = (random.randrange(0, width), random.randrange(0, heigth))
        # 填充颜色，
        fillcolor = (random.randrange(0, 255), 255, random.randrange(0, 255))
        # 使用point的方法绘制噪点
        draw.point(xy, fill=fillcolor)


    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    # font = ImageFont.truetype('SCRIPTBL.TTF', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # # 绘制4个字
    # draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    # draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    # draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    # draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 绘制4个字,最简单的绘制
    draw.text((5, 2), rand_str[0] )
    draw.text((25, 2), rand_str[1])
    draw.text((50, 2), rand_str[2])
    draw.text((75, 2), rand_str[3])
    # 释放画笔
    del draw
    # 将绘制好的验证码，保存在session里面  rand_str = 随机生成的数字
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    img.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')
