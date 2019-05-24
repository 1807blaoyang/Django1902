from django.conf.urls import url
from . import views
app_name = "blog"
urlpatterns = [
    # 点击标签云，进入标签所属文章详情
    url(r'^tag/(\d+)/$',views.tag,name= "tag"),
    # 点击分类，进入分类所属文章详情
    url(r'^classify/(\d+)/$',views.classify, name="classify"),
    # 点击文章标题，进入文章详情
    url(r'^detail/(\d+)/$',views.detail,name="detail"),
    # 点击进入归档，显示当月的所有文章
    url(r'^archive/(\d+)/(\d+)/$',views.archive,name="archive"),
    # 进入首页
    url(r'', views.index, name="index"),

]