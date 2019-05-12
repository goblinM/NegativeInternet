"""
created by goblinM 2019.5.11
这个是点赞数前50的函数
"""
from app.web.db_utils.mongodb import MongoDBUtils


class Vote:
    def __init__(self,collectionName):
        self.mongo = MongoDBUtils(collectionName)

    def top50(self,keyword,limitsize):
        curInfo = self.mongo.searchByDocSortLimit({"_id":{"$regex":keyword}},"voteup_count",-1,limitsize)
        # print(list(curInfo))
        # for data in curInfo[:5]:
        #     print(data)
        self.mongo.close()
        return list(curInfo)

if __name__ == '__main__':
    obj = Vote("zhihu_paris")
    obj.top50("巴黎圣母院",5)