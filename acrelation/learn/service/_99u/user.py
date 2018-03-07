# coding=utf-8

from learn.service.co_token.uc import *

__author__ = 'Administrator'


def get_user_face(uid):
    """
    获取用户头像
    :param uid:
    :return:
    """
    url = "http://cs.101.com/v0.1/static/cscommon/avatar/%s/%s.jpg?size=120" % (str(uid), str(uid))
    return url


class UcUserAction(object):
    def __init__(self):
        uc_env = UcEnv.ol       # 只对接uc无锡环境的账号
        self.token_o = UcToken(uc_env)
        self.rest_o = CoRestful.Restful()

    def login_with_user_info(self, uid, password):
        """
        获取用户名
        成功，200，返回用户的基本信息
        失败，401，返回msg
        :param uid: 用户id
        :param password: 密码
        :return:
        成功，用户姓名；
        失败，错误信息
        """
        # 登录
        login_res = dict()

        try:
            user_info = self.token_o.get_user_info(uid, password)
            face_url = get_user_face(uid)
            login_res['code'] = 200
            login_res['user_name'] = user_info['org_exinfo']['real_name']
            login_res['face'] = face_url
            login_res['msg'] = '登录成功'
        except Exception as e:
            login_res['code'] = 0
            login_res['user_name'] = ''
            login_res['face'] = ''
            login_res['msg'] = '登录失败：' + str(e)

        return login_res


if __name__ == "__main__":
    pass
