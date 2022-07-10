import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time
from time import sleep

mas = []

mytoken = 'vk1.a.e6Wv7XYU47BrWBiycQuWdGLos04_IvlZwpMoRW3aubOgwJ9esnJaOF42bzi123JTGZX4MobsgU6hxarV_xNtU9OfsD089yqRiFize0So7ywfXfh-VVmTdNOEBbpRnF9LyV4ReI4biYgzbDTA8Lk3iOLTJvqgM6Ow80e6milRdL4mB8_ENxDjUq_86yVPBaN9'
token = 'vk1.a.QF-D9_Sb82wyw-EbLD5wKDaLPg4QBg2ZLoSAPrKZgBYLzo6iDfxplNys3d9BKJKVzwfyATkzsoUJthTtz8oxtpAKck9g9YS6NAie5tOhoNrKIHuv5IfOjahwPEMSQvsAiKL4qRAKug27JV4PhSxNqaZRTn7tBoNYZBNfbOSpjeAc-eB-Pud1DMYIqL6Rwuzx'
vk = vk_api.VkApi(token=mytoken)



while True:
    resp = vk.method('video.get', {'access_token': mytoken, 'owner_id': -214437613})
    #print(resp)
    if resp['items'] != []:
        if id = resp['items'][0]['type'] == 'live':
            id = resp['items'][0]['id']
            if id not in mas:
                mas.append(id)
                print('Новый стрим! Название:' + resp['items'][0]['title'] + '. Ссылка: ' + resp['items'][0]['player'])
        sleep(60)




