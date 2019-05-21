from django.shortcuts import render
from .models import Poll,Choice,User
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
# 在前端验证cookie ，如果没有，将返回登陆页
def index(request):
    # 获取cookie
    un = request.COOKIES.get("username")
    if un:
        # 获得投票项目列表
        latest_poll_list = Poll.objects.all()
        # 构造上下文，将投票项目列表传输到模板
        context = {'latest_poll_list': latest_poll_list,'username': un}
        # 渲染
        return render(request, 'polls/index.html', context)
    else:
        return HttpResponseRedirect('/polls/login/')
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
        name=request.POST.get("username")
        pwd=request.POST.get("pwd")
        if name == "yqh" and pwd == "123456":
            # return HttpResponse("登陆成功！")   登陆成功后，存储cookie相关
            res = HttpResponseRedirect("/polls/index/")
            res.set_cookie("username",name)
            return res
        else:
            return render(request,"polls/login.html",{"err":"用户名或密码错误"})
    return render(request, "polls/login.html",)

# 注册
def register(request):
    if request.method =="POST":
        name = request.POST.get("username")
        pwd = request.POST.get("pwd")
        # 将注册数据保存到数据库
        user = User()
        user.name = name
        user.pwd = pwd
        user.save()
        return HttpResponseRedirect('/polls/login/')
    else:
        return render(request,"polls/register.html")