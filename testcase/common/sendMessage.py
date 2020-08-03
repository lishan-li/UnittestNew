import requests
import json
import utils


from testcase.common.getcookie import test_cookieGet
from testcase.common.gettoken import test_tokenGet

def test():
    self='test'
    payload ={"request_id": "b101382f-3be9-45c0-9c10-8fbfb873b76f", "to_id": 9030516, "type": "text",
     "content": {"text": "test"},
     "chat_send_option": {"force_send_cancel_order_warning": False, "comply_cancel_order_warning": False}}

    #headers = {
    #"authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVfdGltZSI6MTU5NTg2NzMzMCwiaWQiOiIwNmY4OTE2NC1kMDBjLTExZWEtYjBiOS1iNDk2OTE1ZWZlNWUifQ._a7OSme0R8y8762UFWSah5JIBJGQddU5hQPXxxjL2jY"
    # }
    a="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVfdGltZSI6MTU5NTg2NzMzMCwiaWQiOiIwNmY4OTE2NC1kMDBjLTExZWEtYjBiOS1iNDk2OTE1ZWZlNWUifQ._a7OSme0R8y8762UFWSah5JIBJGQddU5hQPXxxjL2jY"

    # url_postMessage = "https://seller.sg.staging.shopee.cn/webchat/api/v1.1/messages?_uid=0-439511&_v=3.9.0"
    url_postMessage = "https://seller.test.shopee.sg/webchat/api/v1.1/messages"
    sesion = requests.session()
    sesion = test_cookieGet(self, sesion)
    result = test_tokenGet(self, sesion).json()
    token = result['token']
    sesion.headers.update({"authorization":  " ".join(["Bearer", token])})
    res= sesion.post(url_postMessage, data=json.dumps(payload))
    print(sesion.headers.get('authorization'))
    print(res.content)
    print(res.status_code)



if __name__ == '__main__':
    test()