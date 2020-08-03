# 导入验证器
from jsonschema import validate

# 编写schema：
_message_resp_schema = {
    "type": "object",
    "properties": {
        "token": {"type": "string"},
        "p_token": {"type": "string"},
        "user": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer","enum" : [439511]},
                        "uid": {"type": "string","enum" : ['0-439511']},
                        "name": {"type": "string","enum" : ['tsx_staging_sg1']},
                        "type": {"type": "string","enum" : ['seller']},
                        "avatar": {"type": "string"},
                        "locale": {"type": "string"},
                        "shop_id": {"type": "integer","enum" : [439512]},
                        "country": {"type": "string","enum" : ['SG']},
                        "status": {"type": "string","enum" : ['normal']}
                    }

                },
         "version": {"type": "integer"},
            },
         "required": [ "token", "p_token", "user","version"]
}

# json数据：
json_data = {
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVfdGltZSI6MTU5NTQyNDE5NSwiaWQiOiI3ZmU0MmRlYy1jYzFlLTExZWEtODAzNC1jY2JiZmVkZjJhMWEifQ.fUSaAwiVfEfBz8yRmRQIulH5mLoNRBklTA76s9XOUVo",
    "p_token":"cnlQSXNtYjdsNXJDd0J2asqqVGy7V+am58l3YJWkxzM=",
    "user":{
        "id":322265,
        "uid":"0-322265",
        "name":"test_sg_002",
        "type":"seller",
        "avatar":"",
        "locale":"zh-Hant",
        "shop_id":322266,
        "country":"SG",
        "status":"normal"
    },
    "version":1
}

# 验证：
#validate(instance=json_data, schema=_message_resp_schema)