import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id
import random
import sys
sys.path.insert(0, "Data/Config")
import connection

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

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
		if text == "погода":
			write_message(sender, "⚠Введите команду /погода [город]", send)

		else:
			config_dict = get_default_config()
			config_dict['language'] = 'ru'
			owm = OWM('e3536bf11667c154f01d2b3dc2620644', config_dict)
			mgr =  owm.weather_manager()

			text = text.lower().split(" ", 1)
			city = text[1]
			observation = mgr.weather_at_place(city)
			weather = observation.weather
			a = weather.detailed_status
			temp = weather.temperature('celsius')['temp']
			wind = observation.weather.wind()['speed']
			weather1 = '''
			🌥Погода🌥
			'''
			weathercity = f"\n🏛В городе сейчас {a}."
			cels = f"\n\n🌡Температура в городе {city} в данный момент приблизительно равна {str(temp)}° градусов."
			wind1 = "\n\n💨Скорость ветра в данный момент составляет приблизительно " + str(wind) + " м/с."
			message = f"{weather1}{weathercity}{cels}{wind1}"
			write_message(sender, "⌛Подождите...", send)
			write_message(sender, message, send)
	except:
		write_message(sender, "⚠Такого города не существует!", send)