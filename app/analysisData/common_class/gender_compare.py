"""
created by goblinM 2019.5.11
这个是性别比例的函数
-1 未知
1  男
0  女
"""
from app.web.db_utils.mongodb import MongoDBUtils


class Gender:
    def __init__(self,collectionName):
        self.mongo = MongoDBUtils(collectionName)

    # 女性
    def female(self):
        female_count = self.mongo.searchByDoc({"author.gender":0}).count()
        self.mongo.close()
        return female_count

    # 男性
    def male(self):
        male_count = self.mongo.searchByDoc({"author.gender": 1}).count()
        self.mongo.close()
        return male_count

    # 未知性
    def unknowmale(self):
        unknow_count = self.mongo.searchByDoc({"author.gender": 0}).count()
        self.mongo.close()
        return unknow_count

if __name__ == '__main__':
    obj = Gender("zhihu_paris")
    print(obj.female())
    print(obj.male())
    print(obj.unknowmale())
