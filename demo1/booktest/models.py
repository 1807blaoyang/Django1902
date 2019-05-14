from django.db import models
# 在这里创建你的模型类
# Create your models here.

# 图书表
class BookInfo(models.Model):
    bttile = models.CharField(max_length=30)
    bdate = models.DateTimeField(auto_now_add=True)
#英雄表
class HeroInfo(models.Model):
    name = models.CharField(max_length=30)
    # bool 类型性别  默认值为true 代表男
    gender = models.BooleanField(default=True)
    # null = True 代表该列可以为空
    skill = models.CharField(max_length=50, null=True)
    # ForeignKey 表名和BookInfo为多对一关系 所以在多地一方设置外键
    # book 的类型 BookInfo
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)


