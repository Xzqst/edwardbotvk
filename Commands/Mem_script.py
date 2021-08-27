import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.keyboard import VkKeyboard, VkKeyboardColor #КЛАВИАТУРА
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

keyboard = VkKeyboard(one_time=False, inline=True)
keyboard.add_button('Следующий мем😹', color=VkKeyboardColor.PRIMARY)

def write_message(sender, message, send, mem_id):
	if send == 1:
		vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message, 'attachment': mem_id})
	elif send == 0:
		vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message, 'attachment': mem_id})

def write_message2(sender, message, send):
	if send == 1:
		vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message})
	elif send == 0:
		vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message})

def start(sender, text, send):
	if text == "мем" or "Следующий мем😹" in text:
		try:
			get = vk_session2.method('wall.get', {'owner_id': -197481314})
			post_list = []
			for post in get['items']:
				try:
					post = post['attachments'][0]
					if post['type'] == 'photo':
						post_list.append(post['photo']['id'])
				except:
					continue

			mem = random.choice(post_list)
			owner_id = -197481314
			mem_id = f"photo{str(owner_id)}_{str(mem)}"
			if send == 1:
				vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': " ", 'attachment': mem_id, 'keyboard': keyboard.get_keyboard()})
			elif send == 0:
				vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': " ", 'attachment': mem_id, 'keyboard': keyboard.get_keyboard()})
		except:
			write_message2(sender, "⚠Произошла ошибка!")

	else:
		try:
			text = text.lower().split(" ", 1)
			text = text[1]
			search = vk_session2.method('wall.search', {'owner_id': -166124324, 'query': text})
			post_list = []
			for post in search['items']:
				try:
					post = post['attachments'][0]
					if post['type'] == 'photo':
						post_list.append(post['photo']['id'])
				except:
					continue

			mem = random.choice(post_list)
			message = f"😹Найден мем по запросу \"{text}\""
			owner_id = -166124324
			mem_id = f"photo{str(owner_id)}_{str(mem)}"
			write_message(sender, message, send, mem_id)
		except:
			message = f"⚠По запросу \"{text}\" ничего не найдено."
			write_message2(sender, message, send)