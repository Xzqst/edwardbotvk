import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id

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



Help_list = '''

📋Команды📋
📑 help - открыть весь список команд

🎉Развлекательные🎉
😱 Жуткая история
🤪 Анекдот
🔮 Шар | шар [текст]
📺 Видео [текст]
😹 Мем | мем [текст]
👉 Выбери [текст] или [текст]
💯 Инфа | инфа [текст]
👤 Кто | кто [текст]
👤 Кто кого | кто кому [текст]
📜 Список [текст]
⚔ Vs [противник] против [противник2]
🔫 Rr | Русская рулетка
👌  Щелчок

🦋Полезные🦋
🔎 Вики [текст]
🌥 Погода [город]
✂ Сократи ссылку [ссылка]
✏ Ed [название]
🔄 flip [текст]
🖥 Онлайн
🆔 id

📕Другие📕
📫Репорт [текст]

💬 С ботом можно поговорить.
Он вам обязательно ответит!

'''

def write_message(sender, message, send):
	if send == 1:
		vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message})
	elif send == 0:
		vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message})

def start(sender, send, name, user_id):
	try:
		message = f"😎[id{str(user_id)}|{name}], вот мои команды: {Help_list}"
		if send == 1:
			write_message(sender, message, send)
		elif send == 0:
			write_message(sender, message, send)
	except:
		write_message(sender, "⚠Произошла ошибка!", send)
