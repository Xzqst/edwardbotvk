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


def start(sender, text, send):
	try:
		if text == "видео":
			write_message(sender, "⚠Введите команду /видео [текст]", send)
		else:
			text = text.split(" ", 1)
			text = text[1]
			video = vk_session2.method('video.search', {'q': text, 'sort': 2})
			video_items = video['items']
			n = 0
			videos = []
			while n <= 6:
				video = random.choice(video_items)
				media_id = video['id']
				owner_id = video['owner_id']
				url = f"video{str(owner_id)}_{str(media_id)}"
				if not url in videos:
					videos.append(url)
					n += 1

			video = f"{videos[0]},{videos[1]},{videos[2]},{videos[3]},{videos[4]}"
			message = f"📺Найдено видео по запросу \"{text}\""

			if send == 1:
				vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message, 'attachment': video})
			elif send == 0:
				vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message, 'attachment': video})
			videos.clear()
	except:
		write_message(sender, "⚠Произошла ошибка!", send)