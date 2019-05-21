# -*- coding: utf-8 -*-
import time

from scrapy import Spider, Request, FormRequest

import sys
sys.path.append('..')
from InternetSpider.items import InternetItem

"""
created by goblinM 2019-04-23
资讯爬虫的社会版块：金融，政治，科技，社会，文化，娱乐
"""


class ChinanewsSocialSpider(Spider):
    name = 'chinanews_social'
    allowed_domains = ['sou.chinanews.com']
    start_urls = ['http://sou.chinanews.com/']

    keyword = "社会"
    page = 0
    formdata = {
        "q": keyword,
        "ps": "10",
        "start": "0",
        "sort": "pubtime",
        "time_scope": "30",
        "channel": "all",
        "adv": "1",
        'day1': '',
        'day2': '',
        'creator': '',
    }
    # post请求的URL
    chinanews_url = r"http://sou.chinanews.com/search.do"

    def start_requests(self):
        self.logger.debug("ChinaNews is Starting")
        # FormRequest是post请求
        yield FormRequest(url=self.chinanews_url, formdata=self.formdata, callback=self.parse_news)  # post请求

        # 首页

    def parse_news(self, response):
        if response.status == 200:
            try:
                # 判断当前页是否是最后一页
                last_page = response.css("#page_bar #pagediv span::text").extract()[-1]
                # 最后一页则跳出
                if last_page is "尾页":
                    return
            except Exception as e:
                # 当匹配不到last_page,说明已经爬取完所有页面
                return
            # 当前页面的所有详情链接
            # self.logger.debug("now,will spider the " + str(self.page + 1) + "page")
            url_list = response.css("#news_list .news_item .news_other::text").extract()
            for url in url_list:
                # print(url)
                # print(url.split()[0])
                # res = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
                # url = re.search(res,url).group()
                url = url.split()[0]
                # self.logger.debug(url)  # 写入url
                print("当前爬取的网址是：", url)
                # self.url = url
                yield Request(url, callback=self.parse_details, dont_filter=True)
            # 循环调用，访问下一页
            self.page += 1
            self.formdata['start'] = '{}'.format(self.page * 10)
            # yield Request(url=self.chinanews_url.format(keyword=self.keyword, start=self.page * 10),
            #               callback=self.get_next_page)  # 默认get请求
            yield FormRequest(url=self.chinanews_url, formdata=self.formdata, callback=self.parse_news)  # post请求
        else:
            print("parse_news()ERROR,爬取到第", (self.page), "页")
            # self.logger.error("parse_news()ERROR,爬取到第"+str(self.page)+"页")

        # 从详情页中解析数据

    def parse_details(self, response):
        """
        这里测试得知：标题可能有2种形式，正文可能有6种
        :param response:
        :return:
        """
        internet = InternetItem()
        try:
            # 这里有一个坑就是网页打开是视频的话这些解析就会被判错一般这些单纯视频的url是类似
            # http://www.chinanews.com/gj/shipin/2019/04-04/news810384.shtml 比普通的多了news
            # 普通的类似http://www.chinanews.com/gj/shipin/2019/04-04/810384.shtml
            if response.status == 200:
                # if response.css(".videoplay").extract():
                #     print("only video")
                #     self.page += 1
                #     yield Request(url=self.chinanews_url.format(keyword=self.keyword, start=self.page * 10),
                #                   callback=self.get_next_page)  # 默认get请求
                # else:
                # 提取标题
                if response.css("#cont_1_1_2 h1::text").extract_first():
                    internet['title'] = response.css("#cont_1_1_2 h1::text").extract_first().strip()
                elif response.css("#cont_1_1_2 title::text").extract_first():
                    internet['title'] = response.css("#cont_1_1_2 title::text").extract_first().strip()
                elif response.css("table td center b br::text").extract_first():
                    internet['title'] = response.css("table tr td center b br::text").extract_first().strip()
                elif response.css(".content_title .left"):
                    internet['title'] = response.css(".content_title .left h1::text").extract_first()
                else:
                    internet['title'] = response.url  # 不然默认赋值打开的链接

                # 提取正文
                try:
                    content = ""
                    if response.css(".left_zw p::text").extract():
                        content = response.css(".left_zw p::text").extract()
                    elif response.css("table tr td center div p::text").extract():
                        content = response.css("table tr td center div p::text").extract()
                    elif response.css(".w1000.m_center .content_desc p::text").extract():
                        content = response.css(".w1000.m_center .content_desc p::text").extract()
                    elif response.xpath('//font[@id="Zoom"]'):
                        content = response.xpath('//font[@id="Zoom"]').extract()
                    elif response.xpath('//div[@id="qb"]'):
                        content = response.xpath('//div[@id="qb"]').extract()
                    elif response.xpath('//div[@class="video_con1_text_top"]/p'):
                        content = response.xpath('//div[@class="video_con1_text_top"]/p').extract()
                    else:
                        print('content:', response.url)
                        # self.logger.debug('this url not spide' + response.url + "!!!!!!!!!!!!")
                    internet["content"] = "".join(content).strip()
                    internet['describe'] = internet["content"][:60]
                except:
                    internet["content"] = ""
                    internet['describe'] = ""

                # 发布时间
                if response.css("#BaiduSpider #pubtime_baidu::text"):
                    internet["pub_time"] = response.css("#BaiduSpider #pubtime_baidu::text").extract_first().strip()
                elif response.css(".content_title .left p::text"):
                    internet["pub_time"] = response.css(".content_title .left p::text").extract_first()
                else:
                    internet["pub_time"] = "1999-01-01"

                # 数据链接
                internet["data_source"] = response.url
                # internet["data_source"] = response.css("#BaiduSpider #source_baidu a::attr(href)").extract_first().strip()
                # reporter = response.css("#BaiduSpider #source_baidu a::text").extract_first()
                # 发布者
                try:
                    internet["reporter"] = response.css("#BaiduSpider #source_baidu a::text").extract_first()
                except:
                    internet["reporter"] = "中国新闻网"

                internet["keyword"] = self.keyword
                internet['release_time'] = int(time.time())
                internet["_id"] = internet["title"].strip()
                internet["data_type"] = "social"
                internet["database_name"] = "zixun_news"
                yield internet
            else:
                print(response.status)
        except Exception as e:
            print("parse_details()ERROR,爬取到第", (self.page), "页")
            # self.logger.error("parse_details()ERROR,spide the" + str(self.page) + "page")
            # self.logger.error(e)
