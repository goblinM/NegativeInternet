# -*- coding: utf-8 -*-
import json

import scrapy
import sys
sys.path.append('..')
from scrapy import Request
from InternetSpider.items import UserItem
# from InternetSpider.InternetSpider.items import UserItem
from app.web.db_utils.mongodb import MongoDBUtils


class ParisUserSpider(scrapy.Spider):
    name = 'paris_user'
    allowed_domains = ['api.zhihu.com']

    start_urls = ['https://api.zhihu.com/']
    start_url = r"https://api.zhihu.com/people/{}"

    def start_requests(self):
        yield Request(self.start_url.format("35529dc647811aecdb640e064620bb19"), callback=self.parse, dont_filter=True)

    def parse(self, response):
        # print(response.text)
        # print(response.status)
        # print(json.loads(response.text))
        # for collections in ["zhihu_paris","zhihu_car","zhihu_icu"]:
        mongo = MongoDBUtils("zhihu_paris")
        curInfo = mongo.distinctID("author.id")
        for uid in curInfo:
            if uid == "0":
                continue
            yield Request(self.start_url.format(uid), callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        result = json.loads(response.text)
        user = UserItem()
        for field in user.fields:
            if field in result.keys():
                user[field] = result.get(field)
            user["_id"] = result.get("id")
            user["database_name"] = "zhihu_user"
        yield user
