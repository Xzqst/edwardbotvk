import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id
import random
import sys
sys.path.insert(0, "Data/Config")
import connection

import pyshorteners #СОКРАЩЕННАЯ ССЫЛКА

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

def start(sender, text, send):
	try:
		if text == "сократи ссылку" or text == "s":
			write_message(sender, "⚠Введите команду /сократи ссылку [ссылка] или /s [ссылка]", send)
		else:
			text = text.lower().split(" ", 1)
			text = text[1]
			s = pyshorteners.Shortener()
			link = s.tinyurl.short(text)
			write_message(sender, "⌛Подождите...", send)
			write_message(sender, link, send)
	except:
		write_message(sender, "⚠Произошла ошибка!", send)