# -*- coding: utf8 -*-
#Бот Едвард
import vk_api
import random
import os
import time
import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import wikipedia
import pyshorteners #СОКРАЩЕННАЯ ССЫЛКА

import Phrases
from Data import Buttons
from Story import History
from translate import Translator
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor #КЛАВИАТУРА

from Data import commands, Fight
from Games import Balance_script
from GIF import Gif_script
from Covid_19 import Covid
from Video import Video_script

def write_message(sender, message): #ОТПРАВКА СООБЩЕНИЯ В БЕСЕДУ
	vk_session.method('messages.send', {'chat_id': sender, 'message': message, 'random_id': get_random_id()})

def write_message2(sender, message): #ОТПРАВКА СООБЩЕНИЯ В ЛС
	vk_session.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})

def edit_chat(ids, title): #ИЗМЕНЕНИЕ НАЗВАНИЯ БЕСЕДЫ
	vk_session.method('messages.editChat', {'chat_id': ids, 'title': title})


def write_button(sender, message): #ОТПРАВКА КЛАВИАТУРЫ
	vk_session.method('messages.send', {'chat_id': sender, 'message': message, 'random_id': get_random_id(), 'keyboard': keyboard.get_keyboard()})

def write_button2(sender, message): #ОТПРАВКА КЛАВИАТУРЫ
	vk_session.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'keyboard': keyboard.get_keyboard()})

def edit_message(sender, message, message_id): #Редактирование сообщения в лс.
	vk_session.method('messages.edit', {'peer_id': sender, 'message': message, 'message_id': message_id})

def post(text):
	vk_session2.method('wall.post', {'owner_id': -197481314, 'message': text})

def write_video(sender, video, message):
	vk_session.method('messages.send', {'user_id': sender, 'message': "🔎Найдено видео по запросу: " + "\"" + message + "\"", 'attachment': video, 'random_id': get_random_id()})

def write_photo2(sender):
	try:
		a = vk_session2.method('wall.get', {'owner_id': -197481314})
		a = a['items']
		r = random.choice(a)
		r = r['attachments'][0]['photo']
		r1 = r['id']
		r2 = r['owner_id']
		photo = "photo" + str(r2) + "_" + str(r1)
		vk_session.method('messages.send', {'user_id': sender, 'message': "Вот вам мем из нашей группы", 'attachment': photo, 'random_id': get_random_id()})
	except:
		write_message2(sender, "⚠Ошибка")

def write_video2(sender, video, message):
	vk_session.method('messages.send', {'chat_id': sender, 'message': "🔎Найдено видео по запросу: " + "\"" + message + "\"", 'attachment': video, 'random_id': get_random_id()})

token="f4a8b4fc8fe0aa8e080fc21186f5606bd26e26f6429715472af9e201254862bf07c4cec92858e0d40558a"  #ТОКЕН ГРУППЫ
access_token = "914ae14206f01f8adaab0ea90b87b6199d09d8aac4ca4075e99e6aed7742ede4328ea6187ad5bb64011e4"
vk_session = VkApi(token = token)
vk_session2 = VkApi(token = access_token)
longpoll = VkBotLongPoll(vk_session, 197481314)
longpollbot = True

#ПОГОДА
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('1ad03b7000a938a954739c5d5d77e6f2', config_dict)

mgr =  owm.weather_manager() #ПОГОДА

while longpollbot:
	try:
		status = vk_session.method('groups.getOnlineStatus', {'group_id': 197481314})
		if not status['status'] == "online":
			vk_session.method('groups.enableOnline', {'group_id': 197481314})

		for event in longpoll.listen():
		    if event.type == VkBotEventType.MESSAGE_NEW:
		    	if event.from_chat and event.message and event.message.get('text'):  #ЕСЛИ НАПИСАЛИ В ЧАТЕ
		    		reseived_message = event.message.get("text")
		    		sender = event.chat_id
		    		
		    		if "следующий анекдот😂" in reseived_message.lower():
	    				f = open('Data/joke.txt', 'r+')
		    			a = f.readlines()
		    			joke = random.choice(a)
		    			keyboard = Buttons.keyboard_joke
		    			write_button(sender, joke)
		    			f.close()

		    		elif "следующая история😱" in reseived_message.lower():
	    				story = random.choice(History.history_list_bot)
	    				keyboard = Buttons.keyboard_history
	    				write_button(sender, story)

	    			elif "следующая цитата📕" in reseived_message.lower():
    					CITAT = 'https://citatnica.ru/citaty/samye-luchshie-tsitaty'
	    				headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
	    				full_page = requests.get(CITAT, headers=headers)
	    				soup = BeautifulSoup(full_page.content, 'html.parser')
	    				convertd = soup.findAll("div", {"class": "su-note"})
	    				a = random.choice(convertd)
	    				a = a.text
	    				keyboard = Buttons.keyboard_citat
	    				write_button(sender, a)

	    			elif "/ответ " in reseived_message.lower(): #ОТВЕТ
	    				try:
			    			a = reseived_message.lower().split()
			    			iduser = a[1]
			    			text = a[2]
			    			message = "✉Вам пришло сообщение от администрации." + '\n' + "📜Текст сообщения:" + '\n' + text
			    			write_message2(int(iduser), message)
			    			write_message(sender, "✅Ваше сообщение успешно доставлено пользователю.")
			    		except:
			    			write_message(sender, "⚠Ошибка!")

		    		elif reseived_message.lower() == "/ответ":
			    		write_message(sender, "⚠Введите команду /ответ [айди] [текст сообщения]")

			    	elif "/репорт " in reseived_message.lower() or "/report " in reseived_message.lower(): #РЕПОРТ
		    			try:
			    			user = vk_session.method("users.get", {"user_ids": sender})
			    			name = user[0]['first_name'] #ПОЛУЧЕНИЕ ИМЕНИ ПОЛЬЗОВАТЕЛЯ
			    			name2 = user[0]['last_name'] #ПОЛУЧЕНИЕ ФАМИЛИИ ПОЛЬЗОВАТЕЛЯ
			    			a = reseived_message.lower().split(" ", 1)
			    			text = a[1]
			    			message1 = '\n' + "📫Пользователь отправил сообщение в тех.поддержку!" + '\n'
			    			
			    			message2 = '\n' + "🆔Id отправителя: " + str(sender)
			    			message3 = '\n' + "👤Имя и фамилия отправителя: " + name + " " + name2
			    			message4 = '\n' + "✉Текст сообщения: " + '\n'+ '\n' + text + '\n' + '\n'
			    			message5 = "Введите команду /ответ [айди] [текст сообщения]"
			    			message = message1 + message2 + message3 + message4 + message5
			    			vk_session.method('messages.send', {'peer_id': 2000000000 + 23, 'message': message, 'random_id': get_random_id()})
			    			write_message(sender, "✅Ваше сообщение успешно доставлено администрации!")
			    		except:
			    			write_message(sender, "⚠Ошибка!")	
			    		

		    		elif reseived_message.lower() == "/репорт" or reseived_message.lower() == "/report": #ПРОВЕРИТЬ!!!!!!!!!!!!!!!!!!!!!!
		    			write_message2(sender, "⚠Введите команду /репорт [сообщение]")

		    		#КОМАНДЫ МОЖНО ПИСАТЬ, БЕЗ ОБРАЩЕНИЯ К БОТУ

		    		elif "/" in reseived_message.lower()[0]:
		    			reseived_message_new = reseived_message.lower().split("/", 1)
		    			index = reseived_message_new[1]

			    		if index == "help!":
			    			write_message(sender, commands.help_list_bot2)

			    		elif index in commands.id_list: #КОМАНДА АЙДИ
			    			iduser = event.message.get("from_id")
			    			user = vk_session.method("users.get", {"user_ids": iduser})
			    			name = user[0]['first_name']
			    			write_message(sender, "⌛Подождите...")
			    			iduser = name + ", " + " ваш 🆔: " + str(iduser)
			    			write_message(sender, iduser)

			    		elif index == "covid" or index == "коронавирус" or index == "covid19" or index == "ковид": #КОРОНАВИРУС
			    			write_message(sender, "⚠Подождите...")
			    			try:
			    				Covid.covid()
			    			except:
			    				write_message(sender, "⚠Не удалось получить информацию.")
			    			else:
			    				write_message(sender, Covid.message[0])
			    						
			    		


			    		elif index in commands.help_list_user: #список команд
			    			write_message(sender, commands.help_list_bot)

			    		elif index in commands.joke_list_user: #АНЕКДОТ
			    			f = open('joke.txt', 'r+')
			    			a = f.readlines()
			    			joke = random.choice(a)
			    			keyboard = Buttons.keyboard_joke
		    				write_button(sender, joke)
			    			f.close()

		    			elif index in commands.cicat_list_user: #ЦИТАТА
		    				CITAT = 'https://citatnica.ru/citaty/samye-luchshie-tsitaty'
		    				headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
		    				full_page = requests.get(CITAT, headers=headers)
		    				soup = BeautifulSoup(full_page.content, 'html.parser')
		    				convertd = soup.findAll("div", {"class": "su-note"})
		    				a = random.choice(convertd)
		    				a = a.text
		    				keyboard = Buttons.keyboard_citat
		    				write_button(sender, a)

			    		elif index == "шар":  #КОМАНДА ШАР
			    			write_message(sender, "⚠Введите команду /шар [фраза]")

				    	elif "шар " in index and not index == "шар":
				    		ball = random.choice(commands.ball_list)
				    		write_message(sender, "🔮")
				    		write_message(sender, ball)

			    		elif "выбери " in index:    #КОМАНДА ВЫБЕРИ
			    			reseived_message_new = index.lower().split("выбери ", 1)
			    			index = reseived_message_new[1].split(" или ")
			    			index1 = index[0]
			    			index2 = index[1]
			    			if "?" in index2 or "." in index2 or "!" in index2 or "," in index2:
			    				index2 = list(index2)
			    				index2.pop()
			    				index_new = index2
			    				index2 = ''.join(index_new)
			    				index = [index1, index2]
			    				message = random.choice(index)
			    				write_message(sender, message)
			    			else:
			    				index = [index1, index2]
			    				message = random.choice(index)
			    				write_message(sender, message)

			    		elif index in commands.history_list_user: #ЖУТКАЯ ИСТОРИЯ
			    			story = random.choice(History.history_list_bot)
			    			keyboard = Buttons.keyboard_history
			    			write_button(sender, story)

			    		elif index == "вероятность" or index == "инфа": #ВЕРОЯТНОСТЬ
			    			infa = random.choice(commands.infa_list_bot)
			    			write_message(sender, infa)

			    		elif ("вероятность " in index or "инфа " in index) and not (index == "вероятность" or index == "инфа"):
			    			reseived_message_new = index.lower().split(" ", 1)
			    			index = reseived_message_new[1]
			    			index = list(index)
			    			if "?" in index or "." in index or "!" in index:
			    				index.pop()
			    				index_new = index
			    				index = ''.join(index_new)
			    				infa = random.choice(commands.infa_list_bot)
			    				message = "Вероятность того, что " + index + ", равна: " + infa
			    				write_message(sender, message)
			    			else:
			    				index = ''.join(index)
			    				infa = random.choice(commands.infa_list_bot)
			    				message = "Вероятность того, что " + index + ", равна: " + infa
			    				write_message(sender, message)

			    		elif "flip " in index and not index == "flip":    #КОМАНДА /FLIP
			    			reseived_message_new = index.lower().split(" ", 1)
			    			index = reseived_message_new[1]
			    			flip = index[::-1]
			    			write_message(sender, "🔁Переворачиваю...")
			    			write_message(sender, flip)

			    		elif index == "flip":
			    			write_message(sender, "⚠Введите команду /flip [фраза]")

			    		elif index == "погода": #ПОГОДА
			    			write_message(sender, "⚠Введите команду /погода [город]")

			    		elif "погода " in index and not index == "погода": #ПОГОДА
			    			try:
				    			reseived_message_new = index.lower().split(" ", 1)
				    			city = reseived_message_new[1]
				    			observation = mgr.weather_at_place(city)
				    			weather = observation.weather
				    			a = weather.detailed_status
				    			temp = weather.temperature('celsius')['temp']
				    			wind = observation.weather.wind()['speed']
				    			weather1 = '''
				    			🌥Погода🌥
				    			'''
				    			weathercity = "\n🏛В городе сейчас " + a + "."
				    			down1 = '''
				    			'''
				    			cels = "\n🌡Температура в городе " + city + " в данный момент приблизительно равна " + str(temp) + "° градусов."
				    			down2 = '''
				    			'''
				    			wind1 = "\n💨Скорость ветра в данный момент составляет приблизительно " + str(wind) + " м/с."
				    			message = weather1 + weathercity + down1 + cels + down2 + wind1
				    		except:
				    			write_message(sender, "⚠Такого города не существует.")
				    		else:
				    			write_message(sender, message)

			    		elif "вики " in index or "википедия " in index: #КОМАНДА ВИКИ
			    			try:
				    			reseived_message_new = index.lower().split(" ", 1)
				    			index = reseived_message_new[1]
				    			write_message(sender, "⌛Подождите...")
				    			wikipedia.set_lang('ru')
				    			wiki = wikipedia.summary(index)
				    		except:
				    			write_message(sender, "⚠Не удалось найти информацию.")
				    		else:
				    			write_message(sender, wiki)

			    		elif "перевод " in index or "переведи " in index: #КОМАНДА ПЕРЕВОДА
			    			try:
				    			reseived_message_new = index.lower().split(" ", 1)
				    			index = reseived_message_new[1]
				    			write_message(sender, "⌛Подождите...")
				    			translator= Translator(to_lang="ru")
				    			translation = translator.translate(index)
				    		except:
				    			write_message(sender, "⚠Не удалось выполнить перевод.")
				    		else: 
		    					write_message(sender, translation)

			    		elif index == "idc":
			    			idc = event.chat_id
			    			idc = "Айди беседы🆔: " + str(idc)
			    			write_message(sender, "⌛Подождите...")
			    			write_message(sender, idc)

				    	elif index == "ed": #КОМАНДА /ed
				    		write_message(sender, "⚠Введите команду /ed [название]")

				    	elif "ed " in index and not index == "ed":
				    		try:
					    		reseived_message_new = index.split(" ", 1)
					    		title = reseived_message_new[1]
					    		ids = event.chat_id
					    		write_message(sender, "⌛Подождите...")
					    		edit_chat(ids, title)
					    	except:
					    		write_message(sender, "⚠Бота необходимо назначить администратором в беседе.")

				    	elif index == "vs":
			    			write_message(sender, "⚠Введите команду /vs [противник] против [противник2]")

				    	elif "vs " in index: #КОМАНДА /VS
				    		reseived_message_new = index.split("vs ", 1)
				    		reseived_message_new2 = reseived_message_new[1]
				    		index = reseived_message_new2.split(" против ", 1)
				    		index1 = index[0]
				    		index2 = index[1]
				    		damage1 = [15, 30, 35]
				    		damage2 = [40, 45, 50]
				    		damage_list = ["наносит урон", "наносит критический урон"]
				    		protection = "защитился(ась) от урона"
				    		protection_tf = [True, False, False]
				    		write_message(sender, "Бой начинается!")
				    		vs = True
				    		life1 = 100
				    		life2 = 100
				    		while vs == True:
				    			score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				    			write_message(sender, score)
				    			damagelist = random.choice(damage_list)
				    			batle = index1 + " " + damagelist
				    			write_message(sender, batle)
				    			protect = random.choice(protection_tf)
				    			if damagelist == "наносит урон" and protect == False:
				    				damage = random.choice(damage1)
				    				life = life2 - damage
				    				life2 = life
				    				score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				    				if life2 > 0:
				    					write_message(sender, score)
				    					damagelist = random.choice(damage_list)
				    					batle = index2 + " " + damagelist
				    					write_message(sender, batle)
				    					if damagelist == "наносит урон" and protect == False:
				    						damage = random.choice(damage1)
				    						life = life1 - damage
				    						life1 = life
				    						if life1 <= 0:
				    							vs = False
				    							life1 = 0
				    							score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				    							write_message(sender, score)
				    							win = "🏆" + index2 + " " + "победил!" + "🏆"
				    							write_message(sender, win)
				    							life1 = 100
				    							life2 = 100
				    					elif damagelist == "наносит критический урон" and protect == False:
				    						damage = random.choice(damage2)
				    						life = life1 - damage
				    						life1 = life
				    						if life1 <= 0:
				    							vs = False
				    							life1 = 0
				    							score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				    							write_message(sender, score)
				    							win = "🏆" + index2 + " " + "победил!" + "🏆"
				    							write_message(sender, win)
				    							life1 = 100
				    							life2 = 100
				    					elif protect == True:
				    						batle = index1 + " " + "защитился(ась) от урона"
				    						write_message(sender, batle)
				    				elif life2 <= 0:
				    					vs = False
				    					life2 = 0
				    					score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				    					write_message(sender, score)
				    					win = "🏆" + index1 + " " + "победил!" + "🏆"
				    					write_message(sender, win)
				    					life1 = 100
				    					life2 = 100
				    			elif damagelist == "наносит критический урон" and protect == False:
				    				damage = random.choice(damage2)
				    				life = life2 - damage
				    				life2 = life
				    				score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				    				if life2 > 0:
				    					write_message(sender, score)
				    					damagelist = random.choice(damage_list)
				    					batle = index2 + " " + damagelist
				    					write_message(sender, batle)
				    					if damagelist == "наносит урон" and protect == False:
				    						damage = random.choice(damage1)
				    						life = life1 - damage
				    						life1 = life
				    						if life1 <= 0:
				    							vs = False
				    							life1 = 0
				    							score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				    							write_message(sender, score)
				    							win = "🏆" + index2 + " " + "победил!" + "🏆"
				    							write_message(sender, win)
				    							life1 = 100
				    							life2 = 100
				    					elif damagelist == "наносит критический урон" and protect == False:
				    						damage = random.choice(damage2)
				    						life = life1 - damage
				    						life1 = life
				    						if life1 <= 0:
				    							vs = False
				    							life1 = 0
				    							score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				    							write_message(sender, score)
				    							win = "🏆" + index2 + " " + "победил!" + "🏆"
				    							write_message(sender, win)
				    							life1 = 100
				    							life2 = 100
				    					elif protect == True:
				    						batle = index1 + " " + "защитился(ась) от урона"
				    						write_message(sender, batle)
				    				elif life2 <= 0:
				    					vs = False
				    					life2 = 0
				    					score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				    					write_message(sender, score)
				    					win = "🏆" + index1 + " " + "победил!" + "🏆"
				    					write_message(sender, win)
				    					life1 = 100
				    					life2 = 100
				    			elif protect == True:
				    				batle = index2 + " " + "защитился(ась) от урона"
				    				write_message(sender, batle)
				    				damagelist = random.choice(damage_list)
				    				batle = index2 + " " + damagelist
				    				protect = random.choice(protection_tf)
				    				write_message(sender, batle)
				    				if damagelist == "наносит урон" and protect == False:
				    					damage = random.choice(damage1)
				    					life = life1 - damage
				    					life1 = life
				    					if life1 <= 0:
				    						vs = False
				    						life1 = 0
				    						score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				    						write_message(sender, score)
				    						win = "🏆" + index2 + " " + "победил!" + "🏆"
				    						write_message(sender, win)
				    						life1 = 100
				    						life2 = 100
				    				elif damagelist == "наносит критический урон" and protect == False:
				    					damage = random.choice(damage2)
				    					life = life1 - damage
				    					life1 = life
				    					if life1 <= 0:
				    						vs = False
				    						life1 = 0
				    						score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				    						write_message(sender, score)
				    						win = "🏆" + index2 + " " + "победил!" + "🏆"
				    						write_message(sender, win)
				    						life1 = 100
				    						life2 = 100
				    				elif protect == True:
				    					batle = index1 + " " + "защитился(ась) от урона"
				    					write_message(sender, batle)

				    	elif index == "сократи ссылку": #СОКРАЩЕННАЯ ССЫЛКА
			    			write_message(sender, "⚠Введите команду /сократи ссылку [ссылка]")

			    		elif "сократи ссылку " in index: #СОКРАЩЕННАЯ ССЫЛКА
			    			try:
				    			iduser = event.message.get("from_id")
				    			user = vk_session.method("users.get", {"user_ids": iduser})
				    			name = user[0]['first_name']
				    			a = index.split("сократи ссылку ", 1)
				    			a = a[1]
				    			s = pyshorteners.Shortener()
				    			link = s.tinyurl.short(a)
				    			write_message(sender, "⌛Подождите...")
				    			link = "👨‍💼" + name + ", " + "вот ваша сокращенная ссылка: " + link
				    			write_message(sender, link)
				    		except:
				    			write_message(sender, "⚠Ошибка!")

				    	elif "видео " in index:
				    		try:
				    			a = index.split(" ", 1)
				    			title = a[1]
				    			Video_script.videos.search(title)
				    			video = Video_script.videos.videos_url
				    			write_video2(sender, video, title)
				    		except:
				    			write_message(sender, "⚠Ошибка!")

			    		elif index == "видео":
			    			write_message(sender, "⚠Введите команду /видео [название]")

			    		elif "репорт " in index or "report " in index: #ПРОВЕРИТЬ!!!!!!!!!!!!!!!!!!!!!!
			    			iduser = event.message.get("from_id")
			    			user = vk_session.method("users.get", {"user_ids": iduser})
			    			name = user[0]['first_name'] #ПОЛУЧЕНИЕ ИМЕНИ ПОЛЬЗОВАТЕЛЯ
			    			name2 = user[0]['last_name'] #ПОЛУЧЕНИЕ ФАМИЛИИ ПОЛЬЗОВАТЕЛЯ
			    			a = reseived_message.lower().split(" ", 1)
			    			text = a[1]
			    			message1 = '\n' + "📫Пользователь отправил сообщение в тех.поддержку!" + '\n'
			    			
			    			message2 = '\n' + "🆔Id отправителя: " + str(iduser)
			    			message3 = '\n' + "👤Имя и фамилия отправителя: " + name + " " + name2
			    			message4 = '\n' + "✉Текст сообщения: " + '\n'+ '\n' + text
			    			message = message1 + message2 + message3 + message4
			    			vk_session.method('messages.send', {'peer_id': 2000000000 + 23, 'message': message, 'random_id': get_random_id()})
			    			write_message(sender, "✅Ваше сообщение успешно доставлено администрации!")

			    		elif index == "репорт" or index == "report": #ПРОВЕРИТЬ!!!!!!!!!!!!!!!!!!!!!!
			    			write_message(sender, "⚠Введите команду /репорт [сообщение]")

		    			else:
		    				iduser = event.message.get("from_id")
			    			user = vk_session.method('users.get', {'user_ids': iduser, 'fields': 'sex'})
					    	sex = user[0]['sex'] #Пол пользователя.
			    			message = reseived_message.lower()
			    			words = Phrases.filter.words #Слова пользователя
			    			text_bot = Phrases.Hello.text_bot #Сообщения бота пользователю
			    			Phrases.filter.analysis(message)
			    			Phrases.Hello.write(words, sex)
			    			for t in text_bot:
			    				write_message(sender, t)
			    			Phrases.remove.delete(words, text_bot)


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		    	elif event.from_user and event.message and event.message.get('text'):   #ЕСЛИ НАПИСАЛИ В ЛС
		    		reseived_message = event.message.get("text")
		    		sender = event.message.get("from_id")
		    		id_message = event.message.get("id")

		    		if reseived_message.lower() == "следующий анекдот😂":
		    			f = open('Data/joke.txt', 'r+')
		    			a = f.readlines()
		    			joke = random.choice(a)
		    			keyboard = Buttons.keyboard_joke
		    			write_button2(sender, joke)
		    			f.close()

		    		elif reseived_message.lower() == "следующая история😱":
		    			story = random.choice(History.history_list_bot)
		    			keyboard = Buttons.keyboard_history
	    				write_button2(sender, story)

		    		elif reseived_message.lower() == "следующая цитата📕":
		    			CITAT = 'https://citatnica.ru/citaty/samye-luchshie-tsitaty'
	    				headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
	    				full_page = requests.get(CITAT, headers=headers)
	    				soup = BeautifulSoup(full_page.content, 'html.parser')
	    				convertd = soup.findAll("div", {"class": "su-note"})
	    				a = random.choice(convertd)
	    				a = a.text
	    				keyboard = Buttons.keyboard_citat
		    			write_button2(sender, a)

		    		elif reseived_message.lower() == "/help!":
		    			write_message2(sender, commands.help_list_bot2)

		    		elif reseived_message.lower() in commands.help_list_user: #КОМАНДЫ
		    			write_message2(sender, commands.help_list_bot)

		    		elif reseived_message.lower() in commands.joke_list_user: #АНЕКДОТ
	    				f = open('joke.txt', 'r+')
		    			a = f.readlines()
		    			joke = random.choice(a)
		    			keyboard = Buttons.keyboard_joke
		    			write_button2(sender, joke)
		    			f.close()

		    		elif reseived_message.lower() in commands.history_list_user: #ЖУТКАЯ ИСТОРИЯ
		    			story = random.choice(History.history_list_bot)
		    			keyboard = Buttons.keyboard_history
	    				write_button2(sender, story)

		    		elif reseived_message.lower() in commands.cicat_list_user: #ЦИТАТА
		    			CITAT = 'https://citatnica.ru/citaty/samye-luchshie-tsitaty'
		    			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
		    			full_page = requests.get(CITAT, headers=headers)
		    			soup = BeautifulSoup(full_page.content, 'html.parser')
		    			convertd = soup.findAll("div", {"class": "su-note"})
		    			a = random.choice(convertd)
		    			a = a.text
		    			keyboard = Buttons.keyboard_citat
		    			write_button2(sender, a)

		    		elif reseived_message.lower() == "шар" or reseived_message.lower() == "/шар":  #КОМАНДА ШАР
		    				write_message2(sender, "⚠Введите команду шар [фраза]")

		    		elif ("шар " in reseived_message.lower() or "/шар " in reseived_message.lower()) and not (reseived_message.lower() == "шар" or reseived_message.lower() == "/шар"):
		    			ball = random.choice(commands.ball_list)
		    			write_message2(sender, "🔮")
		    			write_message2(sender, ball)

		    		elif "выбери " in reseived_message.lower():    #КОМАНДА ВЫБЕРИ
		    			reseived_message_new = reseived_message.lower().split("выбери ", 1)
		    			index = reseived_message_new[1].split(" или ")
		    			index1 = index[0]
		    			index2 = index[1]
		    			if "?" in index2 or "." in index2 or "!" in index2 or "," in index2:
		    				index2 = list(index2)
		    				index2.pop()
		    				index_new = index2
		    				index2 = ''.join(index_new)
		    				index = [index1, index2]
		    				message = random.choice(index)
		    				write_message2(sender, message)
		    			else:
		    				index = [index1, index2]
		    				message = random.choice(index)
		    				write_message2(sender, message)

		    		elif reseived_message.lower() == "вероятность" or reseived_message.lower() == "инфа" or reseived_message.lower() == "/инфа" or reseived_message.lower() == "/вероятность": #ВЕРОЯТНОСТЬ
		    			infa = random.choice(commands.infa_list_bot)
		    			write_message2(sender, infa)

		    		elif ("вероятность " in reseived_message.lower() or "инфа " in reseived_message.lower() or "/вероятность " in reseived_message.lower() or "/инфа " in reseived_message.lower()) and not (reseived_message.lower() == "вероятность" or reseived_message.lower() == "инфа" or reseived_message.lower() == "/инфа" or reseived_message.lower() == "/вероятность"):
		    			reseived_message_new = reseived_message.lower().split(" ", 1)
		    			index = reseived_message_new[1]
		    			index = list(index)
		    			if "?" in index or "." in index or "!" in index:
		    				index.pop()
		    				index_new = index
		    				index = ''.join(index_new)
		    				infa = random.choice(commands.infa_list_bot)
		    				message = "Вероятность того, что " + index + ", равна: " + infa
		    				write_message2(sender, message)
		    			else:
		    				index = ''.join(index)
		    				infa = random.choice(commands.infa_list_bot)
		    				message = "Вероятность того, что " + index + ", равна: " + infa
		    				write_message2(sender, message)

		    		elif ("/flip " in reseived_message.lower() or "flip " in reseived_message.lower()) and not (reseived_message.lower() == "/flip" or reseived_message.lower() == "flip"):    #КОМАНДА /FLIP
		    			reseived_message_new = reseived_message.lower().split(" ", 1)
		    			index = reseived_message_new[1]
		    			flip = index[::-1]
		    			write_message2(sender, "🔁Переворачиваю...")
		    			write_message2(sender, flip)

		    		elif reseived_message.lower() == "/flip" or reseived_message.lower() == "flip":
		    			write_message2(sender, "⚠Введите команду /flip [фраза]")

		    		elif reseived_message.lower() == "вероятность" or reseived_message.lower() == "инфа" or reseived_message.lower() == "/инфа" or reseived_message.lower() == "/вероятность": #ВЕРОЯТНОСТЬ
		    			infa = random.choice(commands.infa_list_bot)
		    			write_message2(sender, infa)

		    		elif ("вероятность " in reseived_message.lower() or "инфа " in reseived_message.lower() or "/вероятность " in reseived_message.lower() or "/инфа " in reseived_message.lower()) and not (reseived_message.lower() == "вероятность" or reseived_message.lower() == "инфа" or reseived_message.lower() == "/инфа" or reseived_message.lower() == "/вероятность"):
		    			reseived_message_new = reseived_message.lower().split(" ", 1)
		    			index = reseived_message_new[1]
		    			index = list(index)
		    			if "?" in index or "." in index or "!" in index:
		    				index.pop()
		    				index_new = index
		    				index = ''.join(index_new)
		    				infa = random.choice(commands.infa_list_bot)
		    				message = "Вероятность того, что " + index + ", равна: " + infa
		    				write_message2(sender, message)
		    			else:
		    				index = ''.join(index)
		    				infa = random.choice(commands.infa_list_bot)
		    				message = "Вероятность того, что " + index + ", равна: " + infa
		    				write_message2(sender, message)

		    		elif reseived_message.lower() in commands.id_list: #КОМАНДА АЙДИ
		    			iduser = event.message.get("from_id")
		    			user = vk_session.method("users.get", {"user_ids": iduser})
		    			name = user[0]['first_name']
		    			write_message2(sender, "⌛Подождите...")
		    			iduser = name + ", " + " ваш 🆔: " + str(iduser)
		    			write_message2(sender, iduser)

		    		elif reseived_message.lower() == "погода" or reseived_message.lower() == "/погода":   # ПОГОДА
		    			write_message2(sender, "⚠Введите команду погода [город]")

		    		elif ("погода " in reseived_message.lower() or "/погода " in reseived_message.lower()) and not (reseived_message.lower() == "погода" or reseived_message.lower() == "/погода"):
		    			try:
			    			reseived_message_new = reseived_message.lower().split(" ", 1)
			    			city = reseived_message_new[1]
			    			observation = mgr.weather_at_place(city)
			    			weather = observation.weather
			    			a = weather.detailed_status
			    			temp = weather.temperature('celsius')['temp']
			    			wind = observation.weather.wind()['speed']
			    			weather1 = '''
			    			🌥Погода🌥
			    			'''
			    			weathercity = "\n🏛В городе сейчас " + a + "."
			    			down1 = '''
			    			'''
			    			cels = "\n🌡Температура в городе " + city + " в данный момент приблизительно равна " + str(temp) + "° градусов."
			    			down2 = '''
			    			'''
			    			wind1 = "\n💨Скорость ветра в данный момент составляет приблизительно " + str(wind) + " м/с."
			    			message = weather1 + weathercity + down1 + cels + down2 + wind1
			    		except:
			    			write_message2(sender, "⚠Ошибка! Такого города не существует.")
			    		else:
			    			write_message2(sender, message)

		    		elif "вики " in reseived_message.lower() or "/вики " in reseived_message.lower() or "википедия " in reseived_message.lower() or "/википедия " in reseived_message.lower(): #КОМАНДА 
		    			try:
			    			reseived_message_new = reseived_message.lower().split(" ", 1)
			    			index = reseived_message_new[1]
			    			write_message2(sender, "⌛Подождите...")
			    			wikipedia.set_lang('ru')
			    			wiki = wikipedia.summary(index)
			    		except:
			    			write_message2(sender, "⚠Не могу найти информацию.")
			    		else:
			    			write_message2(sender, wiki)

		    		elif "перевод " in reseived_message.lower() or "переведи " in reseived_message.lower() or "/перевод " in reseived_message.lower() or "/переведи " in reseived_message.lower(): #КОМАНДА ПЕРЕВОДА
		    			try:
			    			reseived_message_new = reseived_message.lower().split(" ", 1)
			    			index = reseived_message_new[1]
			    			write_message2(sender, "⌛Подождите...")
			    			translator= Translator(to_lang="ru")
			    			translation = translator.translate(index)
			    		except:
			    			write_message2(sender, "⚠Не удалось выполнить перевод.")
			    		else:
			    			write_message2(sender, translation)							

		    		elif reseived_message.lower() == "/ed" or ("/ed " in reseived_message.lower() and not reseived_message.lower() == "/ed"):
		    			write_message2(sender, "⚠Эта команда работает только в беседе.")

		    		elif reseived_message.lower() == "/idc" or reseived_message.lower() == "idc": #КОМАНДА АЙДИ БЕСЕДЫ
		    			write_message2(sender, "⚠Эта команда работает только в беседе.")

			    	elif reseived_message.lower() == "/vs":
			    		write_message2(sender, "⚠Введите команду /vs [противник] против [противник2]")

			    	elif "/vs " in reseived_message.lower():
			    		Fight.user(sender, reseived_message)
			    		

			    	elif reseived_message.lower() == "/covid" or reseived_message.lower() == "covid" or reseived_message.lower() == "коронавирус" or reseived_message.lower() == "/коронавирус" or reseived_message.lower() == "/covid19" or reseived_message.lower() == "ковид" or reseived_message.lower() == "/ковид": #КОРОНАВИРУС
			    		covid1()

		    		elif reseived_message.lower() == "/сократи ссылку" or reseived_message.lower() == "сократи ссылку": #СОКРАЩЕННАЯ ССЫЛКА
		    			write_message2(sender, "⚠Введите команду /сократи ссылку [ссылка]")

		    		elif "сократи ссылку " in reseived_message.lower(): #СОКРАЩЕННАЯ ССЫЛКА
		    			try:
			    			iduser = event.message.get("from_id")
			    			user = vk_session.method("users.get", {"user_ids": iduser})
			    			name = user[0]['first_name']
			    			a = reseived_message.lower().split("сократи ссылку ", 1)
			    			a = a[1]
			    			s = pyshorteners.Shortener()
			    			link = s.tinyurl.short(a)
			    			write_message2(sender, "⌛Подождите...")
			    			link = "👨‍💼" + name + ", " + "вот ваша сокращенная ссылка: " + link
			    			write_message2(sender, link)
			    		except:
			    			write_message2(sender, "⚠Напишите команду правильно!")

		    		elif reseived_message.lower() == "/infa":
				    	user = vk_session.method('users.get', {'user_ids': sender, 'fields': 'sex'})
				    	sex = user[0]['sex']
				    	message = "Изменено."
				    	write_message2(sender, "Взлом пентагона: 0%")
				    	id_message = id_message + 1
				    	n = 0
				    	while n <= 90:
				    		n = n + 20
				    		message = "👩‍Взлом пентагона: " + str(n) + "%"
				    		edit_message(sender, message, id_message)
				    	write_message2(sender, "🔥Пентагон взломан!")

		    		elif reseived_message.lower() == "/баланс" or reseived_message == "Баланс💰":
		    			iduser = sender #АЙДИ ПОЛЬЗОВАТЕЛЯ
		    			user = vk_session.method("users.get", {"user_ids": iduser})
		    			name = user[0]['first_name'] #ПОЛУЧЕНИЕ ИМЕНИ ПОЛЬЗОВАТЕЛЯ
		    			Balance_script.Money.Check_and_write(iduser)
				    	text = name + ", " + "ваш баланс" + "&#128176;" + ": " + str(Balance.Money.balance) + "&#128178;"
				    	keyboard = Buttons.keyboard_balance
				    	write_button2(sender, text)

		    		elif "/гиф " in reseived_message.lower() or "/gif " in reseived_message.lower():
		    			messege = reseived_message.lower().split(" ", 1)
		    			text = messege[1]
		    			a = Gif_script.Gif.Search(text)
		    			write_message2(sender, Gif_script.Gif.url)

		    		elif "/видео " in reseived_message.lower():
		    			a = reseived_message.lower().split(" ", 1)
		    			title = a[1]
		    			Video_script.videos.search(title)
		    			video = Video_script.videos.videos_url
		    			write_video(sender, video, title)

		    		elif reseived_message.lower() == "/видео":
		    			write_message2(sender, "⚠Введите команду /видео [название]")

		    		elif "/репорт " in reseived_message.lower() or "/report " in reseived_message.lower():
		    			try:
			    			user = vk_session.method("users.get", {"user_ids": sender})
			    			name = user[0]['first_name'] #ПОЛУЧЕНИЕ ИМЕНИ ПОЛЬЗОВАТЕЛЯ
			    			name2 = user[0]['last_name'] #ПОЛУЧЕНИЕ ФАМИЛИИ ПОЛЬЗОВАТЕЛЯ
			    			a = reseived_message.lower().split(" ", 1)
			    			text = a[1]
			    			message1 = '\n' + "📫Пользователь отправил сообщение в тех.поддержку!" + '\n'
			    			
			    			message2 = '\n' + "🆔Id отправителя: " + str(sender)
			    			message3 = '\n' + "👤Имя и фамилия отправителя: " + name + " " + name2
			    			message4 = '\n' + "✉Текст сообщения: " + '\n'+ '\n' + text + '\n' + '\n'
			    			message5 = "Введите команду /ответ [айди] [текст сообщения]"
			    			message = message1 + message2 + message3 + message4 + message5
			    			vk_session.method('messages.send', {'peer_id': 2000000000 + 23, 'message': message, 'random_id': get_random_id()})
			    			write_message2(sender, "✅Ваше сообщение успешно доставлено администрации!")
			    		except:
			    			write_message2(sender, "⚠Ошибка!")	
			    		

		    		elif reseived_message.lower() == "/репорт" or reseived_message.lower() == "/report": #ПРОВЕРИТЬ!!!!!!!!!!!!!!!!!!!!!!
		    			write_message2(sender, "⚠Введите команду /репорт [сообщение]")
		    		
		    		elif reseived_message.lower() == "/мем":
		    			write_photo2(sender)

		    		else:
		    			user = vk_session.method('users.get', {'user_ids': sender, 'fields': 'sex'})
				    	sex = user[0]['sex'] #Пол пользователя.
		    			message = reseived_message.lower()
		    			words = Phrases.filter.words #Слова пользователя
		    			text_bot = Phrases.Hello.text_bot #Сообщения бота пользователю
		    			Phrases.filter.analysis(message)
		    			Phrases.Hello.write(words, sex)
		    			for t in text_bot:
		    				write_message2(sender, t)
		    			Phrases.remove.delete(words, text_bot)

	except requests.exceptions.ReadTimeout:
		print("\n Переподключение к серверам ВК \n")
		time.sleep(3)

		

