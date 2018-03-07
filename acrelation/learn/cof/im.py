# coding=utf-8

import cgi
from apiCloud.cof.http import Http
from apiCloud.cof.restful import *

__author__ = 'linsx'


def get_str_list(id_list):
    """
    将list中的元素转换为字符串
    """
    str_list = list()
    for num in id_list:
        str_list.append(str(num))

    return str_list


class SendNew99U(object):
    """
    新99u推送消息接口封装

    QA机器人：

    uri:281474976720219

    password:4abb8356-d8bd-44eb-b8cc-ee6c2a281ad8

    接口协议见 http://wiki.sdp.nd/index.php?title=IM_Core%E5%B7%A5%E5%85%B7_%E4%BB%A3%E7%90%86_v0.2
    """

    def __init__(self):
        """
        初始化
        """
        self.host = "im-agent.web.sdp.101.com"
        self.url = "/v0.2/api/agents/messages"
        self.http_obj = Http(self.host)
        self.header = {
            "Content-Type": "application/json"
        }
        self.rest_o = Restful()

        # 1.获取代理授权信息
        authorization = self.get_agent_mac_token()
        self.header["Authorization"] = authorization

    def get_agent_mac_token(self):
        """
        获取推送号（只能是公众号）的授权信息
        body参数：
        uri: uid
        password: 密码
        返回值：
        {
            "mac_algorithm": "hmac-sha-256",
            "nonce": "1438677808798:2OLebj6B",
            "mac": "aIlsdFuRcV0jji+u+uwAw3hsNFSS2YJ95LnjYS0h9OY=",
            "access_token": "agent_281474976720145"
        }
        """
        # 1.发送请求
        url = "/v0.2/api/agents/users/tokens"
        body = {
            "uri": "281474976720219",
            "password": "4abb8356-d8bd-44eb-b8cc-ee6c2a281ad8"
        }
        param = json.dumps(body)

        self.http_obj.set_header(self.header)

        res = self.http_obj.send('POST', url, param)
        code = 200
        msg = "获取代理用户授权失败"

        data = self.rest_o.parse_response(res, code, msg)

        # 2.拼装数据
        access_token = data['access_token']
        nonce = data['nonce']
        mac = data['mac']
        authorization = 'MAC id="%s",nonce="%s",mac="%s"' % (access_token, nonce, mac)
        return authorization

    def send_to_receivers(self, info, receiver_list):
        """
        发送原始内容到各知照人的99u
        content：内容
        list：需要通知的人的名单，list类型
        """
        # 发送消息
        id_list = get_str_list(receiver_list)
        content = "Content-Type:text/plain\r\n\r\n%s" % info
        body = {
            "filter": [
                {
                    "name": "uri",
                    "args": {
                        "uri_list": id_list
                    }
                }
            ],
            "body": {
                "content": content,
                "flag": 0
            }
        }
        param = json.dumps(body)
        self.http_obj.set_header(self.header)

        code = 200
        msg = "发送消息给个人失败"
        res = self.http_obj.send('POST', self.url, param)
        self.rest_o.parse_response(res, code, msg)

    def send_to_groups(self, info, group_list):
        """
        发送原始内容到99u群
        content：内容
        group_id：群id列表，list类型
        """
        # 发送消息
        id_list = get_str_list(group_list)
        content = "Content-Type:text/plain\r\n\r\n%s" % info
        body = {
            "filter": [
                {
                    "name": "gid",
                    "args": {
                        "gid": id_list
                    }
                }
            ],
            "body": {
                "content": content,
                "flag": 0
            }
        }
        param = json.dumps(body)
        self.http_obj.set_header(self.header)

        code = 200
        msg = "发送消息给群组失败"
        res = self.http_obj.send('POST', self.url, param)
        self.rest_o.parse_response(res, code, msg)

    def send_to_receivers_in_box(self, info, receiver_list, send_type):
        """
        以消息盒子的方式推送
        :param info: 消息内容
        {
            title：// 消息标题,
            content: // 消息内容（测试结果）,
            url: // 报告内容
        }
        :param receiver_list: 接收者列表
        :param send_type: 推送类型， 1是个人、2是群
        :return:
        """
        # 格式化接收者，根据类型设置过滤器
        id_list = get_str_list(receiver_list)

        if send_type == 1:
            body_filter = {
                "name": "uri",
                "args": {
                    "uri_list": id_list
                }
            }
        else:
            body_filter = {
                "name": "gid",
                "args": {
                    "gid": id_list
                }
            }

        # 设置推送内容
        content = """Content-Type:box/xml\r\n\r\n
        <box data-summary="%s">
          <div class="row">
            <div class="col-6">
              <span style="font-weight:bold;">%s</span>
            </div>
          </div>
          <div class="row">
            <div class="col-6">
              <span>%s</span>
            </div>
          </div>
          <hr/>
          <div class="row">
            <div class="col-5">
              <span style="color:#878787;">详情请查看</span>
            </div>
            <div class="col-1">
              <button class="arrow-default" data-href="%s"></button>
            </div>
          </div>
        </box>
        """ % (info['title'], info['title'], info['content'], cgi.escape(info['url']))

        body = {
            "filter": [
                body_filter
            ],
            "body": {
                "content": content,
                "flag": 0
            }
        }
        param = json.dumps(body)
        self.http_obj.set_header(self.header)

        code = 200
        msg = "发送消息失败"
        res = self.http_obj.send('POST', self.url, param)
        self.rest_o.parse_response(res, code, msg)

    def send_pic(self, entry_id, receiver_list):
        """
        发送内容到各知照人的99u
        content：内容
        list：需要通知的人的名单，list类型
        """
        # 发送消息
        id_list = get_str_list(receiver_list)

        info = '<img src="dentry://' + entry_id.encode(
            'utf-8') + '" mime="jpeg" width="240" height="320" fullimage="true" encoding="zip" size="1201024" alt="图片说明" md5="bcb31b38e4c01691881e38023dea69e9" />'

        content = "Content-Type:img/xml\r\n\r\n%s" % info

        body = {
            "filter": [
                {
                    "name": "uri",
                    "args": {
                        "uri_list": id_list
                    }
                }
            ],
            "body": {
                "content": content,
                "flag": 0
            }
        }
        param = json.dumps(body)
        self.http_obj.set_header(self.header)

        code = 200
        msg = "发送消息给个人失败"
        res = self.http_obj.send('POST', self.url, param)

    def send_pic_to_group(self, entry_id, group_list):
        """
        发送图片到99u群
        :param entry_id:
        :param group_list:
        :return:
        """
        # 发送消息
        id_list = get_str_list(group_list)
        info = '<img src="dentry://' + entry_id.encode(
            'utf-8') + '" mime="jpeg" width="240" height="320" fullimage="true" encoding="zip" size="1201024" alt="图片说明" md5="bcb31b38e4c01691881e38023dea69e9" />'

        content = "Content-Type:img/xml\r\n\r\n%s" % info
        body = {
            "filter": [
                {
                    "name": "gid",
                    "args": {
                        "gid": id_list
                    }
                }
            ],
            "body": {
                "content": content,
                "flag": 0
            }
        }
        param = json.dumps(body)
        self.http_obj.set_header(self.header)

        code = 200
        msg = "发送图片给群组失败"
        res = self.http_obj.send('POST', self.url, param)


if __name__ == "__main__":
    # 新99u方式：
    send_o = SendNew99U()
    info = {
        "title": "测试推送",
        "content": "运行时间： 670.959s",
        "url": "http://cdncs.101.com/v0.1/download?dentryId=5792a70f-3740-40ad-aa36-fccaf55e3097&session=77ee4b79-f28d-42d3-9682-1ed12546633b"
    }
    # send_o.send_to_receivers(info, [900109])
    send_o.send_to_receivers_in_box(info, [900109], 1)
    # send_o.send_to_receivers_in_box(info, [11004213, 2148065], 2)
