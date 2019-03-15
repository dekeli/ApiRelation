from ..public.HttpService import *


class QipeiService(BaseHttp):
    def __init__(self, env="test_qipei"):
        """
        初始化方法
        各个接口方法封装中需要的公共内容
        """
        BaseHttp.__init__(self, env=env)

    def quotation(self, data):
        url = '/order/dealer/quotation/create'
        resp = self.post(url=url, params=data)
        return resp

    def accept_order(self, data):
        base = BaseHttp()
        url = 'http://devapi.phc-dow.com/order/dealer/purchase/{}/confirm'.format(data)
        resp = base.post(url=url)
        return resp
