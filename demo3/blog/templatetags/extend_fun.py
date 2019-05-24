# 此文件为自建扩展功能模块
# 导入模块
from django import template
from blog.models import Article,Classify,Tag,Addimg
# 注册模块
register = template.Library()

# 注册一下，转小写
@register.filter()
def mylower(value):
    return  value.lower()

# 注册一下，截取指定字符长度,两个参数，注册成过滤器
@register.filter()
def myslice(value,lenth):
    return value[:lenth]

# 注册成标签 获取最新文章  num=3为形参，不传值默认为取前三个
@register.simple_tag()
def getlatestartices(num = 3):
    return  Article.objects.all().order_by("-create_time")[:num]

# 注册成标签，归档,用dates函数获得按月份降序，显示三个 ,
@register.simple_tag()
def getarchives(num = 3):
    return Article.objects.dates(field_name="create_time",kind="month",order='DESC')[:num]

# 获取所有分类
@register.simple_tag()
def getclassify():
    return Classify.objects.all()

# 获取所有标签
@register.simple_tag()
def gettag():
    return Tag.objects.all()

# 轮播图  获取数据库所有图片（注意  图像 并非直接保存于数据库，数据库中存的是路径）
@register.simple_tag()
def getaddimg():
    return Addimg.objects.all()


