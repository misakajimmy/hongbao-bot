from wxpy import *
from function import *
from function import *

bot = Bot(cache_path=True)
bot.enable_puid()


@bot.register(Friend)
def receive_msg(msg):
    print(msg)
    user = msg.chat
    if not user.is_friend():
        # 接受好友请求
        user.accept()
        # 向新的好友发送消息
        user.send(welcome_text)
        return
    if "帮助" in msg.text:
        user.send(help_text)
    elif msg.type == "Text":
        if "绑定" in msg.text:
            # 绑定手机号
            phone = check_phone(msg.text[2:])
            if not phone:
                user.send(error_phone)
                return
            else:
                code, res = bind_id(phone, user.puid, 2)
                user.send(res)
        else:
            url = change_url(msg.text)
            if not url:
                user.send(error_url)
                return
            url = check_url(url)
            if url:
                code, res = bot_get_hongbao(user.puid, 2, url)
                user.send(res)
            else:
                user.send(get_help_text)
    elif msg.type == "Sharing":
        url = check_url(msg.url)
        if url:
            code, res = bot_get_hongbao(user.puid, 2, url)
            user.send(res)
        else:
            user.send(share_error_url)
    else:
        user.send(no_support_type)


embed()
