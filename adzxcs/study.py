import json
import pprint
import requests
import unittest
import re


class CivaTutorbalance(unittest.TestCase):
    '''获取外教卡余额'''

    #     def test1(self):
    #         burl = "http://192.168.0.201:8083/eclp-service/user/v1/getTOlmytutorByUId.do"
    #         para = json.dumps({
    #             'userId': '00014ea3-9aca-4385-8145-b2fe7cb5e2e3',
    #             'classType': '0'
    #
    #         })
    #         headers = {'Content-type': 'application/json'}
    #
    #         response = requests.post(url=burl, headers=headers, data=para)
    #         # 获取响应时间，单位s
    #         ResponsesTime = response.elapsed.total_seconds()
    #         print(burl)
    #         # 输出接口响应时间等信息
    #         print('响应时间(s):', ResponsesTime, 'Code:', response.status_code)
    #         # 输出接口返回结果
    #         # pprint.pprint(response.json())
    #         print(response.json())
    #
    #
    # class CivaTutorconsume(unittest.TestCase):
    #     '''外教卡扣除使用'''
    #
    #     def test1(self):
    #         burl = "http://192.168.0.201:8083/eclp-service/user/v1/tOlmytutorUse.do"
    #         para = json.dumps({
    #             'userId': '3ddb0ef63d6942e39ef7d31e4ec15323',
    #             'classType': '0',
    #             'token': 'JSESSIONID=645f850d-b080-4b81-89a3-548003ac9b96'
    #         })
    #         headers = {'Content-type': 'application/json'}
    #
    #         response = requests.post(url=burl, headers=headers, data=para)
    #         # 获取响应时间，单位s
    #         ResponsesTime = response.elapsed.total_seconds()
    #         print(burl)
    #         # 输出接口响应时间等信息
    #         print('响应时间(s):', ResponsesTime, 'Code:', response.status_code)
    #         # 输出接口返回结果
    #         # pprint.pprint(response.json())
    #         print(response.json())

    def guest_addevent_test(self):
        burl = "http://127.0.0.1:8001/api/add_event/"
        para = json.dumps({
            "eid": "10",
            "name": "添加发布会接口自测",
            "limit": "500",
            "status": "false",
            "address": "河坊街1号",
            "start_time": "2018-08-18 18:18:18"
        })
        headers = {'Content-type': 'application/json'}

        response = requests.post(url=burl, headers=headers, data=para)
        # 获取响应时间，单位s
        ResponsesTime = response.elapsed.total_seconds()
        print(burl)
        # 输出接口响应时间等信息
        print('响应时间(s):', ResponsesTime, 'Code:', response.status_code)
        # 输出接口返回结果
        # pprint.pprint(response.json())
        print(response.json())


if __name__ == '__main__':
    unittest.main()
#
# str = 'w@ww.#ba#idu?.co?m'
# sentences = re.split(r"[.@?#]", str)
#
# print(sentences)
