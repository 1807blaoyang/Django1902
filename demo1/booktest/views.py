from django.shortcuts import render

# 导入视图所需要的包
from django.http import HttpResponse, HttpResponseRedirect
# 导入自定义模板需要的包 loader（加载），RequestContext（请求上下文）
from django.template import loader,RequestContext
# 导入自定义的类（包含书籍信息）
from .models import BookInfo,HeroInfo

# Create your views here.
def index(request):
    # return HttpResponse("这是首页")
    # 1. 加载模板
    template = loader.get_template("booktest/index.html")

    # 2.构造上下文
    context = {}

    #3. 渲染模板显示动态数据
    render1 = template.render(context=context)
    return HttpResponse(render1)
def list(request):
    # loader.get_template("booktest/list.html")
    # 获取所有的书
    allbook = BookInfo.objects.all()
    print(allbook)
    # 构造上下文
    context = {"allbook":allbook}
    # 简写   渲染动态数据
    render2 = render(request,"booktest/list.html",context)
    return HttpResponse(render2)
    # return HttpResponse("这是列表")
# 详情页
def detail(request,id):
    # return request.HttpResponse("这是%s页"%id)
    #
    book = None
    try:
        book = BookInfo.objects.get(pk=id)
    except Exception as f:
        return HttpResponse("对不起，没有书籍")
    # 构造上下文
    context = {"book": book}
    return render(request, 'booktest/detail.html', context)

# 删除功能（重定向）
def deletebook(request,id):
    # 执行删除
    book = BookInfo.objects.get(pk=id).delete()
    # print(book)
    # return HttpResponse("成功！")
    return HttpResponseRedirect("/booktest/list/")
def addbook(request,id):
    # 将参数id定义
    book =BookInfo.object.get(pk=id)
    # 存储表单数据：
    book1 = BookInfo()
    book1.bttile = request.POST["btitle"]
    book1.bdate = request.POST["bdate"]
    # return HttpResponse("成功")

# 删除英雄
def deletehero(request,id):
    # 依靠id获取该英雄,然后删除
    hero = HeroInfo.objects.get(pk=id)
    bookid = hero.book.id
    hero.delete()
    print(hero)
    # print(book)
    # return HttpResponse("成功！")
    # 重定向的详情页
    return HttpResponseRedirect("/booktest/detail/%s"%(bookid))
# 添加角色
def addhero(request,id):
    # return HttpResponse("chenggong !")
    # 经典错误！！！小细节！！！！ 并不是路由，前面没有斜杠
    # return render(request, '/booktest/addhero.html/')
    # 进行表单的提交，利用get和post请求的切换
    if request.method == "GET":
        print("我进来了")
        return render(request, 'booktest/addhero.html/', context={"bookid": id})


    elif request.method =="POST":
        # 将参数id定义  wei书籍的id 在数据库中存的虽然是一个id 但其实获得是
        book = BookInfo.objects.get(pk=id)
        # 存储表单数据：
        hero = HeroInfo()
        hero.name = request.POST["username"]
        hero.gender = request.POST["sex"]
        hero.skill = request.POST["skill"]
        # 所属书籍   !!!! hero.book   由多地一方直接点出来
        hero.book = book
        # 保存
        hero.save()
        # return HttpResponse("chenggong")
        return HttpResponseRedirect("/booktest/detail/%s" % (id))





