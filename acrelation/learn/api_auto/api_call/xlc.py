from ..public.HttpService import *


class XlcService(BaseHttp):
    def __init__(self, env="test_xlc"):
        """
        初始化方法
        各个接口方法封装中需要的公共内容
        """
        BaseHttp.__init__(self, env=env)

    def commit_query_order(self,data):
        url = '/order/garage/inquiry/create'
        resp = self.post(url=url,params=data)
        return resp