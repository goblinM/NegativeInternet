# -*- coding: utf-8 -*-
import json
import re

import scrapy
from scrapy import Request

from InternetSpider.InternetSpider.items import ZhiHuItem

class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['zhihu.sougou.com']
    start_urls = ['https://zhihu.sougou.com/']
    keyword = "奔驰车主维权"
    page = 5
    query_url = r"https://zhihu.sogou.com/zhihu?query={keyword}&page={page}"
    answer_include = "data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics"
    answer_limit = 5
    answer_offset = 0
    sort_by = "default"
    platform = "desktop"
    answer_url = r"https://www.zhihu.com/api/v4/questions/{url_id}/answers?include={answer_include}&limit={answer_limit}&offset={answer_offset}&platform={platform}&sort_by={sort_by}"

    def start_requests(self):
        yield Request(url=self.query_url.format(keyword=self.keyword, page=self.page), callback=self.parse_zhihu)

    def parse_zhihu(self, response):
        if response.status == 200:
            # 这里的下一页是指搜狗知乎的下一页
            try:
                last_page = response.css('.result-page ul li>a::text').extract()[-1]
                print(last_page)
                if last_page != "下一页":
                    return
            except:
                return
            result = response.css(".result-about-list .about-list-title a::attr(href)").extract()
            for url in result:
                url = url.split("/answer")[0]
                url = re.search('\d+', url).group()
                yield Request(url=self.answer_url.format(url_id=str(url), answer_include=self.answer_include,
                                                         answer_limit=self.answer_limit,
                                                         answer_offset=self.answer_offset, platform=self.platform,
                                                         sort_by=self.sort_by), callback=self.parse_detail,
                              dont_filter=True)
                # yield Request(url=url,callback=self.parse_detail,dont_filter=True)

            self.page += 1
            yield Request(url=self.query_url.format(keyword=self.keyword, page=self.page), callback=self.parse_zhihu,
                          dont_filter=True)

    def parse_detail(self, response):
        print(self.page)
        if response.status == 200:
            # result = response.css(".List-item .ContentItem-meta .UserLink-link::text").extract()
            # print(result)
            result = response.text
            result = json.loads(result)  # json化字符串
            if result:
                data = result["data"]
                for da in data:
                    icu = ZhiHuItem()
                    for field in icu.fields:
                        if field in da.keys():
                            icu[field] = da.get(field)
                        else:  # 这里是为了保持格式一致，避免有些字段出现有些字段没有出现
                            icu[field] = ""
                        icu["_id"] = da.get("question").get("title") + "_" + str(da.get("id"))
                    yield icu
                # 这块是知乎回答的分页，知乎返回的数据是json格式的
                try:
                    if 'paging' in result.keys() and result.get("paging").get("is_end") == False:
                        next_page = result.get('paging').get("next")
                        yield Request(next_page, self.parse_detail, dont_filter=True)
                except Exception as e:
                    print(e)