import unittest
from ..api_call.query import Query
from ..public.Assert import Assertions
import pytest
import allure
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


# @allure.feature('查询号码归属地')
def test_query():
    base = Query()
    assert_0 = Assertions()
    data = {
        'tel': '15638743707'
    }
    resp = base.query_phone(data)
    print(resp)
    assert_0.assert_code(resp['code'],200)
    assert_0.assert_in_text(resp['text'],'河南')
    s = eval(resp['text'])
    print(s)
