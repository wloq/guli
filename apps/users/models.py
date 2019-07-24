from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class UserProfile(AbstractUser):
    image = models.ImageField(upload_to='user/',max_length=200,verbose_name='用户头像',null=True,blank=True)
    nick_name = models.CharField(max_length=20,verbose_name='用户昵称',null=True,blank=True)
    birthday = models.DateTimeField(verbose_name='用户生日',null=True,blank=True)
    gender = models.CharField(choices=(('girl','女'),('boy','男')),verbose_name='性别',max_length=10,default='girl')
    address = models.CharField(max_length=200,verbose_name='用户地址',null=True,blank=True)
    phone = models.CharField(max_length=11,verbose_name='手机',null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username

class BannerInfo(models.Model):
    image = models.ImageField(upload_to='banner/',verbose_name='轮播图片',max_length=200)
    url = models.URLField(default='http://www.baidu.com',max_length=200,verbose_name='图片链接')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "轮播图信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.image

class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=20,verbose_name='邮箱验证码')
    email = models.EmailField(max_length=200,verbose_name='验证码邮箱')
    send_type = models.IntegerField(choices=((1,'register'),(2,'forget'),(3,'change')),verbose_name='验证码类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "邮箱验证码信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.code
