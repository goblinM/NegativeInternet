"""
created by goblinM 2019-04-22
每日热点详情
"""
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.web.models import Hot_Daily
from app.web.webSerializers import HotSerializer
from scrapyd_api import ScrapydAPI

class HotViewSet(viewsets.ModelViewSet):
    queryset = Hot_Daily.objects.all()
    serializer_class = HotSerializer

    @action(methods=["get"],detail=False)
    def get_hot_data(self,request):
        """
        获取更新后的热点
        :return:
        """
        data = self.queryset.order_by('-update_time')[:50]
        # data = data.order_by('rank')
        hot_news =  HotSerializer(data,many=True)
        result = reversed(hot_news.data)
        return Response(result)

    @action(methods=["post"],detail=False)
    def start_hot_spider(self,request):
        """
        启动每日热点的爬虫，需要验证admin权限
        :param request: user_type:用户的身份权限
        :return:
        """
        data = request.data
        user_type = data.get("user_type")
        if user_type == "1":#admin权限,开启爬虫
            # run_hot()
            # scrapyd = ScrapydAPI('http://localhost:6800') # 这里是去调用部署分布式爬虫
            # print(scrapyd.list_projects())#获取爬虫项目名
            # print(scrapyd.list_spiders('default'))#获取爬虫项目中的爬虫工程名
            # print(scrapyd.list_jobs('default')) #获取爬虫项目中运行的爬虫工程信息
            # print(scrapyd.list_versions('default'))# 获取爬虫项目中的版本
            # scrapyd.schedule('default','hotdaily') # 这里是启动爬虫
            return Response("ok")
        else:
            return Response("failed")