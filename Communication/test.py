import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id

import random
import sys
sys.path.insert(0, "Data/Config")
import connection

from Data import answer_data as answer
from Data import words_data as data

token=connection.token  #ТОКЕН ГРУППЫ
access_token = connection.access_token
group_id = connection.group_id

vk_session = VkApi(token = token)
vk_session2 = VkApi(token = access_token)
longpoll = VkBotLongPoll(vk_session, group_id)
longpollbot = True

def write_message(sender, message):
	vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message})

def write_message2(sender, message):
	vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message})
id_mess = []
data = {
	"words": (),
	"answer": (),
}
def start(sender, send, text, id_message):
	data["words"].append(text)
	id_mess.append(id_message)
	id_message += 1 
