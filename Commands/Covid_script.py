import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id
import random
import sys

from covid.api import CovId19Data #КОРОНАВИРУС

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

def start(sender, text, send): #Получение информации о коронавирусе в ЛС
	try:
		res = api.get_stats()
		ru = api.filter_by_country("russia")
		write_message2(sender, "⚠Подождите...")
		cov0 = '''
		🦠Статистика случаев заражения коронавирусом🦠
		'''
		cov11 = "\n🌐В мире:"
		cov1 = "\n🤒" + "Заражений: " + str(res['confirmed'])
		cov2 = "\n☠" + "Смертей: " + str(res['deaths'])
		cov3 = "\n💊" + "Выздоровлений: " + str(res['recovered'])
		cov4 = "\n "
		cov5 = "\n🇷🇺В России:"
		cov6 = "\n🤒" + "Заражений: " + str(ru['confirmed'])
		cov7 = "\n☠" + "Смертей: " + str(ru['deaths'])
		cov8 = "\n💊" + "Выздоровлений: " + str(ru['recovered'])
		cov9 = '''
		⚠В случае, если в вашей местности зарегистрировано распространение COVID-19, соблюдайте простые меры предосторожности: держитесь на безопасной дистанции от окружающих, носите маску, хорошо проветривайте помещения, избегайте мест скопления людей, мойте руки и прикрывайте нос и рот сгибом локтя или салфеткой при кашле или чихании. Следите за рекомендациями для вашего населенного пункта и места работы. Беригите себя!
		'''
		cov = cov0 + cov11 + cov1 + cov2 + cov3 + cov4 + cov5 + cov6 + cov7 + cov8 + cov9
	except:
		write_message2(sender, "⚠Не удалось получить информацию.")
	else:
		write_message2(sender, cov)