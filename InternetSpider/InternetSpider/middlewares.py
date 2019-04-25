# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import random
import time

import requests
from jieba import analyse
from scrapy import signals

# 获取随机头部
from InternetSpider.settings import PROXIES


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        #print "**************************" + random.choice(self.agents)
        request.headers.setdefault('User-Agent', random.choice(self.agents))

# 获取settings.py文件的随机代理
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        # 这个是配置文件里的代码
        proxy = random.choice(PROXIES)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            # encoded_user_pass = base64.b64encode(proxy['user_pass'])
            # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            print("**************ProxyMiddleware have pass************" + proxy['ip_port'])
        else:
            print("**************ProxyMiddleware no pass************" + proxy['ip_port'])
            request.meta['proxy'] = "http://%s" % proxy['ip_port']

# 阿布云
class ABProxyMiddleware(object):
    def process_request(self,request,spider):
        # 代理服务器
        # proxyHost = "http://http-cla.abuyun.com"
        # proxyPort = "9030"
        proxyServer = "http://http-dyn.abuyun.com:9020"
        # 代理隧道验证信息
        proxyUser = "H05Z5U9SXCRE3O3D"
        proxyPass = "77AD782E0401FFA3"
        proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")
        print("**************ProxyMiddleware************" )
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth

class IPPOOlS(object):
    # 初始化
    def __init__(self,ip=""):
        self.ip = ip
        self.IPPOOL = []
    # 请求处理
    def process_request(self, request, spider):
        # 先随机选择一个IP
        # 这里填写无忧代理IP提供的API订单号（请到用户中心获取）
        order = "96a61d1bda162d574947584f1376f572"
        # # 获取IP的API接口
        apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order
        # # 获取IP时间间隔，建议为5秒
        fetchSecond = 5
        # # 开始自动获取IP
        # GetIpThread(apiUrl, fetchSecond).start()

        if not self.IPPOOL or len(self.IPPOOL) < 100:
            # while n<5:
                # 获取IP列表
            res = requests.get(apiUrl).content.decode()
            # 按照\n分割获取到的IP
            # IPPOOL = res.split('\n')
            # print(res)
            # for ip in res:
            self.IPPOOL.append(res.split('\n')[0])
            # print(self.IPPOOL)
            # 休眠
            time.sleep(fetchSecond)

        thisip = random.choice(self.IPPOOL)
        print(thisip)
        time.sleep(fetchSecond)
        print("**************当前使用的IP************" + thisip)
        request.meta["proxy"] = "http://" + thisip





class InternetspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class InternetspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

