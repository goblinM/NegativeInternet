# -*- coding: utf-8 -*-
"""
created by goblinM 2019-4-22
百度实时热点搜索
"""
import json

from scrapy import Spider,Request

from InternetSpider.items import hotItem


class HotSpider(Spider):
    name = 'hotdaily'
    allowed_domains = ['top.baidu.com']
    start_urls = ['http://top.baidu.com/']
    hot_url = r"http://top.baidu.com/buzz?b=1&c=513&fr=topbuzz_b341_c513"

    def start_requests(self):
        yield Request(url=self.hot_url, callback=self.parse)

    # 网页解析
    def parse(self, response):

        try:
            if response.status == 200:
                # print(response.text)
                rank_list = response.css(".list-table .first span::text").extract() # 排名list
                keyword_list = response.css(".list-table .keyword a.list-title::text").extract() #关键字list
                keyword_url_list = response.css(".list-table .keyword a.list-title::attr(href)").extract()
                url_list = response.css(".list-table .tc a::attr(href)").extract()
                news_list = [url_list[url] for url in range(0,len(url_list),3)]
                video_list = [url_list[url] for url in range(1, len(url_list), 3)]
                image_list = [url_list[url] for url in range(2, len(url_list), 3)]
                score_list = response.css(".list-table .last span::text").extract()
                # print("rank_list:",rank_list)
                # print("keyword_list:",keyword_list)
                # print("keyword_url_list:",keyword_url_list)
                # print("news_list:",news_list)
                # print("video_list:",video_list)
                # print("image_list:",image_list)
                # print("score_list:",score_list)
                info = list(zip(rank_list,keyword_list,keyword_url_list,news_list,video_list,image_list,score_list))
                for data in info:
                    item = hotItem()
                    item["rank"] = data[0]
                    item["keyword"] = data[1]
                    item["keyword_link"] = data[2]
                    item["news_link"] = data[3]
                    item["video_link"] = data[4]
                    item["image_link"] = data[5]
                    item["search_score"] = data[6]

                    yield item
        except:
            yield Request(url=self.hot_url, callback=self.parse)

