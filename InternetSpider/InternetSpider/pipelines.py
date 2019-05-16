# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import random
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

import pymongo
from jieba import analyse

# 关键词
class KeyswordPipeline(object):
    """
    添加数据来源及抓取时间；
    结合textrank算法，抽取新闻中最重要的5个词，作为关键词
    """
    def process_item(self, item, spider):

        # 数据来源
        content = item['content']
        keywords = ' '.join(analyse.textrank(content, topK=5))
        # 关键词
        item['keywords'] = keywords
        return item

# 数据存储MongoDB
class MongoPipeline(object):
    def __init__(self,mongo_url,mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_url=crawler.settings.get("MONGO_URL"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )
    def open_spider(self,spider):
        #连接数据库
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        #关闭数据库
        self.client.close()

    def process_item(self, item, spider):
        # collection_name = item.__class__.__name__
        collection_name = item["database_name"]#"zixun_news" Internet  china_news
        #如果存在更新，没有就插入 去重操作
        # self.db[collection_name].update({'url_token':item['url_token']},{"$set":item},True)
        try:
            self.db[collection_name].insert(dict(item))
        except:
            # res = item["_id"]
            # item["_id"] = res+"_"+ str(int(time.time()))
            # self.db[collection_name].insert(dict(item))
            pass
        return item
