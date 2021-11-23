
import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id
import random
import sys
import wikipedia
sys.path.insert(0, "Data/Config")
import connection
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
			if text == "вики" or text == "wiki":
				write_message(sender, "⚠Введите команду /вики [текст]", send)
			else:
				text = text.lower().split(" ", 1)
				index = text[1]
				write_message(sender, "⌛Подождите...", send)
				wikipedia.set_lang('ru')
				w = wikipedia.page(index)
				wiki = wikipedia.summary(index)
				count = len(wiki)
				if count > 300:
					url = w.url
					wiki = wiki[0:300] + "\n" + "Читать полностью:" + "\n" + url
				write_message(sender, wiki, send)
		except:
			write_message(sender, "⚠Не удалось найти информацию.", send)