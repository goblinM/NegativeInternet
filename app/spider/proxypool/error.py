"""
自定义的错误锦集
"""
class PoolEmptyError(Exception):
    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        # repr将对象转化为供解释器读取的形式。
        return repr('代理池已经枯竭')