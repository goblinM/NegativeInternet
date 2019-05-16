import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.analysisData.common_class.comment_top import Comment
from app.analysisData.common_class.event_trend import Event
from app.analysisData.common_class.gender_compare import Gender
from app.analysisData.common_class.loaction import Location
from app.analysisData.common_class.vote_top import Vote
from app.analysisData.common_class.word_cloud import Word
from app.web.db_utils.mongodb import MongoDBUtils


def index(request):
    return HttpResponse("分析数据")


def data_analysis_report(request):
    data_name = request.POST.get("data_name")
    keyword = request.POST.get("keyword")
    mongo = MongoDBUtils("data_report")
    curInfo = mongo.searchByDoc({"_id":data_name+"_report"})
    # 如果报告已经存在了直接引用，不存在调用接口生成
    if curInfo:
        print(curInfo)
    else:
        # 事件走势
        event_mongo = Event(data_name)
        event_data = event_mongo.trend(keyword)
        # 这个是性别比例的函数
        gender_mongo = Gender(data_name)
        female = gender_mongo.female()
        male = gender_mongo.male()
        unknowmale = gender_mongo.unknowmale()
        # 信息地域分布
        location_mongo = Location(data_name)
        location_data = location_mongo.analysis()
        # 点赞数前50的函数
        vote_top = Vote(data_name)
        vote_data = vote_top.top50(keyword,50)
        # 评论数前50的函数
        comment_top = Comment(data_name)
        comment_data = comment_top.top50(keyword,50)
        # 词云生成,这个是生成图
        word_mongo = Word(data_name)
        word_cloud = word_mongo.keywordcloud(keyword)
        word_count = word_mongo.wordcount()
        word_pie = word_mongo.wordpie()
        word_data = word_mongo.get_data()
        data = {
            "event_data":event_data,
            "gender_date":{
                "female":female,
                "male":male,
                "unknowmale":unknowmale
            },
            "location_data": location_data,
            "vote_data": vote_data,
            "comment_data": comment_data,
            "word_data":word_data,
            "_id":data_name+"_report",
            "created_time": int(time.time())
        }
        mongo.insertmongoDB(data)





