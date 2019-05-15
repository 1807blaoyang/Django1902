from django.db import models
# 在这里创建你的模型类
# Create your models here.

# 图书表
class BookInfo(models.Model):
    bttile = models.CharField(max_length=30,verbose_name="书名")
    bdate = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    def __str__(self):
        return self.bttile
#英雄表
class HeroInfo(models.Model):
    name = models.CharField(max_length=30,verbose_name="英雄")
    # bool 类型性别  默认值为true 代表男
    gender = models.BooleanField(default=True,verbose_name="性别")
    # null = True 代表该列可以为空
    skill = models.CharField(max_length=50, null=True,verbose_name="技能")
    # ForeignKey 表名和BookInfo为多对一关系 所以在多地一方设置外键
    # book 的类型 BookInfo
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE,verbose_name="所属书籍")
    def __str__(self):
        return self.name




