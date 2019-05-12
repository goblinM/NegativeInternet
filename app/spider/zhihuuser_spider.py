"""
created by goblinM 2019.5.11
知乎用户的信息的爬取
"""
import json
import os
import time
from multiprocessing.pool import Pool

import redis
import requests

import app.web.db_utils.mongodb as mongodb
from app.spider.redis_utils import RedisClient


def worker(arg):
    print("子进程开始执行>>> pid={},ppid={},编号{}".format(os.getpid(), os.getppid(), arg))
    mongo = mongodb.MongoDBUtils(arg)
    curInfo = mongo.distinctID("author.id")
    # db = RedisClient()
    insert_mongo = mongodb.MongoDBUtils("zhihu_user")
    for uid in curInfo[:10]:
        # db.add(uid)
        print(uid)
        if uid == "0":
            continue
        else:
            start_url = r'https://api.zhihu.com/people/{}'.format(uid)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRjYzc5MmM1MTBiMDMzYTUzNTZjNzA4NjBhNWRjZjliBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUp6S2tXT3g5a0FCT01ndzlmWWZqRVJNek1WanRuUDBCbTJUN21GMTBKd3M9BjsARg%3D%3D--2a69429cb2115c6a0cc9a86e0ebe2800c0d471b3',
                'Host': 'www.xicidaili.com',
                'Referer': 'http://www.xicidaili.com/nn/3',
                'Upgrade-Insecure-Requests': '1',
            }
            response = requests.get(start_url,headers=headers)
            print(response.content)
            insert_mongo.insert(json.loads(response.content))
    insert_mongo.close()
    mongo.close()
    print("子进程终止>>> pid={},ppid={},编号{}".format(os.getpid(), os.getppid(), arg))


if __name__ == '__main__':
    start_url = r'https://api.zhihu.com/people/{}'.format("35529dc647811aecdb640e064620bb19")
    # start_url = r"https://www.baidu.com"
    proxies = {
        "http": "http://118.89.204.192:443",
        "https": "https://118.89.204.192:443"
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Cookie': '_xsrf=gQxd6U7hVMtZtu6snZcv4RNrSnY1ok1f; d_c0="AMAluk5B3Q2PTjEnbZMdApgV8Qv6EJYrROM=|1530966478"; _zap=78230fd3-fca3-4811-b46a-f85807c72ada; q_c1=26228f9f414d4c58a4e60f0c0e661461|1554986317000|1552035353000; l_cap_id="NzA2Mzg0ZTY2M2UwNDQ1ZGIwNTkzN2UyNTAzYjc0ZWY=|1556202064|54db52bc727f4c5e23caaf0b1f0fcda7e69ca866"; r_cap_id="OTRlZTdjMDM2MzVhNGJmYTk2YzZmMWNhMDhlZGQyZjA=|1556202064|0421fd4a844da1054453e4a1cbc0fe07d87f6beb"; cap_id="NTY3NDZiMjNiMzM4NGY5M2I0YWJjZWIxYTQ0ZGJmMDk=|1556202064|dda3e0f2a523aa7987e42ebe19fc3f9acb8e1975"; capsion_ticket="2|1:0|10:1556202070|14:capsion_ticket|44:MjJlMzYxYTEzMjBjNDk4ZWJiM2NiNDRmZDk4ZDA3MzA=|c8ed1247b518fc0ab48a6ad943be4bdeb7168b7e88aec08ad5d1f1c4c81fc695"; __gads=ID=d316d3cb1e30450d:T=1556336591:S=ALNI_MalXfST2FYUpkmyho8XMC2Ed9Loog; __utma=155987696.1311869025.1556366312.1556366312.1556366312.1; __utmz=155987696.1556366312.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d',
        "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        'Upgrade-Insecure-Requests': '1',
        "host":"api.zhihu.com"
    }
    response = requests.get(start_url, headers=headers)
    print(response.status_code)
    # print("主进程开始执行>>> pid={}".format(os.getpid()))
    # ps = Pool(5)
    # for i in ["zhihu_paris","zhihu_car","zhihu_icu"]:
    #     # ps.apply(worker,args=(i,))          # 同步执行
    #     ps.apply_async(worker, args=(i,))  # 异步执行
    # 关闭进程池，停止接受其它进程
    # ps.close()
    # 阻塞进程
    # ps.join()
    # print("主进程终止")

# main()
# class User_Spider:
#     def __init__(self):
#         self.mongo = mongodb.MongoDBUtils("zhihu_paris")
#
#     def spider(self):
#         curInfo = self.mongo.distinctID("author.id")
#         print(curInfo[0])

# if __name__ == "__main__":
#     obj = User_Spider()
#     obj.spider()