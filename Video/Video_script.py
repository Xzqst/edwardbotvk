import random
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id

access_token = "914ae14206f01f8adaab0ea90b87b6199d09d8aac4ca4075e99e6aed7742ede4328ea6187ad5bb64011e4"
vk_session2 = VkApi(token = access_token)
title = None
types = None #ФОТО ИЛИ ВИДЕО
class videos:
	videos_url = None
	def search(title):
		search = vk_session2.method('video.search', {'q': title, 'sort': 2})
		v = search['items']

		b = random.choice(v)
		n1 = "video"
		n2 = b['id']
		n3 = b['owner_id']
		video1 = n1 + str(n3) + "_" + str(n2)

		b2 = random.choice(v)
		n2 = b2['id']
		n3 = b2['owner_id']
		video2 = n1 + str(n3) + "_" + str(n2)

		b3 = random.choice(v)
		n2 = b3['id']
		n3 = b3['owner_id']
		video3 = n1 + str(n3) + "_" + str(n2)

		b4 = random.choice(v)
		n2 = b4['id']
		n3 = b4['owner_id']
		video4 = n1 + str(n3) + "_" + str(n2)

		b5 = random.choice(v)
		n2 = b5['id']
		n3 = b5['owner_id']
		video5 = n1 + str(n3) + "_" + str(n2)

		videos.videos_url = video1 + "," + video2 + "," + video3 + "," + video4 + "," + video5