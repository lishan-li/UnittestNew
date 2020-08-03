
import json
import sys
import unittest
import utils
import requests
from ddt import ddt, file_data
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from testData.data_driver import get_data_file
from testcase.common.loggerInfo import logInfo

from testcase.common.getcookie import test_cookieGet
from testcase.common.gettoken import test_tokenGet



_data_file_get_message = 'test_api.json'

@ddt
class Test(unittest.TestCase):

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
    def test_sendMessage(self, request_id, to_id, type, content,chat_send_option):
     time.sleep(5)
    # 初始化参数
     params = {}
     self.request_id = request_id
     self.to_id = to_id
     self.type = type

     self.content = content
    # self.chat_send_option = chat_send_option
    # 消息发送
    # url_postMessage = "https://seller.sg.test.shopee.cn/webchat/api/v1.1/messages?_uid=0-439511&_v=3.9.0"
     url_postMessage="https://seller.test.shopee.sg/webchat/api/v1.1/messages?_uid=0-9018157&_v=3.10.0"



     payload = {
        'request_id': request_id,
        'to_id': to_id,
        'type': type,
        'content': content,
        'chat_send_option': chat_send_option
    }



     sesion=requests.session()
     sesion=test_cookieGet(self,sesion)
     result=test_tokenGet(self,sesion).json()
     token=result['token']



    # headers = {
      # "authorization": " ".join(["Bearer", token])
      # "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVfdGltZSI6MTU5NTg1NzM5NiwiaWQiOiIwNmY4OTE2NC1kMDBjLTExZWEtYjBiOS1iNDk2OTE1ZWZlNWUifQ.JmP_OA-GpsA89zMcenR-TKAdqPMDiUDT2CxKNZ9J_T8"
      #}


     sesion.headers.update({"authorization": " ".join(["Bearer", token])})

     #print(sesion.headers.get('authorization'))


     resMess = sesion.post(url_postMessage, data=json.dumps(payload))




     logInfo(self,resMess)
     self.assertEqual(resMess.status_code, 200)
     return resMess


