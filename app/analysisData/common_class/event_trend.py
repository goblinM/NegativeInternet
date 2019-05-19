"""
@author:goblinM
@date:2019.5.12
@describe:事件走势
"""
from app.web.db_utils.mongodb import MongoDBUtils


class Event:
    def __init__(self,collectionName):
        self.mongo = MongoDBUtils(collectionName)
        self.data_name = collectionName

    def trend(self,keyword):
        if self.data_name == "zhihu_icu":
            # curInfo = self.mongo.searchByDoc({"question.title": {"$regex": keyword,"$options": "i"}})
            curInfo = self.mongo.searchByDocSortLimit({"question.title": {"$regex": keyword,"$options": "i"}}, "voteup_count", -1, 500)
        else:
            curInfo = self.mongo.searchByDocSortLimit({"_id":{"$regex": keyword,"$options": "i"}}, "voteup_count", -1, 500)

        question_id = []
        # print(question_id)
        # question_id = list(set(question_id))
        for q in curInfo:
            if q.get("question").get("id") not in question_id:
                question_id.append(q.get("question").get("id"))
        print(question_id)
        top = []
        for id in question_id:
            curQ = self.mongo.searchByDoc({"question.id":id})
            title = curQ[0].get("question").get("title")
            created_time = curQ[0].get("question").get("created")
            comment_count = 0
            voteup_count = 0
            for c in curQ:
                comment_count += c.get("comment_count")
                voteup_count += c.get("voteup_count")
            top.append({
                "title":title,
                "created_time":created_time,
                "comment_count":comment_count,
                "voteup_count":voteup_count
            })
        return top

if __name__ == '__main__':
    obj = Event("zhihu_paris")
    obj.trend("巴黎圣母院")