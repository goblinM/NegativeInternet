"""NegativeInternet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from app.web.views import index
from app.web.web_views.analysis_view import ReportAPIView
from app.web.web_views.hot_view import HotViewSet
from app.web.web_views.news_view import ZiXunViewSet
from app.web.web_views.spider_view import SpiderAPIView
from app.web.web_views.user_view import UserViewSet
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
schema_view = get_swagger_view(title='API 接口文档')
router = routers.DefaultRouter()
router.register(r'user',UserViewSet,base_name='user')
router.register(r"hot",HotViewSet,base_name='hot')
router.register(r"news",ZiXunViewSet,base_name='news')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/login/', obtain_jwt_token),
    path("api/",include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('api-docs/',schema_view),#自动生成的api文档
    path("api_report/",ReportAPIView.as_view(),name='report'),
    path("api_spider/",SpiderAPIView.as_view(),name='spider'),
    #path('',index,name='index'),#这个是首页
    path(r'', TemplateView.as_view(template_name="index.html")),
    path('spider/',include('spider.urls')),#spider的路径
    path('web/',include('web.urls')),#系统集成数据的路径
    path('analysis/',include('analysisData.urls'))#数据分析的路劲
]
