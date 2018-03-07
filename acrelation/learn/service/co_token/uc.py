# coding=utf-8

import os
import time
from learn.cof.proc import CoProc
import learn.cof.http as cofHttp
from learn.cof.nd_uc import *
import learn.cof.restful as CoRestful


def get_md5_pw(password):
        """
        根据uc的算法，对密码加密
        """
        p = os.path.abspath(__file__)
        p = os.path.dirname(p)
        md5_jar = p + os.sep + 'md5.jar'

        cmd = 'java -jar ' + md5_jar + ' %s' % password

        res = CoProc().run(cmd)
        return res['result'][:-2]


def get_beijing_time(utc_time):
    """
    根据iso时间获取北京时间
    utc_time 评价的创建时间，utc格式，'2015-12-28T03:05:56.000+0000'
    """
    real_time = utc_time[:-9]
    time_array = time.strptime(real_time, "%Y-%m-%dT%H:%M:%S")
    time_stamp = int(time.mktime(time_array))

    beijing_time_stamp = time_stamp + 60 * 60 * 8
    # beijing_time_stamp = time_stamp
    beijing_time = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(beijing_time_stamp))

    return beijing_time


class UcToken(NdUc):
    """
    通过uc获取token
    """
    def __init__(self, env):
        """
        :param env: 指定配置文件中的环境名称
        """
        self.env = env
        super(UcToken, self).__init__(self.env)

        # 声明一些参数
        self.rest_o = CoRestful.Restful()

        # uc账号相关数据
        self.user_id = ''
        self.access_token = ''
        self.mac_key = ''

        self.http_obj = cofHttp.Http(host=self.host, port=self.port, ssl=self.is_ssl)
        self.http_obj.set_header(self.header)

    def get_server_time(self):
        """
        获取服务器时间
        """
        self.http_obj.set_header(self.header)
        response = self.http_obj.send('get', "/v0.93/server/time")

        data_dict = self.rest_o.parse_response(response, 200, '获取系统时间失败')
        # assert_that(data_dict, has_key('server_time'))
        server_time = data_dict['server_time']

        return server_time

    # ------------- 个人接口 ---------------- #
    def get_user_info(self, user_id, password):
        """
        获取用户信息
        :return:
        """
        org = 'nd'
        url = '/v0.93/users/' + str(user_id)
        method = 'GET'
        host = self.host
        access_token = self.get_token(user_id, password, org, url, method, host)
        self.header['Authorization'] = access_token
        self.http_obj.set_header(self.header)
        response = self.http_obj.send(method, url)
        data_dict = self.rest_o.parse_response(response, 200, '获取用户信息失败')
        return data_dict

    # -------------- 生成mac token ----------------- #
    def get_mac_content(self, url, method, host):
        """
        :name 获取Authorization - os方法
        :param
        #.  id token
        #.  time 2014-12-24T12:23:12Z 时间
        #.  host 访问的域名（非默认端口号时，需要加上端口号）
        #.  method  获取方法
        注：一般没生成authorization，是因为没有事先登录，获取token
        """
        token_id = self.access_token

        server_time = self.get_server_time()
        server_time = server_time.encode('UTF-8')   # 2017-06-06T10:09:02.048+0000
        if self.env in [UcEnv.aws, UcEnv.awsca]:
            server_time = get_beijing_time(server_time)     # 加8小时

        p = os.path.abspath(__file__)
        p = os.path.dirname(p)
        tok_jar = p + os.sep + 'token.jar'

        # 调用jar[命令跟dos下一样]
        url = url.replace('$', '*')
        # print "------------------ begin jar"
        cmd = 'java -jar "' + tok_jar + '" %s %s %s %s "%s" %s' % (
            token_id, server_time, host, method, url, self.mac_key
        )
        # print "------------------ end jar"
        # print cmd

        res = CoProc().run(cmd)
        authorization = res['result'][:-2]
        # print authorization

        return authorization

    def login(self, login_name, password, org_name="", has_encoded=False):
        """
        4.1.3 用户登陆
        {
            "login_name":"", --用户名或手机号或工号
            "password":"", --密码(加密算法由uc_sdk提供)
            "org_name":"", --组织登录名称(可选)
        }
        """
        nd_uc_o = NdUc()

        if has_encoded is False:    # 未加密
            md5_pw = nd_uc_o.get_password_md5(password)
        else:                       # 已加密
            md5_pw = password

        json_data = {
            "login_name": login_name,
            "password": md5_pw,
            "org_name": org_name
        }

        param = json.dumps(json_data)

        self.http_obj.set_header(self.header)

        url = '/v0.93/tokens'
        response = self.http_obj.send('post', url, param)

        return response

    def get_token(self, user, password, org='', url='', method='', host='', has_encoded=False):
        """
        用户登录，获取mac token
        :param user:用户名
        :param password:密码
        :param org:组织，无组织可不传
        :param url:请求的相对url，如 '/user'
        :param method:请求方法，如 'GET'
        :param host:请求的host，不是指uc的host
        :param has_encoded:密码是否已加密
        :return:登录后获取到的token
        """
        # 1.登录
        response = self.login(user, password, org, has_encoded)
        data_dict = self.rest_o.parse_response(response, 201, '用户登陆失败')

        # 2.获取身份信息
        self.user_id = data_dict['user_id']
        self.access_token = data_dict['access_token']
        self.mac_key = data_dict['mac_key']

        if len(url) == 0:
            raise Exception("url不能为空")

        if len(method) == 0:
            raise Exception("http method不能为空")

        mac_token = self.get_mac_content(url, method, host)

        return mac_token

    # -------------- 生成bearer token ----------------- #
    def server_login(self, username, password=None, has_encoded=False):
        """
        4.1.14 服务端登录
        {
            "username"：用户名或手机号
            "password"：密码     【使用后台配置好的密码，如下代码所写】
        }
        注：服务端登录没有对应的退出
        """
        if has_encoded is False:
            md5_pw = get_md5_pw(password)
        else:
            md5_pw = password

        json_data = {
            "login_name": username,
            "password": md5_pw
        }
        param = json.dumps(json_data)

        url = "/v0.93/bearer_tokens"
        response = self.http_obj.send('post', url, param)
        return response

    def get_bearer_token(self, user_name='', password='', has_encoded=False):
        """
        通过服务端登录，获取bearer token
        :param user_name: 用户名
        :param password: 密码
        :param has_encoded: 密码是否已加密
        :return:登录返回的bearer token
        """
        response = self.server_login(user_name, password, has_encoded)
        data_dec = CoRestful.Restful().parse_response(response, 201, "服务端登录失败")

        return data_dec['access_token']
