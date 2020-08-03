import requests
import unittest
from ddt import ddt, file_data
import os
import sys
import json
from jsonschema import validate

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from testData.data_driver import get_data_file


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from testcase.common.loggerInfo import logInfo

from testcase.common.resultValidate import _message_resp_schema


_data_file_get_message = 'test_login.json'

@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass


    def tearDown(self):
        pass

    @file_data(get_data_file(_data_file_get_message))
    def test_loginIn(self,captcha_key,password_hash,username,vcode):

      #初始化参数
      self.captcha_key = captcha_key
      self.password_hash = password_hash
      self.username = username
     # self.vcode = vcode

      #第一步获取cookie

      url = "https://seller.staging.shopee.sg/api/v2/login"

      payload = {'captcha_key': captcha_key,
                 'password_hash': password_hash,
                 'username': username}



      # 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在sesion里。

      sesion = requests.session()

      response = sesion.post(url,data=payload)
      if response.status_code == 481:
          payload['vcode'] = '123456'
          response = sesion.post(url, data=payload)
          logInfo(self,response)



      #第二步登陆
      url_getLogin = "https://seller.staging.shopee.sg/webchat/api/v1.1/login?_v=3.9.0"


      #请求发送


      res=sesion.post(url_getLogin)

      logInfo(self, res)

      #结果校验
      self.assertEqual(res.status_code, 200)

      if res.status_code == 200:
         validate(json.loads(res.content.decode()), _message_resp_schema)