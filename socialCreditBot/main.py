import random, vk_api, vk
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import pymysql.cursors

import requests

from connection import sqlconnect
from config import main_token

vk_session = vk_api.VkApi(token = main_token)
longpoll = VkBotLongPoll(vk_session, "207410256")
vk = vk_session.get_api()

def get_test_message(command):
        with sqlconnect.cursor() as cursor:
                sqlsearch = "SELECT * FROM test_sht"
                cursor.execute(sqlsearch)
                sqlresult = cursor.fetchall()
                id_list = []
                for test_row in sqlresult:
                        id_list.append(str(test_row['shit_id']))
                print(id_list)
                if id_list.count(command[1])==1:
                        sqlsearch = "SELECT * FROM test_sht WHERE shit_id = "+command[1]
                        cursor.execute(sqlsearch)
                        sqlresult = cursor.fetchall()
                        msg = "Ваше тестовое сообщение: "+sqlresult[0]['text']
                        vk.messages.send(
                                user_id=event.obj.from_id,
                                random_id=get_random_id(),
                                message=msg,
                                chat_id = event.chat_id)
                else:
                        vk.messages.send(
                                user_id=event.obj.from_id,
                                random_id=get_random_id(),
                                message='Иди нахуй!',
                                chat_id = event.chat_id)

for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.message['text'].startswith('!'):
                        getted_command = str(event.object.message['text']).split(' ')
                        print(getted_command) 
                        if getted_command[0]=='!test_command' and getted_command[1].isdigit() and len(getted_command)==2:
                                get_test_message(getted_command)
                        elif getted_command[0]=='!help' and len(getted_command)==1:
                                vk.messages.send(
                                        user_id=event.obj.from_id,
                                        random_id=get_random_id(),
                                        message='Нет!',
                                        chat_id = event.chat_id)
