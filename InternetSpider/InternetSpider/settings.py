# -*- coding: utf-8 -*-

# Scrapy settings for InternetSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os
import sys
#
# sys.path.append(os.path.dirname(os.path.abspath('.')))
# os.environ['DJANGO_SETTINGS_MODULE'] = 'NegativeInternet.settings'
# This is required only if Django Version > 1.8
# import django
# django.setup()
# import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'InternetSpider'))

BOT_NAME = 'InternetSpider'

SPIDER_MODULES = ['InternetSpider.spiders']
NEWSPIDER_MODULE = 'InternetSpider.spiders'

MONGO_URL = '127.0.0.1:27017'
MONGO_DB = 'NegativeInternet'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'InternetSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 禁用cookies
COOKIES_ENABLED=False

# 头部设置
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
PROXIES = [

    {"ip_port":"27.208.70.212:8060","user_pass":""},
    {"ip_port":"95.158.62.112:44226","user_pass":""},
    {"ip_port":"110.52.235.24:9999","user_pass":""},
    {"ip_port":"208.83.106.105:9999","user_pass":""},
    {"ip_port":"110.52.235.211:9999","user_pass":""},
    {"ip_port":"119.179.135.181:8060","user_pass":""},
    {"ip_port":"117.191.11.102:8080","user_pass":""},
    {"ip_port":"3121.8.98.196:80","user_pass":""},
    {'ip_port': '211.23.149.28:80', 'user_pass': ''},
    {'ip_port': '218.60.8.99:3129', 'user_pass': ''},
    {'ip_port': '111.26.9.26:80', 'user_pass': ''},
    {'ip_port': '218.58.194.162:8060', 'user_pass': ''},
    {"ip_port":"193.38.139.140:80",'user_pass': ''},
    {'ip_port': '119.179.135.181:8060', 'user_pass': ''},
    {'ip_port': '198.1.122.29:80', 'user_pass': ''},
    {'ip_port': '125.62.40.3:8080', 'user_pass': ''},
    {'ip_port': '157.230.163.11:80', 'user_pass': ''},
    {'ip_port': '68.107.176.159:80', 'user_pass': ''},
    {'ip_port': '171.100.29.202:8080', 'user_pass': ''},
    {"ip_port":"120.210.219.103:8080","user_pass":""},
    {"ip_port":"120.210.219.102:8080","user_pass":""},
    {"ip_port":"120.210.219.101:8080","user_pass":""},
    {"ip_port":"223.16.229.241:8080","user_pass":""},
    {"ip_port":"139.255.17.2:47421","user_pass":""},
]
""" 启用限速设置 """
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 0.2  # 初始下载延迟
DOWNLOAD_DELAY = 0.2  # 每次请求间隔时间#设置下载延迟


#Downloader最大并发请求下载数量，默认32
CONCURRENT_REQUESTS = 50
#每个目标域名最大的并发请求数量，默认8
CONCURRENT_REQUESTS_PER_DOMAIN = 50
#每个目标IP最大的并发请求数量，默认0，非0有效
CONCURRENT_REQUESTS_PER_IP = 50

#调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# :123456
REDIS_URL = 'redis://root@127.0.0.1:6379'
DOWNLOAD_FAIL_ON_DATALOSS = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'InternetSpider.middlewares.InternetspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'InternetSpider.middlewares.RandomUserAgent': 1,
    # 'InternetSpider.middlewares.ProxyMiddleware':110,
    'InternetSpider.middlewares.ABProxyMiddleware':110
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'InternetSpider.pipelines.HotPipeline': 300,
    'InternetSpider.pipelines.MongoPipeline': 301,
    "InternetSpider.pipelines.KeyswordPipeline":300,
    'scrapy_redis.pipelines.RedisPipeline': 301
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
