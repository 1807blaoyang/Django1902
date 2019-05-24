# 引入表单模块，生成表单
from django.forms import ModelForm
from django import forms
from .models import Comment
# 创建一个评论表单类
class CommentForm(forms.Form):
    # 重写
    name = forms.TextInput(attrs={"id":"id_name"})
    email = forms.EmailInput(attrs={"id":"email"})
    url = forms.URLInput(attrs={"id":"url"})
    comment = forms.TextInput(attrs={"id":"comment"})