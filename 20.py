import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


token = 'vk1.a.QF-D9_Sb82wyw-EbLD5wKDaLPg4QBg2ZLoSAPrKZgBYLzo6iDfxplNys3d9BKJKVzwfyATkzsoUJthTtz8oxtpAKck9g9YS6NAie5tOhoNrKIHuv5IfOjahwPEMSQvsAiKL4qRAKug27JV4PhSxNqaZRTn7tBoNYZBNfbOSpjeAc-eB-Pud1DMYIqL6Rwuzx'
mytoken = 'vk1.a.e6Wv7XYU47BrWBiycQuWdGLos04_IvlZwpMoRW3aubOgwJ9esnJaOF42bzi123JTGZX4MobsgU6hxarV_xNtU9OfsD089yqRiFize0So7ywfXfh-VVmTdNOEBbpRnF9LyV4ReI4biYgzbDTA8Lk3iOLTJvqgM6Ow80e6milRdL4mB8_ENxDjUq_86yVPBaN9'

vk = vk_api.VkApi(token=token)
#myvk = vk_api.VkApi(token=mytoken)

longpoll = VkLongPoll(vk)

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

def free_check():
    f1, f2, f3, f4 = 0, 0, 0, 0
    while f1 == 0 and f2 == 0 and f3 == 0 and f4 == 0:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                request = event.text
                if request == 'free1':
                    f1 = 1
                    break
                elif request == 'free2':
                    f2 = 1
                    break
                elif request == 'free3':
                    f3 = 1
                    break
                elif request == 'free4':
                    f4 = 1
                    break
    if f1 == 1:
        return 1
    elif f2 == 1:
        return 2
    elif f3 == 1:
        return 3
    elif f4 == 1:
        return 4

link1 = 'https://vk.com/call/join/RgM4UtRMeM7jwKIlhNGWb4w6mQwVeEKU_BFEzvhj6m6ZohHZ1RBMvAMODeOiB1k32nJY0goHGTZeo9emhP1QgJArZnXTbg9dxEDeCYUUAZk'
link2 = 'https://vk.com/call/join/d/yJvMW9X0_Q7_GPw5xmfa_SPRozKwLlDO2TUsLdD1JZ/h2LNf1ylNvm8FwnA2O_M57LySpplFelqjxqbY_3vHSSt4y6QYqBMJj/_kkOXaQ'
link3 = 'https://vk.com/call/join/A9AH9bjfNFuJDqa1AiXQGB6KCOyBNN_TljVyXTiL9EtNifecuMxHCoXvAEwWnzvi4L1HX5lwJMqkvmObBMzWYRmSNZOdqtq2OT0rWLoGmko'
link4 = 'https://vk.com/call/join/NXnCK8FePqcTT1VTMGueb/ayq9lEclDnvVcCmeaQuHxk3QXWOVtdnpW0MxM3_p663ygWRbxxS8N4dLXzt1AeKcf9mHmKOWvuJ6qsReC4pTE'

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text
        if request.lower() == 'call':
            oper = free_check()
            if oper == 1:
                write_msg(event.user_id, link1)
            elif oper == 2:
                write_msg(event.user_id, link2)
            elif oper == 3:
                write_msg(event.user_id, link3)
            elif oper == 4:
                write_msg(event.user_id, link4)

