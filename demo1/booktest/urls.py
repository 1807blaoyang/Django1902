# 将url包引入
from django.conf.urls import url
# 将视图文件导入
from . import views
# 解除硬编码
app_name = "polls"
# 设计url，应用路由
urlpatterns = [
    # url(r'^index&',views.index),
    # 首页
    url(r'^index/$', views.index, name= "index"),
    # 列表
    url(r'^list/$', views.list, name="list"),
    # 详情
    url(r'^detail/(\d+)/$', views.detail, name="detail"),
    #删除后重定向（书籍）
    url(r'^deletebook/(\d+)/$', views.deletebook, name="deletebook"),
    # 删除后重定向（角色）
    url(r'^deletehero/(\d+)/$',views.deletehero, name="deletehero"),
    #添加角色
    url(r'^addhero/(\d+)/$', views.addhero, name="addhero"),


    # 添加图书
    url(r'^addbook/$',views.addbook,name="addbook"),
    # 编辑角色
    url(r'^edithero/(\d+)/$', views.edithero,name="edithero"),
]