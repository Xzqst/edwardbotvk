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

def start(sender, text, send, user):
	if send == 0:
		message = "⚠Эта команда работает только в беседе!"
		write_message(sender, message, send)

	else:
		
		try:
			users_get = vk_session.method('messages.getConversationMembers', {'peer_id': 2000000000 + sender})
			users = []
			video = f"video110913168_456239174"

			check_admin = False
			try:
				for admin in users_get['items']:
					if admin['member_id'] == user:
						if admin['is_admin'] == True:
							check_admin = True
						else:
							check_admin = False
			except:
				write_message(sender, "⚠Данная команда доступна только для администраторов беседы!")

			if check_admin == True:
				for user_id in users_get['profiles']:
					id_get = user_id['id']
					users.append(id_get)

				count = len(users)
				print(users)
				print(count)

				if count >= 2:
					n = count / 2
					print(int(n))
					n2 = 0
					vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': " ", 'attachment': video})
					
					for user in users:
						try:
							vk_session.method('messages.removeChatUser', {'chat_id': sender, 'user_id': user})
							n2 += 1
							if n2 >= int(n):
								break
						except:
							continue
						
				elif count < 2:
					write_message(sender, "⚠Количество участников в беселе должно быть не меньше 2-х!", send)

			elif check_admin == False:
				write_message(sender, "⚠Данная команды доступна только администраторам беседы!", send)

		except:
			write_message(sender, "⚠Для этой команды нужно назначить бота администратором в беседе!", send)
