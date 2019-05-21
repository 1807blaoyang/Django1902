from django.contrib import admin
from .models import Poll,Choice,User
# Register your models here.
# 注册后台管理
# Register your models here.
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(User)

