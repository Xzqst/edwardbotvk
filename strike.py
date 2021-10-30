import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id
from threading import Thread # Многопоточность
import requests

token="b2404bfb9a2e571486737e966f628e5faef38be2a82f763e9398ec6563db0aa5a64097133e1ec6bcef3b9"  #ТОКЕН ГРУППЫ
group_id = 200012156
vk_session = VkApi(token = token)
longpoll = VkBotLongPoll(vk_session, group_id)
longpollbot = True

helps = '''
🖥КОМАНДЫ🖥

📕 /help - команды
💣 /spam - спам атака в беседе
🔫 /spamuser [айди пользователя] - спам атака на пользователя
✏  /ed [текст]- изменить текст сообщения
🆔 /id - узнать свой айди
🆔 /ids - узнать айди беседы


'''

message_strike = "Спам атака"

help_list = ("команды", "хелп", "help", "покажи команды", "command", "команда", "начать", "start")

def write_message(sender, message, send):
	if send == 1:
		vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message})
	elif send == 0:
		vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message})

def execute(event): #Выполнение команд в БЕСЕДЕ
	
	reseived_message = event.message.get("text")
	sender = event.chat_id
	send = 1

	if reseived_message.lower()[0] == "/":
		user = event.message.get("from_id")
		id_message = event.message.get("conversation_message_id")
		reseived_message_new = reseived_message.lower().split("/", 1)
		text = reseived_message_new[1]
		get_user = vk_session.method('users.get', {'user_ids': user, 'fields': "sex"})
		name = get_user[0]["first_name"]

		if not user == 278339864:
			vk_session.method('messages.send', {'chat_id': 146, 'random_id': get_random_id(), 'message': "Кто-то написал в беседе!"})

		if text in help_list: #ВСЕ КОМАНДЫ
			try:
				write_message(sender, helps, send)
			except:
				write_message(sender, "⚠Ошибка!", send)

		elif text == "spam":
			try:
				n = 0
				while n <= 300:
					global message_strike
					message_strike = message_strike
					write_message(sender, message_strike, send)
					n+=1
			except:
				write_message(sender, "⚠Ошибка!", send)

		elif text[0:8] == "spamuser":
			try:
				text = text.lower().split(" ", 1)
				index = text[1]
				n = 0
				write_message(sender, "Спам атака началась!", send)
				while n <= 300:
					#global message_strike
					message_strike = message_strike
					write_message(int(index), message_strike, 0)
					n+=1
			except:
				write_message(sender, "⚠Неудалось провести спам атаку(", send)

		elif text[0:2] == "ed":
			try:
				text = text.lower().split(" ", 1)
				text = text[1]
				message_strike = text
				write_message(sender, "✅Текст успешно изменен!", send)
			except:
				write_message(sender, "⚠Ошибка!", send)

		elif text == "ids":
			messages = f"🆔Айди беседы: {str(sender)}"
			write_message(sender, messages, send)

		elif text == "id":
			messages = f"{name}, ваш 🆔: {str(user)}"


		else:
			write_message(sender, "⚠Такой команды нет!", send)

	else: #ВЗАИМОДЕЙСТВИЕ С КНОПКАМИ
		if "Следующий мем😹" in reseived_message: #МЕМ
			mem.start(sender, reseived_message, send)

		else:
			button.start(sender, send, reseived_message)

def execute2(event): #Выполнение команд в ЛС
	text = event.message.get("text")
	sender = event.message.get("from_id")
	id_message = event.message.get("id")
	get_user = vk_session.method('users.get', {'user_ids': sender, 'fields': "sex"})
	name = get_user[0]["first_name"]
	send = 0

	if text in help_list: #ВСЕ КОМАНДЫ
			try:
				write_message(sender, helps, send)
			except:
				write_message(sender, "⚠Ошибка!", send)

	elif text == "/spam":
		try:
			write_message(sender, "⚠Данная команда работает только в беседе")
		except:
			write_message(sender, "⚠Ошибка!", send)

	elif text[0:9] == "/spamuser":
		try:
			text = text.lower().split(" ", 1)
			index = text[1]
			n = 0
			write_message(sender, "Спам атака началась!", send)
			while n <= 300:
				global message_strike
				#message_strike = message_strike
				write_message(index, message_strike, send)
				n+=1
		except:
			write_message(sender, "⚠Неудалось провести спам атаку(", send)

	elif text[0:3] == "/ed":
		try:
			text = text.lower().split(" ", 1)
			text = text[1]
			message_strike = text
			write_message(sender, "✅Текст успешно изменен!", send)
		except:
			write_message(sender, "⚠Ошибка!", send)

	elif text == "/ids":
		write_message(sender, "⚠Данная команда работает только в беседе!", send)

	elif text == "/id":
		messages = f"{name}, ваш 🆔: {str(sender)}"

	else:
		write_message(sender, "⚠Такой команды нет!", send)
		
while longpollbot:
	try:
		status = vk_session.method('groups.getOnlineStatus', {'group_id': group_id})
		if not status['status'] == "online":
			vk_session.method('groups.enableOnline', {'group_id': group_id})
		for event in longpoll.listen():
			try:
			    if event.type == VkBotEventType.MESSAGE_NEW: #Кто-то отправил боту сообщение
			    	if event.from_chat and event.message and event.message.get('text'):  #ЕСЛИ НАПИСАЛИ В ЧАТЕ
			    		Thread(target = execute, args = (event, ), daemon = True).start()

			    	elif event.from_user and event.message and event.message.get('text'):   #ЕСЛИ НАПИСАЛИ В ЛС
			    		Thread(target = execute2, args = (event, ), daemon = True).start()

			    elif event.type == VkBotEventType.GROUP_JOIN: #Если пользователь вступил в группу
			    	sender = event.object.user_id
			    	send = 0
			    	get_user = vk_session.method('users.get', {'user_ids': sender, 'fields': "sex"})
			    	sex = get_user[0]["sex"]
			    	name = get_user[0]["first_name"]
			    	if sex == 2:
			    		message = "👋Привет! Я рад, что ты вступил в группу!😄"
			    	else:
			    		message = "👋Привет! Я рад, что ты вступила в группу!😄"
			    	write_message(sender, message, send)
			    	message = f"{name}, вот мои команды: \n{helps}"
			    	write_message(sender, message, send)
			except:
				print("Ошибка!")    

	except requests.exceptions.ReadTimeout:
		print("\n Переподключение к серверам ВК \n")
		time.sleep(3)