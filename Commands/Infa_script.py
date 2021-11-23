import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id
import random
import sys
sys.path.insert(0, "Data/Config")
import connection

token=connection.token  #ТОКЕН ГРУППЫ
access_token = connection.access_token
group_id = connection.group_id

vk_session = VkApi(token = token)
vk_session2 = VkApi(token = access_token)
longpoll = VkBotLongPoll(vk_session, group_id)
longpollbot = True

infa_list = [0, 1, 5, 10, 20, 25, 50, 60, 70, 80, 90, 100,
0.0000001, 0.1, 0.5, 99, 46, 69, 23, 44, 21, 12, 13, 99.9]

def write_message(sender, message, send):
	if send == 1:
		vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message})
	elif send == 0:
		vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message})

def start(sender, text, send):
	try:
		if text == "инфа" or text == "вероятность":
			infa = random.choice(infa_list)
			infa = f"{str(infa)}%"
			message = f"Вероятность равна: {infa}"
			write_message(sender, message, send)

		else:
			text = text.lower().split(" ", 1)
			text = text[1]
			infa = random.choice(infa_list)
			infa = f"{str(infa)}%"
			message = f"Вероятность того, что {text}, равна: {infa}"
			write_message(sender, message, send)
	except:
		write_message(sender, "⚠Произошла ошибка!", send)
