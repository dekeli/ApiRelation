__author__ = ''
import json
import pprint
from hamcrest import *

class ResponseCheck(object):
    def parse_response(self, response, code, message):
        """
        解析请求接口返回的数据。
        若与期望相符，则返回data_dec；否则直接断言失败，跳出case。
        :param response: 返回的数据；
        :param code: [整型]请求所期望返回的code；
        :param message: 错误时需要指明的信息；
        :return: data_dec，转换为json格式之后的data字段
        """
        data = response['Data']
        data_dec = dict()
        if response['Code'] != code:  # 状态码错误
            if len(data) == 0:  # 判断data有没有内容
                error = message + "，\n状态码：" + str(response['Code']) + "\请求为：" + str(response['Request'])
            else:  #判断状态码
                try:
                    data_dec = json.loads(data)
                except Exception as e:
                    error = message + "，返回数据为： " + str(response['Code']) + "，数据不是json格式的，\n请求为：" + str(
                        response['Request'] + "，返回数据为： " + str(response['Data']))
                    assert_that(response['Code'], equal_to(code), error)
                # 如果返回的data里面没有message字段，直接输出data
                if 'message' in data_dec:
                    error = ''
                    if data_dec['message']:
                        error = message + "，\n状态码：" + str(response['Code']) + "，\n错误信息：" + data_dec['Message'].encode(
                            'utf-8') + "，\n请求为：" + str(response['Request'])
                    else:
                        error = message + "，\n状态码：" + str(response['Code']) + "，\n错误信息为空，\n请求为：" + str(response['Request'])
                    assert_that(response['Code'], equal_to(code), error)
        else: # 状态码正确
            if len(data) == 0:
                return dict()
            else:
                try:
                    data_dec = json.loads(data)
                except Exception as e:
                    error = message + "，\n状态码：" + str(response['Code']) + "，数据不是json格式的，\n请求为：" + str(
                        response['Request'] + "返回数据为： " + str(response['Data']))
                    assert_that(error, equal_to(""), e)
                    return data_dec