from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login#django自带登陆验证函数库
from django.contrib.auth import logout
from users . models import UserProfile
from django.urls import reverse#反向解析网址
from django.contrib.auth.hashers import make_password#加密密码库
import datetime

# Create your views here.

def index(request):
    return render(request,'index.html')
