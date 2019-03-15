import unittest
from ..public import base


# class post_register(unittest.TestCase):

    # def setUp(self):
    #     endurl = 'api-proxy/wxapi/v4/user/userInformation.do'
    #     self.url = base.get_url(endurl)
    #
    # def test_001(self):
    #     params = {
    #         'type': '1',
    #         'uid': 'MjAxODExMjkxNzEyMjYwLjEwNzMwMTYwNjE3ODgzNjU1',
    #         'tel': '15899990253',
    #         'verifyCode': 'wnyz',
    #         'password': 'a11111'
    #     }
    #     DataALL = {'params': params}
    #     Method = 'post'
    #     resp = base.get_req_way(self.url, Method, **DataALL)
    #     print(self.url)
    #
    # def tearDown(self):
    #     pass
    #
    # if __name__ == '__main__':
    #     unittest.main()


# class Test(unittest.TestCase):
#         def setUp(self):
#             print("start!")
#
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


# if __name__ == '__main__':
#     # list1 = [1, 2, 3, 4, 5, 5, 3, 2]
#     # list2 = []
#     # for i in range(len(list1)):
#     #     if list1[i] not in list2:
#     #         list2.append(list1[i])
#     # print(list2)
#     nums = [1,3,2,8,5,34,8,33,6,4332,2,6,]
#
#     def maopao(nums):
#         for i in range(len(nums)-1):
#             for j in range(len(nums)-i-1):
#                 if nums[j]>nums[j+1]:
#                     nums[j],nums[j+1]=nums[j+1],nums[j]
#         return nums
#
#
#     print(maopao(nums))
#
#     list1 = [1,2,4,2,66,3,76,4,4,6,6,7,7,8,8,9]
#     list2 = []
#     for i in list1:
#         if i not in list2:
#             list2.append(i)
#     print(list2)
#
