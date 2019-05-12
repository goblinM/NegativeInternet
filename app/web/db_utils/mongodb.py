"""
mongodb的配置文件
"""
import pymongo
from app.web.db_utils import db_tools as tools

class MongoDBUtils:
    def __init__(self,collectionName):
        try:
            # print(collectionName)
            self.client = pymongo.MongoClient(tools.default_mongo_host,tools.default_mongo_port)
            self.db = self.client[tools.default_mongo_name]
            # self.db.authenticate(tools.default_mongo_user,tools.default_mongo_password)
            self.collection = self.db[collectionName]
        except Exception as e:
            print(e)

    def close(self):
        self.client.close()

    def searchByDoc(self, searchDoc, condi=None):
        resultDoc = {}
        try:
            resultDoc = self.collection.find(searchDoc, condi)
            if resultDoc.count() == 0:
                resultDoc = [{}]
        except Exception as e:
            print(e)
        return resultDoc

    def searchByDocSort(self, searchDoc, sortKey, ENDING ,condi=None): #ENDING,
        resultDoc = {}
        try:
            resultDoc = self.collection.find(searchDoc, condi).sort(sortKey, ENDING) #, ENDING
        except Exception as e:
            print(e)
        return resultDoc

    def searchByDocSortLimit(self, searchDoc, sortKey, ENDING ,size,condi=None): #ENDING,
        resultDoc = {}
        print(searchDoc)
        print(sortKey)
        print(ENDING)
        print(size)
        try:
            resultDoc = self.collection.find(searchDoc, condi).sort(sortKey, ENDING).limit(size) #, ENDING
        except Exception as e:
            print(e)
        return resultDoc

    def insert(self, data):
        item = None
        try:
            item = self.collection.insert_one(data)
        except Exception as e:
            print(e)
        return item

    def delectData(self, data):
        try:
            self.collection.remove(data)
        except Exception as e:
            print(e)
        return "ok"

    # mongo插入数据
    def insertmongoDB(self, data):
        try:
            self.collection.insert(data)
        except Exception as e:
            print(e)
        return "ok"

    # 查找唯一值id
    def distinctID(self,data):
        item = None
        try:
            item = self.collection.distinct(data)
        except Exception as e:
            print(e)
        return item
