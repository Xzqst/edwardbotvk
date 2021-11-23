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
		if text[0:3] == "кто" and not ("кого" in text or "кому" in text):
			if send == 0:
				write_message(sender, "⚠Эта команда работает только в беседе!", send)
			else:
				users_get = vk_session.method('messages.getConversationMembers', {'peer_id': 2000000000 + sender})
				users = []
				answer = ["Я считаю, что это", "По моему скромному мнению, это", "Это явно", "Мне сказали, что это", "100% это"]
				for name_get in users_get['profiles']:
					name = name_get['first_name']
					surname = name_get['last_name']
					id_get = name_get['id']

					result = f"{str(id_get)} {name} {surname}"
					users.append(result)
				get = random.choice(users)
				get = get.split(" ", 1)
				user_id = get[0]
				name = get[1]
				r = random.choice(answer)
				message = f"{r} [id{str(user_id)}|{name}]"
				write_message(sender, message, send)
				users.clear()

		elif text[0:8] == "кто кого" or text[0:8] == "кто кому":
			if text == "кто кого":
				write_message(sender, "⚠Введите команду /кто кого [текст]", send)

			elif text == "кто кому":
				write_message(sender, "⚠Введите команду /кто кому [текст]", send)

			else:	
				if send == 0:
					write_message(sender, "⚠Эта команда работает только в беседе!", send)
				else:
					if text[0:8] == "кто кого":
						text = text.lower().split("кого ", 1)
					elif text[0:8] == "кто кому":
						text = text.lower().split("кому ", 1)
				

				text = text[1]
				users_get = vk_session.method('messages.getConversationMembers', {'peer_id': 2000000000 + sender})
				users = []
				for name_get in users_get['profiles']:
					name = name_get['first_name']
					surname = name_get['last_name']
					id_get = name_get['id']
					result = f"{str(id_get)} {name} {surname}"
					users.append(result)

				n = 0
				users2 = []
				count = len(users)
				if count >= 2:
					while n < 2:
						get = random.choice(users)
						get = get.split(" ", 1)
						user_id = get[0]
						name = get[1]
						message = f"[id{str(user_id)}|{name}]"
						if message not in users2:
							users2.append(message)
							n += 1

					message = f"{users2[0]} {text} {users2[1]}"
					write_message(sender, message, send)
					users = []
					users2 = []
					n = 0
				else:
					message = "⚠В беседе количество участников должно быть не меньше, чем 2!"
					write_message(sender, message, send)
					users = []
					users2 = []
					n = 0


		elif text[0:6] == "список":
			if text == "список":
				write_message(sender, "⚠Введите команду /список [текст]", send)
			else:
				if send == 0:
					write_message(sender, "⚠Эта команда работает только в беседе!", send)

				text2 = text.lower().split(" ", 1)
				text2 = text2[1]
				users_get = vk_session.method('messages.getConversationMembers', {'peer_id': 2000000000 + sender})
				users = []
				users2 = []
				n = 0
				for name_get in users_get['profiles']:
					name = name_get['first_name']
					surname = name_get['last_name']
					id_get = name_get['id']
					result = f"{str(id_get)} {name} {surname}"
					users.append(result)
				while n <= 4:
					get = random.choice(users)
					get = get.split(" ", 1)
					user_id = get[0]
					name = get[1]
					message = f"[id{str(user_id)}|{name}]"
					if message not in users2:
						users2.append(message)
					n += 1
				users.clear()
				for user in users2:
					user = f"{user}\n"
					users.append(user)
				users = ''.join(users)
				message = f"📜Список \"{text2}\": \n\n{users}"
				write_message(sender, message, send)
				users = []
				users2 = []
				n = 0

		elif text == "онлайн":
			if send == 0:
				write_message(sender, "⚠Эта команда работает только в беседе!", send)

			users_get = vk_session.method('messages.getConversationMembers', {'peer_id': 2000000000 + sender})

			users = []
			n = 0

			for name_get in users_get['profiles']:
				name = name_get['first_name']
				surname = name_get['last_name']
				id_get = name_get['id']
				sym = None
				if name_get['online'] == 1:
					try:
						online = name_get['online_mobile']
						result = f"\n📱 [id{str(id_get)}|{name} {surname}] через приложение"
						users.append(result)
						n += 1

					except:
						result = f"\n🖥 [id{str(id_get)}|{name} {surname}] через сайт"
						users.append(result)
						n += 1

			users = ''.join(users)
			message = f"Онлайн в беседе ({n} чел.): \n\n{users}"
			write_message(sender, message, send)
			users = []
			n = 0




	except:
		if send == 1:
			write_message(sender, "⚠Для этой команды нужно назначить бота администратором в беседе!", send)


	