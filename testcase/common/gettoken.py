import sys
import requests
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from testcase.common.loggerInfo import logInfo

def test_tokenGet(self,sesion):

    # 第二步登陆
    url_getLogin = "https://seller.test.shopee.sg/webchat/api/v1.1/login?_v=3.9.0"

    formdata = {

    "_v": "3.9.0"

     }

    # 请求发送

    res = sesion.post(url_getLogin, data=formdata)

    logInfo(self, res)

    return res