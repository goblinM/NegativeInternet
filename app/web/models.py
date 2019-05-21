from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# 拓展继承user
class User(AbstractUser):
    # choices,第一个元素是存在数据库里真实的，第二个是页面显示的
    TYPE_CHOINCES = (
        (0,"user"),
        (1,"admin")
    )
    # user = models.CharField(max_length=25,null=True)
    # password = models.CharField(max_length=255,null=True)
    user_type = models.CharField(max_length=25,choices=TYPE_CHOINCES,default=0,verbose_name=u'用户的类型')#默认普通用户
    user_phone = models.CharField(null=True,verbose_name=u"用户的手机号码",max_length=25)

    class Meta(AbstractUser.Meta):
        verbose_name = "用户表"
        app_label = "web"

# 功能模块表
class Internet_Module(models.Model):
    name = models.CharField(max_length=55,null=True,verbose_name=u"中文模块名")
    unique_id = models.IntegerField()
    english_name = models.CharField(max_length=55,null=True,verbose_name=u"英文模块名")
    create_time = models.DateField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateField(auto_now=True,verbose_name=u"每次更新时间")

    class Meta:
        verbose_name = "功能模块表" #指定在admin管理界面中显示的名称
        db_table = "internet_module" #自定义表名称
        app_label = "web"

#  用户功能配置表
class User_Module(models.Model):
    module = models.ForeignKey(Internet_Module,on_delete=models.CASCADE,verbose_name=u"关联功能模块表")
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=u"用户表外键")

    class Meta:
        verbose_name = "用户功能配置表"
        db_table = "user_module"
        app_label = "web"

# 每日热点
class Hot_Daily(models.Model):
    rank = models.CharField(max_length=25,null=True,verbose_name=u"排名")  # 排名
    keyword = models.CharField(max_length=55,null=True,verbose_name=u"关键词")  # 关键词
    keyword_link = models.CharField(max_length=255,null=True,verbose_name=u"关键词链接")  # 关键词链接
    news_link = models.CharField(max_length=255,null=True,verbose_name=u"新闻链接")  # 新闻链接
    video_link = models.CharField(max_length=255,null=True,verbose_name=u"视频链接")  # 视频链接
    image_link = models.CharField(max_length=255,null=True,verbose_name=u"图片链接")  # 图片链接
    search_score = models.CharField(max_length=255,null=True,verbose_name=u"搜索指数")  # 搜索指数
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "每日热点表"
        db_table = "hot_daily"
        app_label = "web"