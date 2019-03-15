import unittest
from ..api_call.register_service import ReService
from ..public.data import CreatPhone


class PostRegister(unittest.TestCase):

    def setUp(self):
        self.base = ReService()
        self.phone = CreatPhone().mobole_phone()

    def test_001(self):
        data = {
            'type': 1,
            'uid': 'MjAxODEwMjUxMDU5MzkwLjk1MTYyMTk1MTY3MzY4NjQ=',
            'verifyCode': 'wnyz',
            'tel': self.phone,
            'smsType': '0',
            'telCode': '111111',
            'password': 'a11111',
            'recommend': ''
        }
        resp = self.base.post_register(data=data).text
        print(resp)
        data = {
            'type': '2',
            'uid': 'MjAxODEyMTMxNDAzMjIwLjA5Nzk3ODg3ODc4MDgwMDg2',
            'loginName': self.phone,
            'password': 'a11111',
            'verifyCode': ''
        }
        resp = self.base.post_login(data=data).text
        print(resp)

    # def test_002(self):


    def tearDown(self):
        pass

    # if __name__ == '__main__':
    #     unittest.main()


# class Test(unittest.TestCase):
#         def setUp(self):
#             print("start!")

# def test(self):
#     url = 'http://tinstitutionapi.shitou.local:80/institution/institutionUserService/institutionRegister'
#     # url = 'http://18.16.200.15:5200/institution/institutionUserService/institutionRegister'
#     headers = {'ST-CLIENT-ID': 'JISUY'}
#     order = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#     para = {
#         "order_id": order,
#         "type": "03",
#         "name": "卫魏黄",
#         "id_card": "340101197705051337",
#         "tel": "13816764900",
#         "ret_url": "http://www.baidu.com"
#     }
#     print('开户签约订单号为：%s' % order)
#     resp = requests.post(url, json=para, headers=headers)
#     print('开户申请结果为：%s' % resp.text)
#         def tearDown(self):
#             print("end!")
#
#         def test01(self):
#             print('111')
#
#         def test02(self):
#             print('222')
#
#         def test03(self):
#             print('333')


if __name__ == '__main__':
    unittest.main()
