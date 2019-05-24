from django.conf.urls import url
from . import views
app_name = "comment"

# 应用路由
urlpatterns = [
    url(r'^addcomment/(\d+)/$',views.AddComment.as_view(),name="addcomment"),
]