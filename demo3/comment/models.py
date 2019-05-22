from django.db import models
# 将blog引入
from blog.models import Article

# Create your models here.
# 评论表
class Comment(models.Model):
    # 评论名
    username = models.CharField(max_length=30,verbose_name="评论者名字")
    # 评论者Email  允许为空
    email = models.EmailField(blank=True,null=True,verbose_name="email")
    #  个人主页   允许为空
    url = models.URLField(blank=True,null=True,verbose_name="个人主页")
    # 评论内容
    content = models.CharField(max_length=500,verbose_name="评论内容")
    # 关联文章，一篇文章 可以有多个评论
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="所属文章")

    class Meta():
        verbose_name = "评论表"
        # 去除s
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username

