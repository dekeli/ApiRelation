from ..public.HttpService import *


class ReService(BaseHttp):
    def __init__(self, env="test"):
        """
        初始化方法
        各个接口方法封装中需要的公共内容
        """
        BaseHttp.__init__(self, env=env)

    def post_register(self, data):
        url = '/api-proxy/wxapi/v4/user/register.do'
        resp = self.post(url=url, body=data)
        return resp

    def post_login(self, data):
        url = '/api-proxy/wxapi/v4/user/login.do'
        resp = self.post(url=url, body=data)
        return resp
