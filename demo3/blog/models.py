from django.db import models
# 少见一张表，直接用django里面自带的user表
from django.contrib.auth.models import User
# Create your models here.
# 分类
class Classify(models.Model):
    title = models.CharField(max_length=30,verbose_name="分类名")
    def __str__(self):
        return  self.title

    class Meta():
        verbose_name = "分类表"
        # 去除s
        verbose_name_plural = verbose_name


# 标签
class Tag(models.Model):
    title = models.CharField(max_length=30,verbose_name="标签名")
    def __str__(self):
        return  self.title

    class Meta():
        verbose_name = "标签表"
        # 去除s
        verbose_name_plural = verbose_name


# 文章
class Article(models.Model):
    # 文章名
    title = models.CharField(max_length=100,verbose_name="文章名")
    # 文章文本
    body = models.TextField(verbose_name="正文")
    # 作者.   一个作者有多篇文章。
    auther = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="作者")
    #     # 阅读数 默认为0
    views = models.IntegerField(default=0,verbose_name="阅读次数")
    # 发表时间
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="发表时间")
    # 更改时间
    update_time = models.DateTimeField(auto_now=True,verbose_name="更改时间")
    # 一个分类对应多篇文章。 分类为1， 文章为多
    classify = models.ForeignKey(Classify,on_delete=models.CASCADE,verbose_name="所属分类")
    # 一个标签对应多个文章,一片文章对应多个标签
    tag = models.ManyToManyField(Tag,verbose_name="所属标签")
    def __str__(self):
        return  self.title

    class Meta():
        verbose_name = "文章表"
        # 去除s
        verbose_name_plural = verbose_name






