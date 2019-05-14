from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.
# 注册booktest的模型
admin.site.register(BookInfo)
admin.site.register(HeroInfo)
