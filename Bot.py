import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id
from threading import Thread # Многопоточность
import requests
import time
import random
import sys
sys.path.insert(0, "Commands")
sys.path.insert(0, "Data/Config")
sys.path.insert(0, "Data/Cmds")
import Help_script
import Joke_script
import connection
import Cmds_data as cmd
import Story_script as story
import Buttons_script as button
import Joke_script as Jokes
import Flip_script as flip
import Battle_script as battle
import Ball_script as ball
import Id_script
import Wiki_script as wiki
import Video_script as video
import Choose_script as choose
import Who_script as who
import Link_script as link
import Infa_script as infa
import Ed_script as ed
import Weather_script as weather
import Mem_script as mem
import Russian_roulette_script as rr

from Communication import Communication_script as answer
token=connection.token  #ТОКЕН ГРУППЫ
access_token = connection.access_token
group_id = connection.group_id
vk_session = VkApi(token = token)
vk_session2 = VkApi(token = access_token)
longpoll = VkBotLongPoll(vk_session, group_id)
longpollbot = True

def write_message(sender, message, send):
	if send == 1:
		vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message})
	elif send == 0:
		vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message})

def execute(event): #Выполнение команд в БЕСЕДЕ
	
	reseived_message = event.message.get("text")
	sender = event.chat_id
	send = 1

	if reseived_message.lower()[0] == "/":
		user = event.message.get("from_id")
		id_message = event.message.get("conversation_message_id")
		reseived_message_new = reseived_message.lower().split("/", 1)
		reseived_message = reseived_message_new[1]
		get_user = vk_session.method('users.get', {'user_ids': user, 'fields': "sex"})
		sex = get_user[0]["sex"]
		name = get_user[0]["first_name"]
		text = reseived_message.lower()

		if text in cmd.helps: #ВСЕ КОМАНДЫ
			Help_script.start(sender, send, name, user)

		elif text in cmd.story: #Жуткая история
			story.start(sender, send)

		elif text in cmd.joke: #Анекдот
			Jokes.start(sender, send)

		elif text[0:4] == "flip" or text[0:10] == "переверни": #Переверни
			flip.start(sender, send, reseived_message)

		elif text[0:2] == "vs": #В РАЗРАБОТКЕ
			battle.start(text, send, sender)

		elif text[0:3] == "шар": #ШАР
			ball.start(sender, send)

		elif text[0:2] == "id" or text[0:3] == "idc":
			Id_script.start(sender, text, send, name, user)

		elif text[0:4] == "вики" or text[0:4] == "wiki": #ВИКИПЕДИЯ
			wiki.start(sender, text, send)

		elif text[0:5] == "видео": #ВИДЕО
			video.start(sender, reseived_message, send)

		elif text[0:6] == "выбери": #ВЫБЕРИ
			choose.start(sender, text, send)

		elif text[0:3] == "кто" or text[0:6] == "список":
			who.start(sender, text, send)

		elif text[0:14] == "сократи ссылку" or text.lower()[0] == "s": #СОКРАЩЕННАЯ ССЫЛКА
			link.start(sender, text, send)

		elif text[0:11] == "вероятность" or text.lower()[0:4] == "инфа": #ВЕРОЯТНОСТЬ
			infa.start(sender, text, send)

		elif text[0:2] == "ed": #ИЗМЕНЕНИЕ НАЗВАНИЯ БЕСЕДЫ
			ed.start(sender, text, send)

		elif text[0:6] == "погода": #ПОГОДА
			weather.start(sender, text, send)

		elif text[0:3] == "мем": #МЕМ
			mem.start(sender, text, send)

		elif text[0:2] == "rr" or text[0:15] == "русская рулетка": #РУССКАЯ РУЛЕТКА
			rr.start(sender, text, send, user, id_message)

		else:
			answer.start(reseived_message, sender, send, sex)

	else: #ВЗАИМОДЕЙСТВИЕ С КНОПКАМИ
		if "Следующий мем😹" in reseived_message: #МЕМ
			mem.start(sender, reseived_message, send)

		else:
			button.start(sender, send, reseived_message)
	#except:
		#print("Ошибка!")

def execute2(event): #Выполнение команд в ЛС
	#try:
	reseived_message = event.message.get("text")
	sender = event.message.get("from_id")
	id_message = event.message.get("id")
	get_user = vk_session.method('users.get', {'user_ids': sender, 'fields': "sex"})
	sex = get_user[0]["sex"]
	name = get_user[0]["first_name"]
	send = 0

	if reseived_message.lower()[0] == "/":
		reseived_message_new = reseived_message.split("/", 1)
		reseived_message = reseived_message_new[1]

	if reseived_message.lower() in cmd.helps: #ВСЕ КОМАНДЫ
		Help_script.start(sender, send, name, sender)

	elif reseived_message.lower() in cmd.story or "Следующая история😱" in reseived_message: #Жуткая история
		story.start(sender, send)

	elif reseived_message.lower() in cmd.joke or "Следующий анекдот😂" in reseived_message: #Анекдот
		Jokes.start(sender, send)

	elif "Следующий мем😹" in reseived_message: #МЕМ
		mem.start(sender, reseived_message, send)

	elif reseived_message.lower()[0:4] == "flip" or reseived_message.lower()[0:10] == "переверни": #Переверни
		flip.start(sender, send, reseived_message)

	elif reseived_message.lower()[0:2] == "vs": #В РАЗРАБОТКЕ
		battle.start(reseived_message, send, sender)

	elif reseived_message.lower()[0:3] == "шар": #ШАР
		ball.start(sender, send)

	elif reseived_message.lower()[0:2] == "id" or reseived_message.lower()[0:3] == "idc":
		Id_script.start(sender, reseived_message, send, name, sender)

	elif reseived_message.lower()[0:4] == "вики" or reseived_message.lower()[0:4] == "wiki": #ВИКИПЕДИЯ
		wiki.start(sender, reseived_message, send)

	elif reseived_message.lower()[0:5] == "видео": #ВИДЕО
		video.start(sender, reseived_message, send)

	elif reseived_message.lower()[0:6] == "выбери": #ВЫБЕРИ
		choose.start(sender, reseived_message, send)

	elif reseived_message.lower()[0:3] == "кто" or reseived_message.lower()[0:6] == "список":
		who.start(sender, reseived_message, send)

	elif reseived_message.lower()[0:14] == "сократи ссылку" or reseived_message.lower()[0] == "s":  #СОКРАЩЕННАЯ ССЫЛКА
		link.start(sender, reseived_message, send)

	elif reseived_message.lower()[0:11] == "вероятность" or reseived_message.lower()[0:4] == "инфа": #ВЕРОЯТНОСТЬ
		infa.start(sender, reseived_message, send)

	elif reseived_message.lower()[0:2] == "ed": #ИЗМЕНЕНИЕ НАЗВАНИЯ БЕСЕДЫ
		ed.start(sender, reseived_message, send)

	elif reseived_message.lower()[0:6] == "погода": #ПОГОДА
		weather.start(sender, reseived_message, send)

	elif reseived_message.lower()[0:3] == "мем": #МЕМ
		mem.start(sender, reseived_message, send)

	elif reseived_message.lower()[0:2] == "rr" or reseived_message.lower()[0:15] == "русская рулетка": #РУССКАЯ РУЛЕТКА
		rr.start(sender, reseived_message, send, sender, id_message)


	else:
		answer.start(reseived_message, sender, send, sex)
	#except:
		#print("Ошибка!")
		
while longpollbot:
	try:
		status = vk_session.method('groups.getOnlineStatus', {'group_id': group_id})
		if not status['status'] == "online":
			vk_session.method('groups.enableOnline', {'group_id': group_id})
		for event in longpoll.listen():
			try:
			    if event.type == VkBotEventType.MESSAGE_NEW: #Кто-то отправил боту сообщение
			    	if event.from_chat and event.message and event.message.get('text'):  #ЕСЛИ НАПИСАЛИ В ЧАТЕ
			    		Thread(target = execute, args = (event, ), daemon = True).start()

			    	elif event.from_user and event.message and event.message.get('text'):   #ЕСЛИ НАПИСАЛИ В ЛС
			    		Thread(target = execute2, args = (event, ), daemon = True).start()

			    elif event.type == VkBotEventType.GROUP_JOIN: #Если пользователь вступил в группу
			    	sender = event.object.user_id
			    	send = 0
			    	get_user = vk_session.method('users.get', {'user_ids': sender, 'fields': "sex"})
			    	sex = get_user[0]["sex"]
			    	name = get_user[0]["first_name"]
			    	if sex == 2:
			    		message = "👋Привет! Я рад, что ты вступил в группу!😄"
			    	else:
			    		message = "👋Привет! Я рад, что ты вступила в группу!😄"
			    	write_message(sender, message, send)
			    	Help_script.start(sender, send, name, sender)
			except:
				print("Ошибка!")

			    

	except requests.exceptions.ReadTimeout:
		print("\n Переподключение к серверам ВК \n")
		time.sleep(3)