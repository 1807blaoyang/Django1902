
# 将url包引入
from django.conf.urls import url
# 将视图文件导入
from . import views
# 解除硬编码
app_name = "polls"

# 应用路由
urlpatterns = [
    # url(r'^index&',views.index),
    # 首页
    url(r'^index/$', views.index, name= "index"),
    url(r'^detail/(\d+)/$', views.detail, name="detail"),
    url(r'^result/(\d+)/$', views.result, name="result"),
    # 验证登陆
    url(r'^login/$',views.login,name="login"),
    # 注册
    url(r'^register/$', views.register, name="register"),
]
