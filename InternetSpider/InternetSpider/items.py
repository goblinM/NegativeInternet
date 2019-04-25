# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field
from scrapy_djangoitem import DjangoItem

from app.web.models import Hot_Daily


class hotItem(DjangoItem):
    django_model = Hot_Daily
# class hotItem(Item):
#     rank = Field() #排名
#     keyword = Field() #关键词
#     keyword_link = Field() #关键词链接
#     news_link = Field() #新闻链接
#     video_link = Field() #视频链接
#     image_link = Field() #图片链接
#     search_score = Field() #搜索指数


class InternetItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = Field()
    title = Field() #标题
    describe = Field() # 简述
    pub_time = Field() #报告时间
    reporter = Field() #报告者或者来源
    data_source = Field() #信息的链接
    detail_url = Field() # 这个不一定要
    content = Field() #正文
    keywords = Field() #搜索的关键词组
    keyword = Field()  # 搜索的关键词
    release_time = Field() #爬取的时间
    data_type = Field() #数据类型