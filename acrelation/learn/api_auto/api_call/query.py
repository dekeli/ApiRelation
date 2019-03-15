from ..public.HttpService import *


class Query(BaseHttp):
    def __init__(self, env="test"):
        """
        初始化方法
        各个接口方法封装中需要的公共内容
        """
        BaseHttp.__init__(self, env=env)

    def query_phone(self, data):
        url = '/cc/json/mobile_tel_segment.htm'
        resp = self.get(url=url, params=data)
        return resp

