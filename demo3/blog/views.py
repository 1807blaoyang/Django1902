from django.shortcuts import render,redirect,reverse
# 导入异常报错
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from comment.forms import CommentForm
from django.views import View
# paginator   分页器   page
from django.core.paginator import Paginator
# 发送邮件   send_mail 单封邮件   send_mass_mail   发送多封邮件
from django.core.mail import send_mail, send_mass_mail

# 将数据库中的存的数据表引入
from .models import Article,Classify,Tag,MessageInfo,Addimg as Ad

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


# 联系我们富文本，发送邮件
def contactus(request):
    m = MessageInfo()
    # 保存表单数据向开发者提意见
    if request.method =="POST":
        # 格式：用request.请求.get（“前端页面的name属性名”）
        # m.username = request.POST.get("username")
        m.email = request.POST.get("email")
        m.subject = request.POST.get("subject")
        m.info = request.POST.get("info")


        # 发送邮件
        try:
            # 将在setting中配置好的参数导入
            from django.conf import settings
            # 发送单封邮件
            # 第一个参数为主题     (subject, message, from_email, recipient_list,
            # 第二个参数为正文
            # 第三个参数为发件人
            # 第四个参数为收件人列表

            # 发送一封邮件
            # send_mail("这是一封测试邮件1","djange是可以发送邮件的",settings.DEFAULT_FROM_EMAIL,["1143108768@qq.com"])
            # print("发送成功！")

            # 发送多封邮件    此功能易错点 注意几个括号  因为send_mass_mail 接收参数时与一封邮件是相同的
            # send_mass_mail(
            #     (("测试邮件2","好好学习，天天向上",settings.DEFAULT_FROM_EMAIL,["1143108768@qq.com"]),
            #     ("测试邮件3", "好好学习，天天向上", settings.DEFAULT_FROM_EMAIL, ["1143108768@qq.com"]),
            #     ("测试邮件4", "好好学习，天天向上", settings.DEFAULT_FROM_EMAIL, ["1143108768@qq.com"]),
            #     ("测试邮件5", "好好学习，天天向上", settings.DEFAULT_FROM_EMAIL, ["1143108768@qq.com"]))
            # )
            # 将表单中的内容当作邮件发送给HR    最后面的收件人想要做成动态的，可以新建收件人类，从数据库中写一个函数获得所有的收件人
            send_mail(m.subject,m.info,settings.DEFAULT_FROM_EMAIL,["1143108768@qq.com"])

        except Exception as e:
            print("EEEEEEEEEEEE")
        # 发送成功保存至数据库
        m.save()

        return render(request,'contact.html',{"err":"发送成功！"})
    else:
        return render(request,'contact.html')

# 自定义头像
# 1. 使用老方法
# def addimg(request):
#     pass

# 2. 继承view,重写get与 post的两种方方法
class AddImg(View):
    def get(self,request):
        return render(request,"addimg.html")
    def post(self,request):
        # 获取表单中信息  img 是图片 所以要用files方法来获取,中括号
        # desc 图片描述则是普通的request.POST.get(前端页面的HTML)
        img=request.FILES["img"]
        desc=request.POST.get("desc")
        # 赋值
        ad =Ad(img=img,desc=desc)
       #  保存
        ad.save()
       #  跳转页面,返回首页
        return HttpResponseRedirect('blog/index')
       # return HttpResponse("sucess")


