from django.db import models

# Create your models here.

# 用户模块
class User(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    pwd = models.CharField(max_length=20, verbose_name="密码")
    cpwd = models.CharField(max_length=20, verbose_name="确认密码")
    email = models.EmailField(default="1143108768@qq.com")
    is_active = models.BooleanField(default=True, verbose_name="是否激活")
    class Meta():
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

#  商品模块
