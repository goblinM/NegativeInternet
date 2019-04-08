'''
获取代理
'''
import sys

from app.spider.proxypool.crawler import Crawler
from app.spider.proxypool.redis_db import RedisClient
from app.spider.proxypool.setting import POOL_UPPER_THRESHOLD


class Getter:
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()  #这个是获取爬虫的

    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                # 获取代理
                proxies = self.crawler.get_proxies(callback)
                sys.stdout.flush()
                for proxy in proxies:
                    self.redis.add(proxy)