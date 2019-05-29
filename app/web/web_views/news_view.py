"""
created by goblinM 2019-04-23
资讯浏览
"""

import json
import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.web.db_utils import mongodb
from app.web.db_utils.mongodb import MongoDBUtils
from app.web.webSerializers import HotSerializer


class ZiXunViewSet(viewsets.ModelViewSet):

    serializer_class = HotSerializer

    @action(detail=False,methods=["post"])
    def get_zixun_news(self, request):
        post_data = request.data
        data_type = post_data.get("data_type")
        page = int(post_data.get("page"))
        page_size = int(post_data.get("page_size"))
        time_sort = int(post_data.get("time_sort"))
        day_limit = post_data.get("day_limit")
        sensitive = post_data.get("sensitive")
        timeselect = datetime.datetime.now()
        actual_time = timeselect - datetime.timedelta(days=int(day_limit))
        actual_time = str(actual_time)
        # print(actual_time)
        # print(type(actual_time))
        mongo = mongodb.MongoDBUtils("zixun_news")
        curInfo = mongo.searchByDocSort({"data_type":data_type,"pub_time":{"$gt":actual_time}},"pub_time",time_sort)
        # print(curInfo[0])
        news_total = curInfo.count()
        # print(json.dumps(curInfo))
        curInfo = curInfo.skip((page-1)*page_size).limit(page_size)
        data = list(curInfo)

        # print(data)
        return Response({"data":data,"news_total":news_total})
