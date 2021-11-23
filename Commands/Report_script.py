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


def start(sender, text, send, user, name, surname):
	try:
		text = text.split(" ", 1)
		text = text[1]
		message = f"📫Пользователь [id{str(user)}|{name} {surname}] отправил(а) сообщение! \n✉Текст сообщения: \n\n{text}"
		vk_session.method('messages.send', {'chat_id': 23, 'random_id': get_random_id(), 'message': message})
		write_message(sender, "📫Сообщение успешно доставлено администрации!", send)
	except:
		write_message(sender, "произошла неизвестная ошибка!", send)