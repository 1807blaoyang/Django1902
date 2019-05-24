from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
# 引入基本视图类
from django.views.generic import View
from .models import Comment
from .models import Article
# Create your views here.
# 传统写法
# def comment(request):
#     return HttpResponse("评论表")
# 视图类写法

class AddComment(View):
    # 重写方法即可使用
    def post(self,request,id):
        # 获取用户名字
        username = request.POST.get("name")
        email = request.POST.get("email")
        url = request.POST.get("url")
        comment = request.POST.get("comment")

        # 赋值，保存，此时还不能保存，应该获得当前文章
        c = Comment()
        c.username = username
        c.email = email
        c.url = url
        c.content = comment
        # 获得文章对象使用get_object_or_404是为了处理异常，如果不处理异常，写法如下
        # article = Article.objects.get(pk=id)
        article = get_object_or_404(Article,pk=id)
        # 评论所属文章赋值
        c.article = article
        # 保存

        c.save()
        # 回到详情页,两种不同写法
        # return HttpResponseRedirect("blog/detail/%s"%(id,))
        return redirect(reverse('blog:detail',args=(id,)))
        # return HttpResponse("评论成功")
