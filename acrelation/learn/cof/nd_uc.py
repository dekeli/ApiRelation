# coding=utf-8
import json
import subprocess

from apiCloud.cof.http import Http
from apiCloud.cof.nd_path import NdPath

nd_path_o = NdPath()


class UcEnv:
    ol = 1
    pre = 2
    aws = 3
    awsca = 4


class NdUc(object):
    def __init__(self, env=UcEnv.ol):
        self.version = 0.93
        self.env = env
        self.port = None

        if self.env == UcEnv.ol:
            self.host = "aqapi.101.com"
        elif self.env == UcEnv.pre:
            self.host = "ucbetapi.101.com"
        elif self.env == UcEnv.aws:
            self.host = "awsuc.101.com"
        elif self.env == UcEnv.awsca:
            self.host = "uc-awsca.101.com"

        # 目前，uc的生产、预生产环境，都使用https协议
        if self.env in [UcEnv.ol, UcEnv.pre, UcEnv.aws, UcEnv.awsca]:
            self.is_ssl = True
        else:
            self.is_ssl = False

        self.header = {
            "Content-Type": "application/json"
        }

    def set_host(self, host):
        """
        自定义设置账号中心主机
        :param host:
        :return:
        """
        self.host = host

    def set_port(self, port):
        """
        自定义设置账号中心端口
        :param port:
        :return:
        """
        self.port = port

    def set_version(self, version):
        """
        自定义设置账户中心的api版本号
        :param version:
        :return:
        """
        self.version = version

    @staticmethod
    def get_password_md5(passwd):
        """

        该函数用于获取加密过的密码

        :param passwd: 要加密的明文密码

        :return:

        调用DEMO

        .. code-block:: python
            :linenos:

        这里的password_md5就是加密后的密码了

        """
        passwd = passwd.replace('`', '\`')
        passwd = passwd.replace('\'', '\\\'')
        passwd = passwd.replace('"', '\\\"')

        jlib_path = nd_path_o.get_jlib_path()

        md5_jar_path = jlib_path + 'md5.jar'
        command = 'java -jar "' + md5_jar_path + '" \"%s\"' % passwd
        proc = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        error = proc.stderr.read()
        passwd_md5 = proc.stdout.read()
        return passwd_md5.strip()

    def get_server_time(self):
        """
        获取服务器时间

        :return:

        .. code-block:: python
            :linenos:

        """
        http_o = Http(self.host, self.port, ssl=self.is_ssl)

        res = http_o.send('get', '/v' + str(self.version) + '/server/time')

        res = res['data']

        res = json.loads(res)

        return res['server_time']
