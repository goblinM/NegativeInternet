# coding=utf-8
from rest_framework.response import Response
from rest_framework.views import APIView
from scrapyd_api import ScrapydAPI


class SpiderAPIView(APIView):
    def post(self,request):
        """
        :param request: 启动爬虫的请求参数
        :return: 爬虫启动是否成功
        """
        data = request.data
        spider_name = data.get("spider_name")
        spider_type = data.get("spider_type")
        # print(spider_name)
        # print(spider_type)
        if spider_type == "start":
            try:
                scrapyd = ScrapydAPI('http://localhost:6800')  # 这里是去调用部署分布式爬虫
                scrapyd.schedule('default', spider_name)  # 这里是启动爬虫
            except:
                return Response("failed")
        else:
            try:
                scrapyd = ScrapydAPI('http://localhost:6800')  # 这里是去调用部署分布式爬虫
                del_dict = scrapyd.list_jobs('default')  # 这里是启动爬虫
                # print(scrapyd.list_jobs('default'))
                del_jobs = []
                for k in ["pending","running"]:
                    # print(del_dict[k])
                    for item in del_dict[k]:
                        if item.get("spider") == spider_name:
                            del_jobs.append(item.get("id"))
                for job_id in del_jobs:
                    scrapyd.cancel('default',job_id)
                # print(del_jobs)

            except:
                return Response("failed")
        return Response("ok")

    def get(self,request):
        pass