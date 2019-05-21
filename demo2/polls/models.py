from django.db import models

# Create your models here.
# 根据投票应用的效果显示可知，可以将表设计成两个，创建两个模型类  投票类
class Poll(models.Model):
    # 属性 1问题
    question = models.CharField(max_length=200, verbose_name="投票问题")
    # 属性2 发布日期
    pub_date = models.DateTimeField('date published', "发布日期")
    class Meta():
        verbose_name = "问题"
        # 去除s
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question


# 选择类
class Choice(models.Model):
    # 属性1选择文本
    choice_text = models.CharField(max_length=200, verbose_name="选择文本")
    # 属性2票数
    votes = models.IntegerField(default=0, verbose_name="票数")
    # 外键
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name="票所属人")
    class Meta():
        verbose_name = "选项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.choice_text
# 用户表
class User(models.Model):
    name = models.CharField(max_length=20,verbose_name="姓名")
    pwd = models.CharField(max_length=20,verbose_name="密码")
    class Meta():
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
