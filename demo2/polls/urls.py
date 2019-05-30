
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
    # 安全退出
    url(r'logout/$',views.logout,name="logout"),
    # 注册
    url(r'^register/$', views.register, name="register"),
    # 激活账户
    url(r'^active/(d+)/$',views.active,name="active"),
    # 获取验证码
    url(r'^verify/$',views.verify,name="verify"),
]

