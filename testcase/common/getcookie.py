import sys
import requests
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from testcase.common.loggerInfo import logInfo




def test_cookieGet(self,sesion):
    # 第一步获取cookie

         url = "https://seller.test.shopee.sg/api/v2/login"


         mainpayload = {
     "captcha_key":"af0b0edeebd84119a91d757d5878997d",
     "password_hash":"24924418d9fce29a5bca4bfccb60c8c5581c8b470215513b52b1cccc4cb590b8",
     "username":"test_tsx_email"
         }



# 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里。
         responsetest = sesion.post(url,data=mainpayload)
         if responsetest.status_code==481:
            mainpayload['vcode']= '123456'
            response=sesion.post(url,data=mainpayload)
            logInfo(self,response)

         return sesion


#if __name__ == '__main__':

#  sesion=requests.session()
#  res=test_cookieGet("test",sesion)
#  print(res)