# coding=utf-8

import os
from apiCloud.cof.api_template import TMPL_PATH
from apiCloudTest.settings import API_TEST_PROJECT_PATH

# __TMPL_PATH = os.path.join(os.path.dirname(TMPL_PATH), 'api_template')

# 本地默认模板路径
PROJECT_TMPL_PATH = os.path.join(API_TEST_PROJECT_PATH, r'template_project\template')  # 模板所在路径
PROJECT_ROOT_PATH = os.path.join(API_TEST_PROJECT_PATH, r'api_project')  # api生成后保存的项目路径
SWAGGER_JSON_ROOT = os.path.join(API_TEST_PROJECT_PATH, r'swagger_json')  # swagger_path.json 上传后保存的位置
a = API_TEST_PROJECT_PATH

API_CALL_CLS_TMPL = os.path.join(os.path.dirname(TMPL_PATH), 'api_call_class_template.txt')
API_CALL_CLS_FUN_TMPL = os.path.join(os.path.dirname(TMPL_PATH), 'api_call_class_def_template.txt')

DATA_STRUCT_CLS_TMPL = os.path.join(os.path.dirname(TMPL_PATH), 'data_struct_class_template.txt')
DATA_STRUCT_CLS_REQUEST_FUN_TMPL = os.path.join(os.path.dirname(TMPL_PATH), 'data_struct_request_def_template.txt')
DATA_STRUCT_CLS_RESPONSE_FUN_TMPL = os.path.join(os.path.dirname(TMPL_PATH), 'data_struct_response_def_template.txt')

TEST_CASE_CLS_TMPL = os.path.join(os.path.dirname(TMPL_PATH), 'test_case_class_template.txt')
TEST_CASE_INIT_TMPL = os.path.join(os.path.dirname(TMPL_PATH), 'test_case_init_template.txt')

# api_call 中的 http 配置文件模板
TEST_CASE_HTTP_TMPL = os.path.join(os.path.dirname(TMPL_PATH), 'api_call_http_template.txt')


# 设置 接口swagger json 跟目录
# SWAGGER_JSON_ROOT = os.path.join(os.path.dirname(swagger_path))


# 类文件下载路径配置


def set_project_path(project_name, project_service, env):
    """
    生成接口所需的所有路径
    :param project_name:
    :param project_service:
    :param env:
    :return:
    """
    # 项目创建后最终保存的位置
    project_path = os.path.join(PROJECT_ROOT_PATH, project_name)
    project_path_dict = dict()
    # 文件路径指定:
    # ./api_project/
    project_path_dict['project_path'] = os.path.join(project_path, project_name)
    # ./api_project/api_call/
    project_path_dict['api_call'] = os.path.join(project_path, 'api_call')
    # ./api_project/api_call/gateway/
    project_path_dict['api_call_service'] = os.path.join(project_path, 'api_call', project_service)
    # ./api_project/api_call/gateway/gateway_call.py
    project_path_dict['api_call_service_api_module'] = \
        os.path.join(project_path, 'api_call', project_service, '%s_call.py' % project_service)
    # ./api_project/data_struct/
    project_path_dict['data_struct'] = os.path.join(project_path, 'data_struct')
    # ./api_project/data_struct/gateway/
    project_path_dict['data_struct_service'] = os.path.join(project_path, 'data_struct', project_service)
    # ./api_project/data_struct/gateway/gateway_data_struct.py
    project_path_dict['data_struct_service_struct_module'] = \
        os.path.join(project_path, 'data_struct', project_service, '%s_data_struct.py' % project_service)
    # ./api_project/testcase/
    project_path_dict['test_case'] = os.path.join(project_path, 'testcase')
    # ./api_project/testcase/test
    project_path_dict['test_case_env'] = os.path.join(project_path, 'testcase', env)
    # ./api_project/testcase/test/gateway
    project_path_dict['test_case_env_service'] = os.path.join(project_path, 'testcase', env, project_service)

    return project_path_dict
