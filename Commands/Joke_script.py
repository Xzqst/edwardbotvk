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

keyboard_joke = VkKeyboard(one_time=False, inline=True)
keyboard_joke.add_button('Следующий анекдот😂', color=VkKeyboardColor.POSITIVE)

def write_message(sender, message, keyboard, send):
	if send == 1:
		vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message, 'keyboard': keyboard.get_keyboard()})
	elif send == 0:
		vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message, 'keyboard': keyboard.get_keyboard()})


def start(sender, send):
	f = open('Data/Jokes/joke.txt','r')
	joke = f.readlines()
	message = random.choice(joke)
	write_message(sender, message, keyboard_joke, send)
	f.close()