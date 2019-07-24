from django.db import models
from datetime import  datetime
from orgs.models import OrgInfo,TeacherInfo
# Create your models here.
class CourseInfo(models.Model):
    image = models.ImageField(upload_to='course/',max_length=200,verbose_name='课程封面')
    name = models.CharField(max_length=20,verbose_name='课程名称')
    study_time = models.IntegerField(default=0,verbose_name='学习时长')
    study_num = models.IntegerField(default=0,verbose_name='学习人数')
    level = models.CharField(choices=(('gj','高级'),('zj','中级'),('cj','初级')),max_length=5,verbose_name='课程难度',default='cj')
    love_num = models.IntegerField(default=0,verbose_name='收藏数')
    click_num = models.IntegerField(default=0,verbose_name='访问量')
    desc = models.CharField(max_length=200,verbose_name='课程简介')
    detail = models.TextField(verbose_name='课程详情')
    category = models.CharField(choices=(('qd','前端开发'),('hd','后端开发')),verbose_name='课程类别',max_length=5)
    course_notice = models.CharField(max_length=200,verbose_name='课程公告')
    course_need = models.CharField(max_length=100,verbose_name='课程须知')
    teacher_tell = models.CharField(max_length=100,verbose_name='老师告诉')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    orginfo = models.ForeignKey(OrgInfo,verbose_name='所属机构')
    teacherinfo = models.ForeignKey(TeacherInfo,verbose_name='所属讲师')

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name