from django.shortcuts import render
# 导入异常报错
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from comment.forms import CommentForm

# paginator   分页器   page
from django.core.paginator import Paginator

# 将数据库中的存的数据表引入
from .models import Article,Classify,Tag

# Create your views here.

# 首页
def index(request):
    # 使用get请求获取参数
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum

    # return HttpResponse("首页")
    # 获得所有的文章，返回一个列表,并按阅读次数降序排列
    articles = Article.objects.all().order_by('-views')
    # 显示分页，一页一个   这一步，paginator将一个文章列表分成了若干份，每份paginator对象里有一篇文章
    paginator = Paginator(articles, 1)
    # 传入一个页码，得到指定页码的页面
    page = paginator.get_page(pagenum)
    # 将page作为参数传入页面(page包含所有信息)
    # 传入循环中

    # 第二功能 显示最近文章
    latestartices = Article.objects.all().order_by("-create_time")[:3]
    return render(request, "index.html", {"page":page})
# single  页面
def detail(request,id):
    a = Article()
    # 获得id跳转，有异常，报404错误
    article = get_object_or_404(Article, pk=id)
    article.views+=int(1)
    article.save()
    # 将数据库的from表单传入，在前端页面进行展示
    # cf = CommentForm()

    # # 第二功能 显示最近文章,已经置换成标签，写在了公共模板里面
    # latestartices = Article.objects.all().order_by("-create_time")[:3]
    return render(request, "single.html", locals())
    # return HttpResponse("首页")

# 归档
def archive(request,year,month):
    # 利用年月筛选出符合的书籍列表
    articles = Article.objects.filter(create_time__year = year,create_time__month=month)
    # 分页器   两个参数，被分页列表，每页分几个
    paginator = Paginator(articles,1)

    page = paginator.get_page(1)
    return render(request,'index.html',{"page":page})

# 分类
def classify(request,id):
    # 获得当前分类,,中所有的文章
    articles = get_object_or_404(Classify,pk=id).article_set.all()
    # 分页器   两个参数，被分页列表，每页分几个
    paginator = Paginator(articles, 1)
    page = paginator.get_page(1)
    return render(request, 'index.html', {"page": page})
# 标签
def tag(request,id):
    # 获得当前标签下的所有文章
    articles = get_object_or_404(Tag, pk=id).article_set.all()
    # 分页器   两个参数，被分页列表，每页分几个
    paginator = Paginator(articles, 1)
    page = paginator.get_page(1)
    return render(request, 'index.html', {"page": page})



