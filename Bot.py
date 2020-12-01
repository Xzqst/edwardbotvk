# -*- coding: utf8 -*-
#Бот Едвард
import vk_api
import random

import os
import time

import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML

import wikipedia

from translate import Translator

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id


from covid.api import CovId19Data #КОРОНАВИРУС


from Phrases import hello_list_user, hello_list_bot, fail_list_bot, user_bot_list, mates_list_user, mates_list_bot, why_list_bot, case_list_bot, case_list_bot2, sorry_bot_list, answer_list_user, answer_list_bot, yes_list_bot, no_list_bot
from commands import help_list_user, help_list_bot, joke_list_user, history_list_user, ball_list, infa_list_bot, id_list, cicat_list_user
from History import history_list_bot

def write_message(sender, message): #ОТПРАВКА СООБЩЕНИЯ В БЕСЕДУ
	vk_session.method('messages.send', {'chat_id': sender, 'message': message, 'random_id': get_random_id()})

def write_message2(sender, message): #ОТПРАВКА СООБЩЕНИЯ В ЛС
	vk_session.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})

def edit_chat(ids, title): #ИЗМЕНЕНИЕ НАЗВАНИЯ БЕСЕДЫ
	vk_session.method('messages.editChat', {'chat_id': ids, 'title': title})

def members_chat(idc):
	vk_session.method('messages.getConversationMembers', {'peer_id': idc, 'group_id': 197481314})


token="f4a8b4fc8fe0aa8e080fc21186f5606bd26e26f6429715472af9e201254862bf07c4cec92858e0d40558a"  #ТОКЕН ГРУППЫ

vk_session = VkApi(token = token)

longpoll = VkBotLongPoll(vk_session, 197481314)

longpollbot = True

 #ПОГОДА
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('1ad03b7000a938a954739c5d5d77e6f2', config_dict)



mgr =  owm.weather_manager() #ПОГОДА

api = CovId19Data(force=True) #КОРОНАВИРУС


while longpollbot:

	try:
	



		for event in longpoll.listen():


		    if event.type == VkBotEventType.MESSAGE_NEW:

		    	if event.from_chat and event.message and event.message.get('text'):  #ЕСЛИ НАПИСАЛИ В ЧАТЕ

		    		reseived_message = event.message.get("text")
		    		sender = event.chat_id


		    		#КОМАНДЫ НУЖНО ПИСАТЬ ТОЛЬКО С ОБРАЩЕНИЕМ К БОТУ

		    		if ("едвард " in reseived_message.lower() or "эдвард " in reseived_message.lower() or "бот " in reseived_message.lower() or "edward " in reseived_message.lower()) or ("едвард, " in reseived_message.lower() or "эдвард, " in reseived_message.lower() or "бот, " in reseived_message.lower() or "edward, " in reseived_message.lower()):    #Проверяем, обратились ли к боту
		    			reseived_message_new = reseived_message.lower().split(" ", 1)
		    			index = reseived_message_new[1]
		    			indexball = reseived_message_new[0]

		    			if index in hello_list_user:
		    				hello = random.choice(hello_list_bot)
		    				write_message(sender, hello)

		    			elif index == "да" or index == "да." or index == "да!" or index == "да?" or index == "да,": #ДА
		    				yes = random.choice(yes_list_bot)
		    				write_message(sender, yes)

		    			elif index == "нет" or index == "нет." or index == "нет!" or index == "нет?" or index == "нет," or index == "не" or index == "не." or index == "не," or index == "не!" or index == "не?": #НЕТ
		    				no = random.choice(no_list_bot)
		    				write_message(sender, no)


		    			elif index in help_list_user:   #список команд
		    				write_message(sender, help_list_bot)

		    			elif index in joke_list_user:  #АНЕКДОТ
		    				pages = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
		    				JOKE = 'https://nekdo.ru/short/'
		    				headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
		    				full_page = requests.get(JOKE, headers=headers)
		    				soup = BeautifulSoup(full_page.content, 'html.parser')
		    				convertd = soup.findAll("div", {"class": "text"})
		    				r = random.choice(pages)
		    				JOKE2 = JOKE + str(r) + '/'
		    				full_page = requests.get(JOKE2, headers=headers)
		    				soup = BeautifulSoup(full_page.content, 'html.parser')
		    				convertd = soup.findAll("div", {"class": "text"})
		    				a = random.choice(convertd)
		    				a = a.text
		    				write_message(sender, a)

		    			elif index in history_list_user: #ЖУТКАЯ ИСТОРИЯ
		    				story = random.choice(history_list_bot)
		    				write_message(sender, story)

		    			elif index in cicat_list_user: #ЦИТАТА
		    				CITAT = 'https://citatnica.ru/citaty/samye-luchshie-tsitaty'
		    				headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
		    				full_page = requests.get(CITAT, headers=headers)
		    				soup = BeautifulSoup(full_page.content, 'html.parser')
		    				convertd = soup.findAll("div", {"class": "su-note"})
		    				a = random.choice(convertd)
		    				a = a.text
		    				write_message(sender, a)

		    			elif index == "шар" or index == "/шар":  #КОМАНДА ШАР
		    				write_message(sender, "⚠Введите команду шар [фраза]")

		    			elif ("шар " in index or "/шар " in index) and not (index == "шар" or index == "/шар"):
		    				ball = random.choice(ball_list)
		    				write_message(sender, "🔮")
		    				write_message(sender, ball)

		    			elif "выбери " in index:    #КОМАНДА ВЫБЕРИ
		    				reseived_message_new = index.split("выбери ", 1)
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

		    			elif "шар " in indexball or "/шар " in indexball:
		    				ball = random.choice(ball_list)
		    				write_message(sender, "🔮")
		    				write_message(sender, ball)

		    			elif index in id_list:
			    			iduser = event.message.get("from_id")
			    			user = vk_session.method("users.get", {"user_ids": iduser})
			    			name = user[0]['first_name']
			    			write_message(sender, "⌛Подождите...")
			    			iduser = name + ", " + " ваш 🆔: " + str(iduser)
			    			write_message(sender, iduser)

			    		elif index in mates_list_user:
			    			r = [True, False, False]
			    			r = random.choice(r)
			    			if r == True:
			    				r = "Сам " + index
			    				write_message(sender, r)
			    			elif r == False:
				    			mat = random.choice(mates_list_bot)
				    			write_message(sender, mat)

				    	elif index == "ed": #КОМАНДА /ed
				    		write_message(sender, "⚠Введите команду /ed [название]")

				    	elif "ed " in index and not index == "ed": #РЕДАКТИРОВАНИЕ НАЗВАНИЯ БЕСЕДЫ

				    		try:

					    		reseived_message_new = index.split(" ", 1)
					    		title = reseived_message_new[1]
					    		ids = event.chat_id
					    		write_message(sender, "⌛Подождите...")

					    	except:

					    		write_message(sender, "⚠Чтобы эта команда работала, боту необходимо дать права администратора в беседе.")

					    	else:

					    		edit_chat(ids, title)

				    	elif "зачем" in index or "почему" in index or "нафига" in index or "нахрена" in index or "нахуя" in index:
				    		why = random.choice(why_list_bot)
				    		write_message(sender, why)

				    	elif "дела" in index and "как" in index:
				    		case = random.choice(case_list_bot)
				    		write_message(sender, case)
				    		d = [True, False, False]
				    		d = random.choice(d)

				    		if d == True:
				    			case = random.choice(case_list_bot2)
				    			write_message(sender, case)

				    	elif ("нахуй" in index and "иди" in index) or "съебал" in index or "пиздуй" in index or "блядь" in index or "пиздец" in index:
				    		mat = random.choice(mates_list_bot)
				    		write_message(sender, mat)

				    	elif "извини " in index or "прости" in index or index == "извини":
				    		sorry = random.choice(sorry_bot_list)
				    		write_message(sender, sorry)

				    	elif index in answer_list_user:
				    		answer = random.choice(answer_list_bot)
				    		write_message(sender, answer)

				    	elif index == "covid" or index == "коронавирус" or index == "covid19": #КОРОНАВИРУС

				    		try:

				    			res = api.get_stats()
				    			ru = api.filter_by_country("russia")
					    		write_message(sender, "⚠Подождите...")
					    		cov0 = '''
					    		🦠Статистика случаев заражения коронавирусом🦠
					    		'''
					    		cov11 = "\n🌐В мире:"
					    		
					    		cov1 = "\n🤒" + "Заражений: " + str(res['confirmed'])
					    		cov2 = "\n☠" + "Смертей: " + str(res['deaths'])
					    		cov3 = "\n💊" + "Выздоровлений: " + str(res['recovered'])
					    		cov4 = "\n "
					    		cov5 = "\n🇷🇺В России:"
					    		cov6 = "\n🤒" + "Заражений: " + str(ru['confirmed'])
					    		cov7 = "\n☠" + "Смертей: " + str(ru['deaths'])
					    		cov8 = "\n💊" + "Выздоровлений: " + str(ru['recovered'])

					    		cov9 = '''

					    		⚠В случае, если в вашей местности зарегистрировано распространение COVID-19, соблюдайте простые меры предосторожности: держитесь на безопасной дистанции от окружающих, носите маску, хорошо проветривайте помещения, избегайте мест скопления людей, мойте руки и прикрывайте нос и рот сгибом локтя или салфеткой при кашле или чихании. Следите за рекомендациями для вашего населенного пункта и места работы. Беригите себя!
					    		'''
					    		cov = cov0 + cov11 + cov1 + cov2 + cov3 + cov4 + cov5 + cov6 + cov7 + cov8 + cov9

					    	except:

					    		write_message(sender, "⚠Не удалось получить информацию.")

					    	else:

					    		write_message(sender, cov)











		    			else:
		    				fail = random.choice(fail_list_bot)
		    				write_message(sender, fail)







		    		#КОМАНДЫ МОЖНО ПИСАТЬ, БЕЗ ОБРАЩЕНИЯ К БОТУ

		    		elif "/" in reseived_message.lower()[0]:
		    			reseived_message_new = reseived_message.lower().split("/", 1)
		    			index = reseived_message_new[1]






			    		if index == "эдвард" or index == "едвард" or index == "бот" or index == "edward":
			    			bot = random.choice(user_bot_list)
			    			write_message(sender, bot)

			    		elif index == "да" or index == "да." or index == "да!" or index == "да?" or index == "да,": #ДА
		    				yes = random.choice(yes_list_bot)
		    				write_message(sender, yes)

		    			elif index == "нет" or index == "нет." or index == "нет!" or index == "нет?" or index == "нет," or index == "не" or index == "не." or index == "не," or index == "не!" or index == "не?": #НЕТ
		    				no = random.choice(no_list_bot)
		    				write_message(sender, no)


			    		elif index in id_list: #КОМАНДА АЙДИ
			    			iduser = event.message.get("from_id")
			    			user = vk_session.method("users.get", {"user_ids": iduser})
			    			name = user[0]['first_name']
			    			write_message(sender, "⌛Подождите...")
			    			iduser = name + ", " + " ваш 🆔: " + str(iduser)
			    			write_message(sender, iduser)

			    		elif index == "covid" or index == "коронавирус" or index == "covid19": #КОРОНАВИРУС
			    			res = api.get_stats()
			    			ru = api.filter_by_country("russia")
				    		write_message(sender, "⚠Подождите...")
				    		cov0 = '''
				    		🦠Статистика случаев заражения коронавирусом🦠
				    		'''
				    		cov11 = "\n🌐В мире:"
				    		
				    		cov1 = "\n🤒" + "Заражений: " + str(res['confirmed'])
				    		cov2 = "\n☠" + "Смертей: " + str(res['deaths'])
				    		cov3 = "\n💊" + "Выздоровлений: " + str(res['recovered'])
				    		cov4 = "\n "
				    		cov5 = "\n🇷🇺В России:"
				    		cov6 = "\n🤒" + "Заражений: " + str(ru['confirmed'])
				    		cov7 = "\n☠" + "Смертей: " + str(ru['deaths'])
				    		cov8 = "\n💊" + "Выздоровлений: " + str(ru['recovered'])

				    		cov9 = '''

				    		⚠В случае, если в вашей местности зарегистрировано распространение COVID-19, соблюдайте простые меры предосторожности: держитесь на безопасной дистанции от окружающих, носите маску, хорошо проветривайте помещения, избегайте мест скопления людей, мойте руки и прикрывайте нос и рот сгибом локтя или салфеткой при кашле или чихании. Следите за рекомендациями для вашего населенного пункта и места работы. Беригите себя!
				    		'''
				    		cov = cov0 + cov11 + cov1 + cov2 + cov3 + cov4 + cov5 + cov6 + cov7 + cov8 + cov9
				    		write_message(sender, cov)



			    		elif index in hello_list_user:
			    			hello = random.choice(hello_list_bot)
			    			write_message(sender, hello)

			    		elif index in help_list_user: #список команд
			    			write_message(sender, help_list_bot)

			    		elif index in joke_list_user: #АНЕКДОТ
			    			pages = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
		    				JOKE = 'https://nekdo.ru/short/'
		    				headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
		    				full_page = requests.get(JOKE, headers=headers)
		    				soup = BeautifulSoup(full_page.content, 'html.parser')
		    				convertd = soup.findAll("div", {"class": "text"})
		    				r = random.choice(pages)
		    				JOKE2 = JOKE + str(r) + '/'
		    				full_page = requests.get(JOKE2, headers=headers)
		    				soup = BeautifulSoup(full_page.content, 'html.parser')
		    				convertd = soup.findAll("div", {"class": "text"})
		    				a = random.choice(convertd)
		    				a = a.text
		    				write_message(sender, a)

		    			elif index in cicat_list_user: #ЦИТАТА
		    				CITAT = 'https://citatnica.ru/citaty/samye-luchshie-tsitaty'
		    				headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
		    				full_page = requests.get(CITAT, headers=headers)
		    				soup = BeautifulSoup(full_page.content, 'html.parser')
		    				convertd = soup.findAll("div", {"class": "su-note"})
		    				a = random.choice(convertd)
		    				a = a.text
		    				write_message(sender, a)



			    		elif index == "шар":  #КОМАНДА ШАР
			    			write_message(sender, "⚠Введите команду /шар [фраза]")


				    	elif "шар " in index and not index == "шар":
				    		ball = random.choice(ball_list)
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




			    		elif index in history_list_user: #ЖУТКАЯ ИСТОРИЯ
			    			story = random.choice(history_list_bot)
			    			write_message(sender, story)




			    		elif index == "вероятность" or index == "инфа": #ВЕРОЯТНОСТЬ
			    			infa = random.choice(infa_list_bot)
			    			write_message(sender, infa)

			    		elif ("вероятность " in index or "инфа " in index) and not (index == "вероятность" or index == "инфа"):
			    			reseived_message_new = index.lower().split(" ", 1)
			    			index = reseived_message_new[1]
			    			index = list(index)
			    			if "?" in index or "." in index or "!" in index:
			    				index.pop()
			    				index_new = index
			    				index = ''.join(index_new)
			    				infa = random.choice(infa_list_bot)
			    				message = "Вероятность того, что " + index + ", равна: " + infa
			    				write_message(sender, message)
			    			else:
			    				index = ''.join(index)
			    				infa = random.choice(infa_list_bot)
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


			    		elif index in mates_list_user:
			    			r = [True, False, False]
			    			r = random.choice(r)
			    			if r == True:
			    				r = "Сам " + index
			    				write_message(sender, r)
			    			elif r == False:
				    			mat = random.choice(mates_list_bot)
				    			write_message(sender, mat)



				    	elif index == "ed": #КОМАНДА /ed
				    		write_message(sender, "⚠Введите команду /ed [название]")

				    	elif "ed " in index and not index == "ed":
				    		reseived_message_new = index.split(" ", 1)
				    		title = reseived_message_new[1]
				    		ids = event.chat_id
				    		write_message(sender, "⌛Подождите...")
				    		edit_chat(ids, title)

				    	elif index == "кто":
				    		ids = event.chat_id
				    		idc = 2000000000 + ids
				    		members_chat(idc)

				    		write_message(sender, count)


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

				    	elif "зачем" in index or "почему" in index or "нафига" in index or "нахрена" in index or "нахуя" in index:
				    		why = random.choice(why_list_bot)
				    		write_message(sender, why)

				    	elif "дела" in index and "как" in index:
				    		case = random.choice(case_list_bot)
				    		write_message(sender, case)
				    		d = [True, False, False]
				    		d = random.choice(d)

				    		if d == True:
				    			case = random.choice(case_list_bot2)
				    			write_message(sender, case)

				    	elif ("нахуй" in index and "иди" in index) or "съебал" in index or "пиздуй" in index or "блядь" in index or "пиздец" in index:
				    		mat = random.choice(mates_list_bot)
				    		write_message(sender, mat)

				    	elif "извини " in index or "прости" in index or index == "извини":
				    		sorry = random.choice(sorry_bot_list)
				    		write_message(sender, sorry)

				    	elif index in answer_list_user:
				    		answer = random.choice(answer_list_bot)
				    		write_message(sender, answer)

				    	elif index == "курс":
					    	write_message(sender, "⌛Подождите...")

					    	DOLLAR_RUB = 'https://www.google.ru/search?newwindow=1&ei=X8eCX9HEC8iHwPAPwdGcEA&q=курс+доллара&oq=курс+доллара&gs_lcp=CgZwc3ktYWIQAzINCAAQsQMQgwEQRhCCAjIFCAAQsQMyCAgAELEDEIMBMgUIABCxAzIFCAAQsQMyCAgAELEDEIMBMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzoCCABQ6gFYhhpguxtoAHAAeAGAAdUHiAG4FJIBBTUtMS4ymAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwiR8LC1lKzsAhXIAxAIHcEoBwIQ4dUDCA0&uact=5'
					    	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
					    	full_page = requests.get(DOLLAR_RUB, headers=headers)
					    	soup = BeautifulSoup(full_page.content, 'html.parser')
					    	convertd = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

					    	EURO_RUB = 'https://www.google.ru/search?newwindow=1&ei=jciCX5DlEYy53AO5t43YBg&q=курс+евро&oq=курс+евро&gs_lcp=CgZwc3ktYWIQAzIKCAAQsQMQRhCCAjIFCAAQsQMyBQgAELEDMgIIADIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyAggAMgUIABCxAzoHCAAQsAMQQzoPCAAQsQMQgwEQQxBGEIICOggIABCxAxCDAToGCAAQChAqOgsIABAKECoQRhCCAjoECAAQClDxriVYz9YlYOnbJWgEcAB4A4ABsAuIAf5JkgELMi0xLjUtMS4yLjaYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=psy-ab&ved=0ahUKEwjQ37fFlazsAhWMHHcKHblbA2sQ4dUDCA0&uact=5'
					    	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
					    	full_page = requests.get(EURO_RUB, headers=headers)
					    	soup = BeautifulSoup(full_page.content, 'html.parser')
					    	converte = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

					    	BTC_RUB = 'https://www.google.ru/search?newwindow=1&ei=TtCCX7XMC-n0qwHr1rWQAg&q=курс+биткоина&oq=курс+биткоина&gs_lcp=CgZwc3ktYWIQAzINCAAQsQMQgwEQRhCCAjICCAAyAggAMgUIABCxAzICCAAyAggAMgIIADICCAAyAggAMgIIADoHCAAQsQMQQzoECAAQQzoKCAAQsQMQgwEQQzoICAAQsQMQgwFQsi1Y18EtYI_DLWgBcAB4AYABrwWIAbUpkgEFNC01LjWYAQCgAQGqAQdnd3Mtd2l6sAEAwAEB&sclient=psy-ab&ved=0ahUKEwi1q_T3nKzsAhVp-ioKHWtrDSIQ4dUDCA0&uact=5'
					    	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
					    	full_page = requests.get(BTC_RUB, headers=headers)
					    	soup = BeautifulSoup(full_page.content, 'html.parser')
					    	convertb = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

					    	course1 = "\n💲Текущий курс💲"
					    	course2 = "\n💵Доллар - " + str(convertd[0].text) + "₽"
					    	course3 = "\n💷Евро - " + str(converte[0].text) + "₽"
					    	course4 = "\n₿Биткоин - " + str(convertb[0].text) + "₽"
					    	course = course1 + course2 + course3 + course4
					    	write_message(sender, course)





			    		else:
			    			fail = random.choice(fail_list_bot)
			    			write_message(sender, fail)













		    	elif event.from_user and event.message and event.message.get('text'):   #ЕСЛИ НАПИСАЛИ В ЛС
		    		reseived_message = event.message.get("text")
		    		sender = event.message.get("from_id")

		    		if reseived_message.lower() in hello_list_user:
		    			hello = random.choice(hello_list_bot)
		    			write_message2(sender, hello)

		    		elif reseived_message.lower() == "да" or reseived_message.lower() == "да." or reseived_message.lower() == "да," or reseived_message.lower() == "да!" or reseived_message.lower() == "да?": #ДА
		    			yes = random.choice(yes_list_bot)
		    			write_message2(sender, yes)

		    		elif reseived_message.lower() == "нет" or reseived_message.lower() == "нет." or reseived_message.lower() == "нет," or reseived_message.lower() == "нет!" or reseived_message.lower() == "нет?" or reseived_message.lower() == "не" or reseived_message.lower() == "не!" or reseived_message.lower() == "не?" or reseived_message.lower() == "не." or reseived_message.lower() == "не,": #НЕТ
		    			no = random.choice(no_list_bot)
		    			write_message2(sender, no)


		    		elif reseived_message.lower() == "эдвард" or reseived_message.lower() == "едвард" or reseived_message.lower() == "бот" or reseived_message.lower() == "edward":
		    			bot = random.choice(user_bot_list)
		    			write_message2(sender, bot)

		    		elif reseived_message.lower() in help_list_user: #список команд
		    			write_message2(sender, help_list_bot)

		    		elif reseived_message.lower() in joke_list_user: #анекдот
		    			f = open('joke.txt', 'r')
		    			joke = f.readlines()
		    			joke = random.choice(joke)
		    			write_message2(sender, joke)
		    			


		    		elif reseived_message.lower() in history_list_user: #ЖУТКАЯ ИСТОРИЯ
		    			story = random.choice(history_list_bot)
		    			write_message2(sender, story)

		    		elif reseived_message.lower() in cicat_list_user: #ЦИТАТА
		    			CITAT = 'https://citatnica.ru/citaty/samye-luchshie-tsitaty'
		    			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
		    			full_page = requests.get(CITAT, headers=headers)
		    			soup = BeautifulSoup(full_page.content, 'html.parser')
		    			convertd = soup.findAll("div", {"class": "su-note"})
		    			a = random.choice(convertd)
		    			a = a.text
		    			write_message2(sender, a)


		    		elif reseived_message.lower() == "шар" or reseived_message.lower() == "/шар":  #КОМАНДА ШАР
		    				write_message2(sender, "⚠Введите команду шар [фраза]")

		    		elif ("шар " in reseived_message.lower() or "/шар " in reseived_message.lower()) and not (reseived_message.lower() == "шар" or reseived_message.lower() == "/шар"):
		    			ball = random.choice(ball_list)
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
		    			infa = random.choice(infa_list_bot)
		    			write_message2(sender, infa)

		    		elif ("вероятность " in reseived_message.lower() or "инфа " in reseived_message.lower() or "/вероятность " in reseived_message.lower() or "/инфа " in reseived_message.lower()) and not (reseived_message.lower() == "вероятность" or reseived_message.lower() == "инфа" or reseived_message.lower() == "/инфа" or reseived_message.lower() == "/вероятность"):
		    			reseived_message_new = reseived_message.lower().split(" ", 1)
		    			index = reseived_message_new[1]
		    			index = list(index)
		    			if "?" in index or "." in index or "!" in index:
		    				index.pop()
		    				index_new = index
		    				index = ''.join(index_new)
		    				infa = random.choice(infa_list_bot)
		    				message = "Вероятность того, что " + index + ", равна: " + infa
		    				write_message2(sender, message)
		    			else:
		    				index = ''.join(index)
		    				infa = random.choice(infa_list_bot)
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
		    			infa = random.choice(infa_list_bot)
		    			write_message2(sender, infa)

		    		elif ("вероятность " in reseived_message.lower() or "инфа " in reseived_message.lower() or "/вероятность " in reseived_message.lower() or "/инфа " in reseived_message.lower()) and not (reseived_message.lower() == "вероятность" or reseived_message.lower() == "инфа" or reseived_message.lower() == "/инфа" or reseived_message.lower() == "/вероятность"):
		    			reseived_message_new = reseived_message.lower().split(" ", 1)
		    			index = reseived_message_new[1]
		    			index = list(index)
		    			if "?" in index or "." in index or "!" in index:
		    				index.pop()
		    				index_new = index
		    				index = ''.join(index_new)
		    				infa = random.choice(infa_list_bot)
		    				message = "Вероятность того, что " + index + ", равна: " + infa
		    				write_message2(sender, message)
		    			else:
		    				index = ''.join(index)
		    				infa = random.choice(infa_list_bot)
		    				message = "Вероятность того, что " + index + ", равна: " + infa
		    				write_message2(sender, message)




		    		elif reseived_message.lower() in id_list: #КОМАНДА АЙДИ
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

	    			elif reseived_message.lower() in mates_list_user:
		    			r = [True, False, False]
		    			r = random.choice(r)

		    			if r == True:
		    				r = "Сам " + reseived_message.lower()
		    				write_message2(sender, r)

		    			elif r == False:
			    			mat = random.choice(mates_list_bot)
			    			write_message2(sender, mat)

			    	elif reseived_message.lower() == "/vs":
			    		write_message2(sender, "⚠Введите команду /vs [противник] против [противник2]")



			    	elif "/vs " in reseived_message.lower():
			    		reseived_message_new = reseived_message.lower().split("/vs ", 1)
			    		reseived_message_new2 = reseived_message_new[1]
			    		index = reseived_message_new2.split(" против ", 1)
			    		index1 = index[0]
			    		index2 = index[1]
			    		damage1 = [15, 30, 35]
			    		damage2 = [40, 45, 50]
			    		damage_list = ["наносит урон", "наносит критический урон"]
			    		protection = "защитился(ась) от урона"
			    		protection_tf = [True, False, False]
			    		write_message2(sender, "Бой начинается!")
			    		vs = True
			    		life1 = 100
			    		life2 = 100

			    		while vs == True:

			    			score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
			    			write_message2(sender, score)
			    			damagelist = random.choice(damage_list)
			    			batle = index1 + " " + damagelist
			    			write_message2(sender, batle)
			    			protect = random.choice(protection_tf)

			    			if damagelist == "наносит урон" and protect == False:
			    				damage = random.choice(damage1)
			    				life = life2 - damage
			    				life2 = life
			    				score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"

			    				if life2 > 0:
			    					write_message2(sender, score)
			    					damagelist = random.choice(damage_list)
			    					batle = index2 + " " + damagelist
			    					write_message2(sender, batle)

			    					if damagelist == "наносит урон" and protect == False:
			    						damage = random.choice(damage1)
			    						life = life1 - damage
			    						life1 = life

			    						if life1 <= 0:
			    							vs = False
			    							life1 = 0
			    							score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
			    							write_message2(sender, score)
			    							win = "🏆" + index2 + " " + "победил!" + "🏆"
			    							write_message2(sender, win)
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
			    							write_message2(sender, score)
			    							win = "🏆" + index2 + " " + "победил!" + "🏆"
			    							write_message2(sender, win)
			    							life1 = 100
			    							life2 = 100

			    					elif protect == True:
			    						batle = index1 + " " + "защитился(ась) от урона"
			    						write_message2(sender, batle)

			    				elif life2 <= 0:
			    					vs = False
			    					life2 = 0
			    					score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
			    					write_message2(sender, score)
			    					win = "🏆" + index1 + " " + "победил!" + "🏆"
			    					write_message2(sender, win)
			    					life1 = 100
			    					life2 = 100

			    			elif damagelist == "наносит критический урон" and protect == False:
			    				damage = random.choice(damage2)
			    				life = life2 - damage
			    				life2 = life
			    				score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"

			    				if life2 > 0:
			    					write_message2(sender, score)
			    					damagelist = random.choice(damage_list)
			    					batle = index2 + " " + damagelist
			    					write_message2(sender, batle)

			    					if damagelist == "наносит урон" and protect == False:
			    						damage = random.choice(damage1)
			    						life = life1 - damage
			    						life1 = life

			    						if life1 <= 0:
			    							vs = False
			    							life1 = 0
			    							score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
			    							write_message2(sender, score)
			    							win = "🏆" + index2 + " " + "победил!" + "🏆"
			    							write_message2(sender, win)
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
			    							write_message2(sender, score)
			    							win = "🏆" + index2 + " " + "победил!" + "🏆"
			    							write_message2(sender, win)
			    							life1 = 100
			    							life2 = 100

			    					elif protect == True:
			    						batle = index1 + " " + "защитился(ась) от урона"
			    						write_message2(sender, batle)

			    				elif life2 <= 0:
			    					vs = False
			    					life2 = 0
			    					score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
			    					write_message2(sender, score)
			    					win = "🏆" + index1 + " " + "победил!" + "🏆"
			    					write_message2(sender, win)
			    					life1 = 100
			    					life2 = 100

			    			elif protect == True:
			    				batle = index2 + " " + "защитился(ась) от урона"
			    				write_message2(sender, batle)
			    				damagelist = random.choice(damage_list)
			    				batle = index2 + " " + damagelist
			    				protect = random.choice(protection_tf)
			    				write_message2(sender, batle)

			    				if damagelist == "наносит урон" and protect == False:
			    					damage = random.choice(damage1)
			    					life = life1 - damage
			    					life1 = life

			    					if life1 <= 0:
			    						vs = False
			    						life1 = 0
			    						score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
			    						write_message2(sender, score)
			    						win = "🏆" + index2 + " " + "победил!" + "🏆"
			    						write_message2(sender, win)
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
			    						write_message2(sender, score)
			    						win = "🏆" + index2 + " " + "победил!" + "🏆"
			    						write_message2(sender, win)
			    						life1 = 100
			    						life2 = 100

			    				elif protect == True:
			    					batle = index1 + " " + "защитился(ась) от урона"
			    					write_message2(sender, batle)

			    	elif "зачем" in reseived_message.lower() or "почему" in reseived_message.lower() or "нафига" in reseived_message.lower() or "нахрена" in reseived_message.lower() or "нахуя" in reseived_message.lower():
			    		why = random.choice(why_list_bot)
			    		write_message2(sender, why)

			    	elif "дела" in reseived_message.lower() and "как" in reseived_message.lower():
			    		case = random.choice(case_list_bot)
			    		write_message2(sender, case)
			    		d = [True, False, False]
			    		d = random.choice(d)

			    		if d == True:
			    			case = random.choice(case_list_bot2)
			    			write_message2(sender, case)

			    	elif ("нахуй" in reseived_message.lower() and "иди" in reseived_message.lower()) or "съебал" in reseived_message.lower() or "пиздуй" in reseived_message.lower() or "блядь" in reseived_message.lower() or "пиздец" in reseived_message.lower() \
			    		or "заебал" in reseived_message.lower():
			    		mat = random.choice(mates_list_bot)
			    		write_message2(sender, mat)

			    	elif "извини " in reseived_message.lower() or "прости" in reseived_message.lower() or reseived_message.lower() == "извини":
			    		sorry = random.choice(sorry_bot_list)
			    		write_message2(sender, sorry)

			    	elif reseived_message.lower() in answer_list_user:
			    		answer = random.choice(answer_list_bot)
			    		write_message2(sender, answer)

			    	elif reseived_message.lower() == "/курс":
			    		write_message2(sender, "⌛Подождите...")
			    		DOLLAR_RUB = 'https://www.google.ru/search?newwindow=1&ei=X8eCX9HEC8iHwPAPwdGcEA&q=курс+доллара&oq=курс+доллара&gs_lcp=CgZwc3ktYWIQAzINCAAQsQMQgwEQRhCCAjIFCAAQsQMyCAgAELEDEIMBMgUIABCxAzIFCAAQsQMyCAgAELEDEIMBMgUIABCxAzIFCAAQsQMyBQgAELEDMgUIABCxAzoCCABQ6gFYhhpguxtoAHAAeAGAAdUHiAG4FJIBBTUtMS4ymAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwiR8LC1lKzsAhXIAxAIHcEoBwIQ4dUDCA0&uact=5'
			    		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
			    		full_page = requests.get(DOLLAR_RUB, headers=headers)
			    		soup = BeautifulSoup(full_page.content, 'html.parser')
			    		convertd = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

			    		EURO_RUB = 'https://www.google.ru/search?newwindow=1&ei=jciCX5DlEYy53AO5t43YBg&q=курс+евро&oq=курс+евро&gs_lcp=CgZwc3ktYWIQAzIKCAAQsQMQRhCCAjIFCAAQsQMyBQgAELEDMgIIADIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyAggAMgUIABCxAzoHCAAQsAMQQzoPCAAQsQMQgwEQQxBGEIICOggIABCxAxCDAToGCAAQChAqOgsIABAKECoQRhCCAjoECAAQClDxriVYz9YlYOnbJWgEcAB4A4ABsAuIAf5JkgELMi0xLjUtMS4yLjaYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=psy-ab&ved=0ahUKEwjQ37fFlazsAhWMHHcKHblbA2sQ4dUDCA0&uact=5'
			    		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
			    		full_page = requests.get(EURO_RUB, headers=headers)
			    		soup = BeautifulSoup(full_page.content, 'html.parser')
			    		converte = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

			    		BTC_RUB = 'https://www.google.ru/search?newwindow=1&ei=TtCCX7XMC-n0qwHr1rWQAg&q=курс+биткоина&oq=курс+биткоина&gs_lcp=CgZwc3ktYWIQAzINCAAQsQMQgwEQRhCCAjICCAAyAggAMgUIABCxAzICCAAyAggAMgIIADICCAAyAggAMgIIADoHCAAQsQMQQzoECAAQQzoKCAAQsQMQgwEQQzoICAAQsQMQgwFQsi1Y18EtYI_DLWgBcAB4AYABrwWIAbUpkgEFNC01LjWYAQCgAQGqAQdnd3Mtd2l6sAEAwAEB&sclient=psy-ab&ved=0ahUKEwi1q_T3nKzsAhVp-ioKHWtrDSIQ4dUDCA0&uact=5'
			    		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.1.110 Yowser/2.5 Safari/537.36'}
			    		full_page = requests.get(BTC_RUB, headers=headers)
			    		soup = BeautifulSoup(full_page.content, 'html.parser')
			    		convertb = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

			    		course1 = "\n💲Текущий курс💲"
			    		course2 = "\n💵Доллар - " + str(convertd[0].text) + "₽"
			    		course3 = "\n💷Евро - " + str(converte[0].text) + "₽"
			    		course4 = "\n₿Биткоин - " + str(convertb[0].text) + "₽"
			    		course = course1 + course2 + course3 + course4
			    		write_message2(sender, course)

			    	elif reseived_message.lower() == "/covid" or reseived_message.lower() == "covid" or reseived_message.lower() == "коронавирус" or reseived_message.lower() == "/коронавирус" or reseived_message.lower() == "/covid19": #КОРОНАВИРУС
			    		
			    		try:

				    		res = api.get_stats()
				    		ru = api.filter_by_country("russia")
				    		write_message2(sender, "⚠Подождите...")
				    		cov0 = '''
				    		🦠Статистика случаев заражения коронавирусом🦠
				    		'''
				    		cov11 = "\n🌐В мире:"
				    		
				    		cov1 = "\n🤒" + "Заражений: " + str(res['confirmed'])
				    		cov2 = "\n☠" + "Смертей: " + str(res['deaths'])
				    		cov3 = "\n💊" + "Выздоровлений: " + str(res['recovered'])
				    		cov4 = "\n "
				    		cov5 = "\n🇷🇺В России:"
				    		cov6 = "\n🤒" + "Заражений: " + str(ru['confirmed'])
				    		cov7 = "\n☠" + "Смертей: " + str(ru['deaths'])
				    		cov8 = "\n💊" + "Выздоровлений: " + str(ru['recovered'])
				    		cov9 = '''

				    		⚠В случае, если в вашей местности зарегистрировано распространение COVID-19, соблюдайте простые меры предосторожности: держитесь на безопасной дистанции от окружающих, носите маску, хорошо проветривайте помещения, избегайте мест скопления людей, мойте руки и прикрывайте нос и рот сгибом локтя или салфеткой при кашле или чихании. Следите за рекомендациями для вашего населенного пункта и места работы. Беригите себя!
				    		'''
				    		cov = cov0 + cov11 + cov1 + cov2 + cov3 + cov4 + cov5 + cov6 + cov7 + cov8 + cov9

				    	except:

				    		write_message2(sender, "⚠Не удалось получить информацию.")

				    	else:

				    		write_message2(sender, cov)

		    		else:

		    			fail = random.choice(fail_list_bot)
		    			write_message2(sender, fail)

		

	except requests.exceptions.ReadTimeout:

		print("\n Переподключение к серверам ВК \n")
		time.sleep(3)

		

		

		






	

	

	

		

			