from scrapy.cmdline import execute
'''
每日热点的爬取
'''
def run_hot():
    execute('scrapy crawl hotdaily'.split())
run_hot()