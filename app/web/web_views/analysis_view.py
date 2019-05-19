"""
created by goblinM 2019.5.28
这个是数据分析
"""
import json

from rest_framework.response import Response
from rest_framework.views import APIView


from app.analysisData.views import data_analysis_report
from app.web.db_utils.mongodb import MongoDBUtils


class ReportAPIView(APIView):
    def post(self,request):
        """
        获取案例详情内容
        :param request:请求参数：keyword 关键词data_name 数据库名
        :return: 请求的数据
        """
        data = request.data
        data_name = data.get("data_name")
        keyword = data.get("keywords")
        print(data_name)
        print(keyword)
        mongo = MongoDBUtils("data_report")
        curInfo = mongo.searchByDoc({"_id": data_name + "_report"})[0]
        if curInfo != [{}] and len(curInfo)!=0:
            print(list(curInfo))
            return Response({"data":curInfo})
        else:
            result = data_analysis_report(data_name,keyword)
            return Response({"data":result})
