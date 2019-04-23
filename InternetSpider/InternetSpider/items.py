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


