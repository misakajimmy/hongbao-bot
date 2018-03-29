from qqbot import QQBotSlot as qqbotslot, RunBot
from qqbot import _bot as bot
from function import *


@qqbotslot
def onQQMessage(bot, contact, member, content):
    if not bot.isMe(contact, member):
        if contact.ctype == "buddy":
            if "帮助" in content:
                bot.SendTo(contact, help_text)
                return
            phone = check_phone(content)
            url = change_url(content)
            if "查询" in content:
                if not phone:
                    code, res = get_bind_id(contact.uin, 1)
                    if code != 1:
                        bot.SendTo(contact, not_bind_id_text)
                        return
                    else:
                        phone = res
                code, res = points_back(phone)
                bot.SendTo(contact, res)
                return
            if "日志"in content:
                if phone:
                    logs_str_back="以下是你的点数日志\n"
                    logs_detail,logs_changedate=get_log(phone)
                    for times in logs_detail:
                        logs_str_back+=str(logs_detail[times])+"  于日期"+str(logs_changedate[times])+"\n"
                    bot.SendTo(contact,logs_str_back)
                    
                else :
                    bot.SendTo(contact,log_error_text)
                return
            if phone:
                code, res = take_bind_id(phone, contact.uin, 1)
                bot.SendTo(contact, res)
                return
            if url and url not in "newitd":
                url = check_url(url)
                if url:
                    bot.SendTo(contact, doing_hongbao_text)
                    code, res = bot_get_hongbao(contact.uin, 1, url)
                    bot.SendTo(contact, res)
                else:
                    bot.SendTo(contact, share_error_url_text)
                return
        elif contact.ctype == "group":
            phone = check_phone(content)
            url = change_url(content)
            if "查询" in content:
                if not phone:
                    code, res = get_bind_id(member.uin, 1)
                    if code != 1:
                        bot.SendTo(contact, member.name + "：" + res)
                        return
                    else:
                        phone = res
                code, res = points_back(phone)
                bot.SendTo(contact, member.name + "：" + res)
                return
            if phone:
                code, res = take_bind_id(phone, member.uin, 1)
                bot.SendTo(contact, member.name + "：" + res)
                return
            if url and url not in "newitd":
                url = check_url(url)
                if url:
                    bot.SendTo(contact, member.name + "：" + doing_hongbao_text)
                    code, res = bot_get_hongbao(member.uin, 1, url)
                    bot.SendTo(contact, member.name + "：" + res)
                else:
                    bot.SendTo(contact, member.name + "：" + share_error_url_text)
                return


if __name__ == "__main__":
    # 生产环境
    # RunBot()

    # 测试环境
    bot.Login(["-q", "2390225401"])
    bot.Run()
