"""
created by goblinM 2019.5.11
这个是点赞数前50的函数
"""
from app.web.db_utils.mongodb import MongoDBUtils


class Vote:
    def __init__(self,collectionName):
        self.mongo = MongoDBUtils(collectionName)
        self.data_name = collectionName

    def top50(self,keyword,limitsize):
        if self.data_name == "zhihu_icu":
            curInfo = self.mongo.searchByDocSortLimit({"question.title":{"$regex":keyword,"$options":"i"}},"voteup_count",-1,limitsize)
        else:
            curInfo = self.mongo.searchByDocSortLimit({"_id":{"$regex":keyword,"$options":"i"}},"voteup_count",-1,limitsize)

        # print(list(curInfo))
        # for data in curInfo[:5]:
        #     print(data)
        self.mongo.close()
        return list(curInfo)

if __name__ == '__main__':
    obj = Vote("zhihu_paris")
    obj.top50("巴黎圣母院",5)