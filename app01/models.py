from django.db import models
from datetime import datetime
# # Create your models here.
# from django.contrib.auth.models import AbstractUser
#
# class UserProfile(AbstractUser):
#     nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
#     birday = models.DateTimeField(verbose_name='生日', null=True, blank=True)
#     gender = models.CharField(max_length=6, choices=(('male', '男'), ('female','女')), default='female', verbose_name='性别')
#     address = models.CharField(max_length=100, default='', verbose_name='地址')
#     mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
#     image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100, verbose_name="图片")
#
#     class Meta:
#         verbose_name = '用户信息'
#         verbose_name_plural=verbose_name
#
#     def __str__(self):
#         return self.username
#
#
#
#
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(verbose_name="验证码类型", choices=(('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')), max_length=30)
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email   # 这里很重要，否则在后台就显示不出Meta信息