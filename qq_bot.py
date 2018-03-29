from qqbot import QQBotSlot as qqbotslot, RunBot
from qqbot import _bot as bot
from function import *
import requests

@qqbotslot
def onQQMessage(bot, contact, member, content):
    if not bot.isMe(contact, member) and contact.ctype == "buddy":
        if "帮助" in content:
            bot.SendTo(contact, help_text)
        phone = check_phone(content)
        url = change_url(content)
        cphone=check_points(content)
        if "查询" in content and cphone:
            data = {
            "phone": cphone,
            "url": ""
            }
            r =requests.get("http://hb-api.newitd.com/user_info",data,timeout=30)
            if r.status_code == 200:
                json_result = r.text[5:-1]
                js_res = json.loads(json_result)
                bot.SendTo(contact,js_res["info"])
            else:
                bot.SendTo(contact,"fail to check points")
        if phone and not"查询" in content:
            code, res = bind_id(phone, contact.uin, 1)
            bot.SendTo(contact, res)
        if url:
            url = check_url(url)
            if url:
                bot.SendTo(contact, doing_hongbao)
                code, res = bot_get_hongbao(contact.uin, 1, url)
                bot.SendTo(contact, res)
            else:
                bot.SendTo(contact, share_error_url)
    elif not bot.isMe(contact, member) and contact.ctype == "group":
        phone = check_phone(content)
        url = change_url(content)
        cphone=check_points(content)
        if "查询" in content and cphone:
            data = {
            "phone": cphone,
            "url": ""
            }
            r =requests.get("http://hb-api.newitd.com/user_info",data,timeout=30)
            if r.status_code == 200:
                json_result = r.text[5:-1]
                js_res = json.loads(json_result)
                bot.SendTo(contact,js_res["info"])
            else:
                bot.SendTo(contact,"fail to check points")
        if phone and not"查询" in content:
            code, res = bind_id(phone, contact.uin, 1)
            bot.SendTo(contact, res)
        if url:
            url = check_url(url)
            if url:
                bot.SendTo(contact, member.name + "：" + doing_hongbao)
                code, res = bot_get_hongbao(member.uin, 1, url)
                bot.SendTo(contact, member.name + "：" + res)
            else:
                bot.SendTo(contact, member.name + ":" + share_error_url)


# 生产环境
# RunBot()

# 测试环境
bot.Login(["-q","2390225401"])
bot.Run()
