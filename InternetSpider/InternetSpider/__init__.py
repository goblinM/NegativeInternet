"""
这是scrapy的爬虫文件夹
"""
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import sys
import os
import django
import sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../../../NegativeInternet") #具体路径
os.environ.setdefault('DJANGO_SETTINGS_MODULE','NegativeInternet.settings')
django.setup()
#
# from scrapy import cmdline
# cmdline.execute('scrapy crawl hot'.split(" "))