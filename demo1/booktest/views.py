from django.shortcuts import render

# 导入视图所需要的包
from django.http import HttpResponse
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
def detail(request,id):
    # return request.HttpResponse("这是%s页"%id)
    #
    book = BookInfo.objects.get(pk=id)
    context = {"book": book}
    return render(request, 'booktest/detail.html', context)