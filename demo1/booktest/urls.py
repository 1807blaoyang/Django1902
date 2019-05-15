# 将url包引入
from django.conf.urls import url
# 将视图文件导入
from . import views
# 设计url
urlpatterns = [
    # url(r'^index&',views.index),
    url(r'^index/$', views.index),
    url(r'^list/$', views.list),
    url(r'^detail/(\d+)/$', views.detail),
]