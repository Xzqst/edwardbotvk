# -*- coding: utf-8 -*-
#ПУШКА

import vk_api

import os
import time

import requests

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id



def write_message(sender, message): #ОТПРАВКА СООБЩЕНИЯ В БЕСЕДУ
	vk_session.method('messages.send', {'chat_id': sender, 'message': message, 'random_id': get_random_id()})

def write_message2(sender, message): #ОТПРАВКА СООБЩЕНИЯ В ЛС
	vk_session.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})

token="b2404bfb9a2e571486737e966f628e5faef38be2a82f763e9398ec6563db0aa5a64097133e1ec6bcef3b9"  #ТОКЕН ГРУППЫ

vk_session = VkApi(token = token)

longpoll = VkBotLongPoll(vk_session, 200012156)

longpollbot = True


strike = '''
Вас атакуют!
'''

strike1 = '''
Вас атакуют!
'''

strike3 = '''
Вас атакуют!
'''

commands = '''
📋КОМАНДЫ📋

—📋 /help - открыть все команды. 

🖥ПАНЕЛЬ УПРАВЛЕНИЯ

—✅ /вкл - включить оружие.
—🔌 /выкл - выключить оружие.
—🆔 /id - узнать свой айди.
—🆔 /idc - узнать айди беседы.
—🔄 /restart - перезапустить оружие.
—🚀 /strike [айди пользователя] - нанести удар по пользователю!
—💣 /bomb - начать спам атаку в беседе.

⚙НАСТРОЙКИ⚙

—📝 /r [текст] - изменить сообщение, отправляемое ботом.

'''

onoff = False




while longpollbot:

	try:

	


		for event in longpoll.listen():


		    if event.type == VkBotEventType.MESSAGE_NEW:

		    	if event.from_chat and event.message and event.message.get('text'):  #ЕСЛИ НАПИСАЛИ В ЧАТЕ

		    		reseived_message = event.message.get("text")
		    		sender = event.chat_id


		    		if reseived_message.lower() == "/вкл":
		    			onoff = True
		    			write_message(sender, "✅Орудие включено!")

		    		

		    		elif reseived_message.lower() == "/выкл":
		    			onoff = False
		    			write_message(sender, "❗Оружие выключено!")



		    		elif reseived_message.lower() == "/id":
		    			iduser = event.message.get("from_id")
		    			user = vk_session.method("users.get", {"user_ids": iduser})
		    			name = user[0]['first_name']
		    			write_message(sender, "⌛Подождите...")
		    			iduser = name + ", " + " ваш 🆔: " + str(iduser)
		    			write_message(sender, iduser)

		    		elif reseived_message.lower() == "/idc":
		    			idc = "🆔: " + str(sender)
		    			write_message(sender, idc)


		    		elif "/strike " in reseived_message.lower() and onoff == True:

		    			try:

			    			reseived_message_new = reseived_message.lower().split(" ", 1)
			    			index = reseived_message_new[1]
			    			fire = 0

			    			write_message(sender, "Идет зарядка!")
			    			write_message(sender, "⚡Зарядка... [██████      ] 50%")
			    			write_message(sender, "⚡Зарядка... [█████████   ] 80%")
			    			write_message(sender, "⚡Зарядка... [███████████ ] 99%")
			    			write_message(sender, "⚡Зарядка... [████████████] 100%")
			    			write_message(sender, "✅Орудие заряжено!")
			    			write_message(sender, "🔥Огонь!")
			    			strike = strike1



			    			while fire <= 100:

			    				fire = fire + 10
			    				write_message2(index, strike)
			    				
			    			

			    		except:

			    			fire = 0
			    			write_message(sender, "⚠Орудие разряжено!")
			    			write_message(sender, "🎯Цель не поражена.")

			    		else:

			    			write_message(sender, "⚠Орудие разряжено!")
			    			write_message(sender, "🎯Цель поражена.")
			    			fire = 0


		    		elif "/strike " in reseived_message.lower() and onoff == False:
		    			write_message(sender, "⚠Орудие выключено.")



		    		elif reseived_message.lower() == "/help":
		    			write_message(sender, commands)

		    		elif reseived_message.lower() == "/bomb" and onoff == True:

		    			try:

			    			fire = 0
			    			write_message(sender, "Идет зарядка!")
			    			write_message(sender, "⚡Зарядка... [██████      ] 50%")
			    			write_message(sender, "⚡Зарядка... [█████████   ] 80%")
			    			write_message(sender, "⚡Зарядка... [███████████ ] 99%")
			    			write_message(sender, "⚡Зарядка... [████████████] 100%")
			    			write_message(sender, "✅Бомба готова к взрыву!")
			    			write_message(sender, "💣Взрыв!")
			    			strike = strike1


			    			while fire <= 100:
			    				write_message(sender, strike)
			    				fire = fire + 1

			    		except:

			    			print("Воникло исключение. Бот был исключен из беседы.")

			    		else:

			    			write_message(sender, "⚠Орудие разряжено!")
			    			write_message(sender, "🎯Цель поражена.")
			    			fire = 0

		    		elif reseived_message.lower() == "/bomb" and onoff == False:
		    			write_message(sender, "⚠Орудие выключено.")

		    		elif reseived_message.lower() == "/restart":
		    			strike = strike3
		    			write_message(sender, "✅Бот перезапущен.")
		    			os.system('python "restart.py"')
		    			time.sleep(1)
		    			exit()

		    		elif "/r " in reseived_message.lower():
		    			reseived_message_new = reseived_message.lower().split(" ", 1)
		    			index = reseived_message_new[1]
		    			strike1 = index
		    			write_message(sender, "✅Текст сообщения успешно изменен!")











		    				



		    	elif event.from_user and event.message and event.message.get('text'):   #ЕСЛИ НАПИСАЛИ В ЛС

		    		reseived_message = event.message.get("text")
		    		sender = event.message.get("from_id")

		    		if reseived_message.lower() == "/вкл":
		    			onoff = True
		    			write_message2(sender, "✅Орудие включено!")

		    		elif reseived_message.lower() == "/выкл":
		    			onoff = False
		    			write_message2(sender, "❗Оружие выключено!")


		    		elif reseived_message.lower() == "/id":
		    			iduser = event.message.get("from_id")
		    			user = vk_session.method("users.get", {"user_ids": iduser})
		    			name = user[0]['first_name']
		    			write_message2(sender, "⌛Подождите...")
		    			iduser = name + ", " + " ваш 🆔: " + str(iduser)
		    			write_message2(sender, iduser)

		    		elif reseived_message.lower() == "/idc":
		    			write_message2(sender, "⚠Эта команда работает только в беседе.")


		    		elif "/strike " in reseived_message.lower() and onoff == True:

		    			try:

			    			reseived_message_new = reseived_message.lower().split(" ", 1)
			    			index = reseived_message_new[1]
			    			fire = 0

			    			write_message2(sender, "Идет зарядка!")
			    			write_message2(sender, "⚡Зарядка... [██████      ] 50%")
			    			write_message2(sender, "⚡Зарядка... [█████████   ] 80%")
			    			write_message2(sender, "⚡Зарядка... [███████████ ] 99%")
			    			write_message2(sender, "⚡Зарядка... [████████████] 100%")
			    			write_message2(sender, "✅Орудие заряжено!")
			    			write_message2(sender, "🔥Огонь!")
			    			strike = strike1

			    			while fire <= 100:

			    				fire = fire + 10
			    				write_message2(index, strike)

			    		except:

			    			fire = 0
			    			write_message2(sender, "⚠Орудие разряжено!")
			    			write_message2(sender, "🎯Цель не поражена.")

			    		else:

			    			write_message(sender, "⚠Орудие разряжено!")
			    			write_message(sender, "🎯Цель поражена.")
			    			fire = 0

		    		elif "/strike " in reseived_message.lower() and onoff == False:
		    			write_message2(sender, "⚠Орудие выключено.")



		    		elif reseived_message.lower() == "/help":
		    			write_message2(sender, commands)

		    		elif reseived_message.lower() == "/bomb" and onoff == True:

		    			write_message2(sender, "⚠Эта команда работает только в беседе!")

		    		elif reseived_message.lower() == "/bomb" and onoff == False:
		    			write_message2(sender, "⚠Орудие выключено.")

		    		elif reseived_message.lower() == "/restart":
		    			strike = strike3
		    			write_message2(sender, "✅Бот перезапущен.")
		    			os.system('python "restart.py"')
		    			time.sleep(1)
		    			exit()

		    		elif "/r " in reseived_message.lower():
		    			reseived_message_new = reseived_message.lower().split(" ", 1)
		    			index = reseived_message_new[1]
		    			strike1 = index
		    			write_message2(sender, "✅Текст сообщения успешно изменен!")

	except requests.exceptions.ReadTimeout:

		print("\n Переподключение к серверам ВК \n")
		time.sleep(3)


	
				






		



		
		


		    		

	
		

	
