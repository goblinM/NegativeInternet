# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

# 这个是保存每日热点信息的
class HotPipeline(object):
    def process_item(self,item,spider):
        item.save()
        return item

    # def open_spider(self,spider):
    #     # 每次执行爬虫前需要执行的函数
    #     pass
    #
    # def close_spider(self,spider):
    #     # 每次爬虫结束前必须执行的函数
    #     pass
    #
    # @classmethod
    # def from_crawler(cls,crawler):
    #     pass