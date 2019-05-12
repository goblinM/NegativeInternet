import redis

from app.spider.setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY


class RedisClient:
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        """
        初始化
        :param host: 地址
        :param port: 端口号
        :param password: 密码
        """
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    def add(self,uid):
        """
        添加知乎用户唯一id值
        :param uid: 用户id
        :return: ok
        """
        self.db.zadd(REDIS_KEY,uid)
        return "ok"


