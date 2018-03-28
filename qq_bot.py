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
        if phone:
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
        if phone:
            code, res = bind_id(phone, member.uin, 1)
            bot.SendTo(contact, member.name + "：" + res)
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
bot.Login(['-q', '2594623198', '-u', 'somebody'])
bot.Run()
