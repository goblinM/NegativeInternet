import os

#MySQL数据库的配置
# defaultMysql = MongoTools.objects.filter(mongoChoice="T",dataType="mysql")[0]
# default_mysql_name = "xxx"
# default_mysql_user = "xxx",
# default_mysql_password = "xxx"
# default_mysql_host = "127.0.0.1"
# default_mysql_port = "3306"


#'''rabbitMQ数据库的配置'''
# defaultRabbitmq = MongoTools.objects.filter(mongoChoice="T",dataType="rabbitmq")[0]
# default_rabbit_user = defaultRabbitmq.mongoUser   #"xxx"
# default_rabbit_password = defaultRabbitmq.mongoPwd   #"xxxx"
# default_rabbit_host = defaultRabbitmq.ip   #"xxx.xxx.xx.xx"
# default_rabbit_port = defaultRabbitmq.port  #xxx
# default_rabbit_name = defaultRabbitmq.client  #"xx"


# #MongoDB数据库配置
# defaultMongo = MongoTools.objects.filter(mongoChoice="T",dataType="mongo")[0]
default_mongo_host = "127.0.0.1"  #"192.168.100.179"
default_mongo_port = 27017  #27018
default_mongo_name = "NegativeInternet"  # "CII_db2"#
default_mongo_user = "admin"  #admin
default_mongo_password = "password"  #password