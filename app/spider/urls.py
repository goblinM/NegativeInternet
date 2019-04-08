from django.urls import path

from app.spider.views import index, get_proxy,get_counts

urlpatterns = [
    path(r'',index,name='index'),
    path(r'proxy/',get_proxy,name='proxy'),
    path(r'count_proxy/',get_counts,name="count_proxy")
]