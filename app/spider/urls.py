from django.urls import path

from app.spider.views import index

urlpatterns = [
    path(r'',index,name='index')
]