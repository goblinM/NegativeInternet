from flask import Flask, g

from django.http import HttpResponse
from django.shortcuts import render
import lxml
# Create your views here.
from app.spider.proxypool.redis_db import RedisClient


def index(request):
    return HttpResponse("爬取数据")

def proxy(request):
    return "</h2>Welcome to Proxy System</h2>"

def get_conn():
    # g:global
    # if not hasattr(globals(),'redis'):
    redis = RedisClient()
    return redis

def get_proxy(request):
    """
        Get a proxy
        :return: 随机代理
        """
    conn = get_conn()
    print(conn.random())
    return HttpResponse(conn.random())

def get_counts(request):
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    print(conn.count())
    return HttpResponse(str(conn.count()))

# if __name__ == '__main__':
#     app.run()


