# coding=utf-8

from apiCloud.service.co_token.uc import *
from apiCloud.views.schedule_list_view import get_mac_content

__author__ = 'Administrator'


def get_mac_token_by_session(request, url, method, host):
    """
    根据session中的用户信息，获取mac_token
    :param request: 请求
    :param url:
    :param method:
    :param host:
    :return:
    """
    token_id = request.session.get("access_token")
    mac_key = request.session.get("mac_key")
    mac_token = get_mac_content(url, method, host, token_id, mac_key)
    return mac_token


class SdpApp(object):
    def __init__(self):
        uc_env = UcEnv.ol  # 只对接uc无锡环境的账号
        self.token_o = UcToken(uc_env)
        self.rest_o = CoRestful.Restful()
        self.host = 'sdp-portal-server.pre1.web.nd'
        self.http_obj = cofHttp.Http(host=self.host)
        self.header = dict()

    def get_app_list(self, request=None, uid='', password=''):
        """
        获取当前用户有权限的sdp应用列表
        成功，200，返回用户的基本信息
        失败，401，返回msg
        :param request: 请求
        :param uid: 用户id（没有带组织）
        :param password: 密码
        :return:
        成功，sdp应用列表，结构：
            {
                "oid": "xxxxxxxxxx",
                "name": "xxx",
                "nick_name": "xxxxxx"
            }
        失败，错误信息
        """
        res = dict()
        app_list = list()

        try:
            url = '/v0.2/app?type=PORTAL_GET_APP_LIST&name=group'
            method = 'GET'
            # 只支持uc生产环境的 @nd 组织账号
            if not request and uid and password:
                access_token = self.token_o.get_token(uid, password, org='nd', url=url, method=method, host=self.host)
            else:
                access_token = get_mac_token_by_session(request, url=url, method=method, host=self.host)
            self.header['Authorization'] = access_token
            self.http_obj.set_header(self.header)

            response = self.http_obj.send(method, url)
            data = self.rest_o.parse_response(response, 200, '获取SDP应用列表失败')
            app_object = data['object']

            if app_object:
                app_type_object_list = app_object['app']
                for app in app_type_object_list:
                    app_list.append({
                        'oid': app['oid'],
                        'name': app['name'],
                        'nick_name': app['chinese_name'] if app['chinese_name'] else ''
                    })
                component_type_object_list = app_object['component']
                for component in component_type_object_list:
                    app_list.append({
                        'oid': component['oid'],
                        'name': component['name'],
                        'nick_name': component['chinese_name'] if component['chinese_name'] else ''
                    })
                groups_type_object_list = app_object['groups']
                for group in groups_type_object_list:
                    for app in group['apps']:
                        app_list.append({
                            'oid': app['oid'],
                            'name': app['name'],
                            'nick_name': app['chinese_name'] if app['chinese_name'] else ''
                        })
            res['msg'] = '获取SDP应用列表成功'
        except Exception as e:
            res['msg'] = '获取SDP应用列表失败：' + str(e)

        res['app_list'] = app_list
        return res


if __name__ == "__main__":
    pass
