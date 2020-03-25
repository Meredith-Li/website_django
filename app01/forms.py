

from django import forms
from captcha.fields import CaptchaField   # 引入验证码field
# from .models import UserProfile
#
#
# # 用户登录表单的验证，注意字段与前端页面保持一致
# class LoginForm(forms.Form):
#     username = forms.CharField(required=True)  # 用户名不能为空
#     password = forms.CharField(required=True, min_length=5)  # 密码不能为空，而且最小5位数
#
#
# 用户登录表单时验证码的验证，注意字段与前端页面保持一致




class RegisterForm(forms.Form):
    email = forms.CharField(required=True)  # 用户名不能为空
    email2 = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})

