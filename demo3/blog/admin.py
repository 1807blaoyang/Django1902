from django.contrib import admin

# Register your models here.
from .models import Classify,Article,Tag,MessageInfo,Addimg
# Register your models here.
# 注册后台管理  注册自建表
# Register your models here.

# 分类 表
admin.site.register(Classify)
# 文章表
admin.site.register(Article)
# 标签表
admin.site.register(Tag)

# 标签表
admin.site.register(MessageInfo)
# 轮播图
admin.site.register(Addimg)