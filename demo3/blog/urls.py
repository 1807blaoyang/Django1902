from django.conf.urls import url
from . import views
app_name = "blog"
urlpatterns = [
    # 点击进入自定义头像,这里用到的是继承视图的写法，所以与传统的url写法不同
    url(r'^addimg/$',views.AddImg.as_view(), name="addimg"),
    # 点击联系，进入联系页面
    url(r'^contactus/$',views.contactus, name="contactus"),
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