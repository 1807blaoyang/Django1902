from django.conf.urls import url
# 导入视图
from . import views
app_name = "ttsx"
# 应用路由
urlpatterns = [
    # 退出登陆
    url(r'^logout/$',views.logout,name="logout"),
    # 登陆
    url(r'^login/$',views.login,name="login"),
    # 注册
    url(r'^register/$',views.register,name="register"),
    # 首页
    url(r'',views.index,name="index"),


]