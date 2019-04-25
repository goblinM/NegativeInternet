"""
created by goblinM 2019-04-23
资讯浏览
"""
import json

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.web.db_utils import mongodb
from app.web.db_utils.mongodb import MongoDBUtils


class ZiXunViewSet(viewsets.ModelViewSet):

    @action(detail=False,methods=["get"])
    def get_zixun_news(self,request):
        mongo = mongodb.MongoDBUtils("zixun_news")
        curInfo = mongo.searchByDoc({"data_type":"financial"})
        # print(json.dumps(curInfo))
        data = list(curInfo)[:50]
        # print(data)
        return Response(data)
