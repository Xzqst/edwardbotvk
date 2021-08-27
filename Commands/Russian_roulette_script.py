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

def write_message(sender, message, send):
	if send == 1:
		vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message})
	elif send == 0:
		vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message})

def start(sender, text, send, user, message_id):
	if send == 1:
		write_message(sender, "Барабан револьера заряжен!", send)
		write_message(sender, "Крутим барабан...", send)

		if random.randint(0, 6) == 1:
			try:
				write_message(sender, "💥🔫Выстрел!", send)
				vk_session.method('messages.removeChatUser', {'chat_id': sender, 'user_id': user})
			except:
				vk_session.method('messages.edit', {'peer_id': 2000000000 + sender, 'message': "🔫Осечка! \n(Невозможно исключить админа из беседы)", 'message_id': message_id})
				write_message(sender, "🔫Осечка! \n(Невозможно исключить админа из беседы)", send)
		else:
			write_message(sender, "Осечка!", send)
	else:
		write_message(sender, "⚠Данная команда работает только в беседе!", send)