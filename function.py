import requests
import json
import re
from text_config import *


def check_points(str):
    try:
        str = str.strip("查询")
        res = re.search('(1[0-9]{10})', str).group(1)
        return res
    except:
        return False


def check_url(url):
    try:
        url = url.strip()
        res = re.search('(https://h5.ele.me/hongbao/.*)', url).group(1)
        return res
    except:
        return False


def check_phone(phone):
    try:
        phone = phone.strip()
        res = re.search('(1[0-9]{10})', phone).group(1)
        return res
    except:
        return False


def change_url(url):
    try:
        url = url.strip()
        res = re.search('(https*://.*)', url).group(1)
        result = requests.get(res)
        url = result.url
        return url
    except:
        return False


def points_back(phone):
    data = {
        "phone": phone,
    }
    r = requests.get("http://hb-api.newitd.com/user_info", data, timeout=30)
    if r.status_code == 200:
        json_result = r.text[5:-1]
        js_res = json.loads(json_result)
        return js_res["code"], js_res["info"]
    else:
        return -500, fail_to_connect_server_text


def take_bind_id(phone, id, type):
    data = {
        "phone": phone,
        "id": id,
        "type": type
    }
    r = requests.get("http://hb-api.newitd.com/take_bind_id", data, timeout=30)
    if r.status_code == 200:
        json_result = r.text[5:-1]
        js_res = json.loads(json_result)
        return js_res["code"], js_res["info"]
    else:
        return -500, fail_to_connect_server_text


def get_bind_id(id, type):
    data = {
        "id": id,
        "type": type
    }
    r = requests.get("http://hb-api.newitd.com/get_bind_id", data, timeout=30)
    if r.status_code == 200:
        json_result = r.text[5:-1]
        js_res = json.loads(json_result)
        if js_res["code"] != 1:
            return js_res["code"], js_res["info"]
        else:
            return js_res["code"], js_res["phone"]
    else:
        return -500, fail_to_connect_server_text


def bot_get_hongbao(id, type, url):
    code, phone = get_bind_id(id, type)
    if code != 1:
        return code, not_bind_id_text

    data = {
        "phone": phone,
        "url": url,
    }
    r = requests.get("http://hb-api.newitd.com/hongbao", data, timeout=30)
    if r.status_code == 200:
        json_result = r.text[5:-1]
        js_res = json.loads(json_result)
        return js_res["code"], js_res["info"]
    else:
        return -500, fail_to_connect_server_text


def get_log(phone):
    data = {
        "phone": phone,
        "limit": 20
    }
    r = requests.get("http://hb-api.newitd.com/get_user_log", data, timeout=30)
    if r.status_code == 200:
        json_result = r.text[5:-1]
        js_res = json.loads(json_result)
        return js_res["code"], js_res["res"]
    else:
        return -500, fail_to_connect_server_text


def format_log(res):
    str1 = "以下是你的点数日志\n"
    for log in res:
        if log[2] < 0:
            str1 += "增加"
        else:
            str1 += "消耗"
        str1 += str(log[2])
        str1 += "点---"
        str1 += log[4][5:]
        str1 += "\n"
    return str1
