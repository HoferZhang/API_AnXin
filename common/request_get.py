# -*- coding: utf-8 -*-
# @Time    : 2018.7.13 15:56
# @Author  : Hofer


import requests
import json


# GET 请求
def request_get(url, params):
    rsp = requests.get(url=url, params=params)
    rsp_json = json.loads(rsp.text)

    code = rsp_json["resCode"]
    result.append(code)
    print(str(case_id) + "." + str(result[3]) + ':' + str(code))

    if code == result[5]:
        result.append("pass")
        result.append(rsp_json["resDesc"])
        result.append(rsp.text)
    else:
        result.append("fail")
        result.append(rsp_json["resDesc"])
        result.append(rsp.text)
    return result


# POST 请求
def request_post(case_file, case_id, url, data):
    result = get_case(case_file, case_id)

    rsp = requests.post(url=url, data=data)
    rsp_json = json.loads(rsp.text)

    code = rsp_json["resCode"]
    result.append(code)
    print(str(case_id) + "." + str(result[3]) + ':' + str(code))

    if code == result[5]:
        result.append("pass")
        result.append(rsp_json["resDesc"])
        result.append(rsp.text)
    else:
        result.append("fail")
        result.append(rsp_json["resDesc"])
        result.append(rsp.text)
    return result