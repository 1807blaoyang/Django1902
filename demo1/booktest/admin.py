from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.
# 注册booktest的模型



# Register your models here.
#定义管理后台
class BookInfoAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'bttile', 'bdate']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['btitle']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['btitle']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 2
admin.site.register(BookInfo)
admin.site.register(HeroInfo)