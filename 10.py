import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

token = 'vk1.a.QF-D9_Sb82wyw-EbLD5wKDaLPg4QBg2ZLoSAPrKZgBYLzo6iDfxplNys3d9BKJKVzwfyATkzsoUJthTtz8oxtpAKck9g9YS6NAie5tOhoNrKIHuv5IfOjahwPEMSQvsAiKL4qRAKug27JV4PhSxNqaZRTn7tBoNYZBNfbOSpjeAc-eB-Pud1DMYIqL6Rwuzx'
mytoken = 'vk1.a.e6Wv7XYU47BrWBiycQuWdGLos04_IvlZwpMoRW3aubOgwJ9esnJaOF42bzi123JTGZX4MobsgU6hxarV_xNtU9OfsD089yqRiFize0So7ywfXfh-VVmTdNOEBbpRnF9LyV4ReI4biYgzbDTA8Lk3iOLTJvqgM6Ow80e6milRdL4mB8_ENxDjUq_86yVPBaN9'

vk = vk_api.VkApi(token=token)
myvk = vk_api.VkApi(token=mytoken)

longpoll = VkLongPoll(vk)

def call(token):
    resp = myvk.method('messages.startCall')
    return resp['join_link']

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text
        if request.lower() == 'звонок':
            a = call(mytoken)
            write_msg(event.user_id, a)
        else:
            write_msg(event.user_id, 'я тебя не понял(')



