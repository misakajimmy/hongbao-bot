from qqbot import QQBotSlot as qqbotslot, RunBot
from qqbot import _bot as bot
from function import *


@qqbotslot
def onQQMessage(bot, contact, member, content):
    if not bot.isMe(contact, member) and contact.ctype == "buddy":
        if "帮助" in content:
            bot.SendTo(contact, help_text)
        phone = check_phone(content)
        url = change_url(content)
        cphone = check_points(content)
        if "查询" in content:
            try:
                pointsres = points_back(cphone)
                bot.SendTo(contact, pointsres)
            except:
                bot.SendTo(contact, check_point_error_text)

        if phone and not "查询" in content:
            code, res = take_bind_id(phone, contact.uin, 1)
            bot.SendTo(contact, res)
        if url:
            url = check_url(url)
            if url:
                bot.SendTo(contact, doing_hongbao_text)
                code, res = bot_get_hongbao(contact.uin, 1, url)
                bot.SendTo(contact, res)
            else:
                bot.SendTo(contact, share_error_url_text)
    elif not bot.isMe(contact, member) and contact.ctype == "group":
        phone = check_phone(content)
        url = change_url(content)
        cphone = check_points(content)
        if "查询" in content and cphone:
            try:
                pointsres = points_back(cphone)
                bot.SendTo(contact, pointsres)
            except:
                bot.SendTo(contact, check_point_error_text)

        if phone and not "查询" in content:
            code, res = take_bind_id(phone, contact.uin, 1)
            bot.SendTo(contact, res)
        if url:
            url = check_url(url)
            if url:
                bot.SendTo(contact, member.name + "：" + doing_hongbao_text)
                code, res = bot_get_hongbao(member.uin, 1, url)
                bot.SendTo(contact, member.name + "：" + res)
            else:
                bot.SendTo(contact, member.name + ":" + share_error_url_text)


# 生产环境
# RunBot()

# 测试环境
bot.Login(["-q", "2390225401"])
bot.Run()
