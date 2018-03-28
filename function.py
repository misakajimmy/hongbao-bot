import pymysql
import requests
import json
import re
from config import *
from text_config import *


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


def bind_id(phone, id, type):
    # 建立数据库连接
    try:
        db = pymysql.connect(db_host, db_user, db_password, db_database, charset="utf8")
        cursor = db.cursor()
    except:
        return -1, fail_to_connect_mysql_text
    if type == 1:
        sql = "SELECT phone FROM bot WHERE qqid=%s"
    else:
        sql = "SELECT phone FROM bot WHERE wxid=%s"
    cursor.execute(sql, id)
    result = cursor.fetchall()
    if not result:
        if type == 1:
            sql = "INSERT INTO bot(qqid, phone) VALUES (%s,%s)"
        else:
            sql = "INSERT INTO bot(wxid, phone) VALUES (%s,%s)"
        cursor.execute(sql, (id, phone))
        db.commit()
        return 1, success_insert_bind
    else:
        if type == 1:
            sql = "UPDATE bot SET phone=%s WHERE qqid=%s"
        else:
            sql = "UPDATE bot SET phone=%s WHERE wxid=%s"
        cursor.execute(sql, (phone, id))
        db.commit()
        return 2, success_update_bind


def bot_get_hongbao(id, type, url):
    # 建立数据库连接
    try:
        db = pymysql.connect(db_host, db_user, db_password, db_database, charset="utf8")
        cursor = db.cursor()
    except:
        return -1, "连接数据库失败！请联系管理员！"
    if type == 1:
        sql = "SELECT phone FROM bot WHERE qqid=%s"
    else:
        sql = "SELECT phone FROM bot WHERE wxid=%s"
    cursor.execute(sql, id)
    result = cursor.fetchall()
    if result:
        phone = result[0][0]
        data = {
            "phone": phone,
            "url": url,
        }
        result = requests.get("http://hb-api.newitd.com/hongbao", data, timeout=30)
        if result.status_code == 200:
            json_result = result.text[5:-1]
            js_res = json.loads(json_result)
            return 1, js_res['info']
        else:
            return -2, "服务器出错，请联系管理员！"
    else:
        return -3, "未绑定手机，请输入手机号绑定！"

