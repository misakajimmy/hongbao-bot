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
            if not phone:
                phone = get_phone(contact.uin)
            else:
                code, res = take_bind_id(phone, contact.uin, 1)
                bot.SendTo(contact, res)
                return
            url = change_url(content)
            if "查询" in content:
                if not phone:
                    bot.SendTo(contact, not_bind_id_text)
                    return
                code, res = points_back(phone)
                bot.SendTo(contact, res)
                return
            # if "日志" in content:
            #     if not phone:
            #         bot.SendTo(contact, not_bind_id_text)
            #         return
            #     code, res = get_log(phone)
            #     if code != 1:
            #         bot.SendTo(contact, res)
            #         return
            #     str = format_log(res, phone)
            #     bot.SendTo(contact, str)
            #     return
            # if "记录" in content:
            #     if not phone:
            #         bot.SendTo(contact, not_bind_id_text)
            #         return
            #     code, res = get_task(phone)
            #     if code != 1:
            #         bot.SendTo(contact, res)
            #         return
            #     str = format_task(res, phone)
            #     bot.SendTo(contact, str)
            #     return
            if url and "newitd" not in url:
                if not phone:
                    bot.SendTo(contact, not_bind_id_text)
                    return
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
            if not phone:
                phone = get_phone(contact.uin)
            else:
                code, res = take_bind_id(phone, contact.uin, 1)
                bot.SendTo(contact, res)
                return
            url = change_url(content)
            if "查询" in content:
                if not phone:
                    bot.SendTo(contact, member.name + "：" + not_bind_id_text)
                    return
                code, res = points_back(phone)
                bot.SendTo(contact, member.name + "：" + res)
                return
            # if "日志" in content:
            #     if not phone:
            #         bot.SendTo(contact, member.name + "：" + not_bind_id_text)
            #         return
            #     code, res = get_log(phone)
            #     if code != 1:
            #         bot.SendTo(contact, member.name + "：" + res)
            #         return
            #     str = format_log(res, phone)
            #     bot.SendTo(contact, member.name + "：" + str)
            #     return
            # if "记录" in content:
            #     if not phone:
            #         bot.SendTo(contact, member.name + "：" + not_bind_id_text)
            #         return
            #     code, res = get_task(phone)
            #     if code != 1:
            #         bot.SendTo(contact, member.name + "：" + res)
            #         return
            #     str = format_task(res, phone)
            #     bot.SendTo(contact, member.name + "：" + str)
            #     return
            if url and "newitd" not in url:
                if not phone:
                    bot.SendTo(contact, member.name + "：" + not_bind_id_text)
                    return
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
    bot.Login(["-q", "2594623198"])
    bot.Run()
