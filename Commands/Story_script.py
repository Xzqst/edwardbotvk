import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.keyboard import VkKeyboard, VkKeyboardColor #КЛАВИАТУРА
from vk_api.utils import get_random_id
import random
import sys
sys.path.insert(0, "Data/Config")
sys.path.insert(0, "Data")

import connection
import story_data as story

token=connection.token  #ТОКЕН ГРУППЫ
access_token = connection.access_token
group_id = connection.group_id

vk_session = VkApi(token = token)
vk_session2 = VkApi(token = access_token)
longpoll = VkBotLongPoll(vk_session, group_id)
longpollbot = True

keyboard = VkKeyboard(one_time=False, inline=True)
keyboard.add_button('Следующая история😱', color=VkKeyboardColor.NEGATIVE)

def write_message(sender, message):
	vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message, 'keyboard': keyboard.get_keyboard()})

def write_message2(sender, message):
	vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message, 'keyboard': keyboard.get_keyboard()})


def start(sender, send):
	message = random.choice(story.history_list_bot)
	if send == 1:
		write_message(sender, message)
	elif send == 0:
		write_message2(sender, message)
