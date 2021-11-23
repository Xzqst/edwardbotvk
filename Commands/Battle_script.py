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

class battle():
	def __init__(self, text, send, sender):
		self.text = text
		self.send = send
		self.sender = sender
		self.life1 = 100
		self.life2 = 100
		self.damage_list = ["наносит урон", "наносит критический урон"]
		self.damage = [20, 25, 30]
		self.critical_damage = [35, 40, 50]
		self.defender = [True, False, False, False]

	def fight(self):
		try:
			if self.text == "vs":
				write_message(self.sender, "⚠Введите команду /vs [противник] против [противник2]", self.send)

			else:
				text = self.text.split("vs ", 1)
				text = text[1].split(" против ", 1)
				oponent = text[0]
				oponent2 = text[1]
				a = True
				start = "⚔Бой начинается!⚔"
				write_message(self.sender, start, self.send)
				while a == True:
					if self.life1 <= 0:
						self.life1 = 0
						score = f"👤{oponent} [{str(self.life1)}]🆚[{str(self.life2)}] {oponent2}👤"
						write_message(self.sender, score, self.send)
						message = f"🏆{oponent2} победил!🏆"
						write_message(self.sender, message, self.send)
						break

					elif self.life2 <= 0:
						self.life2 = 0
						score = f"👤{oponent} [{str(self.life1)}]🆚[{str(self.life2)}] {oponent2}👤"
						write_message(self.sender, score, self.send)
						message = f"🏆{oponent} победил!🏆"
						write_message(self.sender, message, self.send)
						break

					else:
						score = f"👤{oponent} [{str(self.life1)}]🆚[{str(self.life2)}] {oponent2}👤"
						write_message(self.sender, score, self.send)
						damage_random = random.choice(self.damage_list)
						defender = random.choice(self.defender)

						if defender == False:
							if damage_random == self.damage_list[0]:
								message  = f"{oponent} {damage_random}"
								write_message(self.sender, message, self.send)
								damage = random.choice(self.damage)
								self.life2 -= damage

							elif damage_random == self.damage_list[1]:
								message  = f"{oponent} {damage_random}"
								write_message(self.sender, message, self.send)
								damage = random.choice(self.critical_damage)
								self.life2 -= damage
						elif defender == True:
							message  = f"{oponent} {damage_random}"
							write_message(self.sender, message, self.send)
							message = f"{oponent2} защитился(ась) от урона"
							write_message(self.sender, message, self.send)

						if self.life1 <= 0:
							self.life1 = 0
							score = f"👤{oponent} [{str(self.life1)}]🆚[{str(self.life2)}] {oponent2}👤"
							write_message(self.sender, score, self.send)
							message = f"🏆{oponent2} победил!🏆"
							write_message(self.sender, message, self.send)
							break

						elif self.life2 <= 0:
							self.life2 = 0
							score = f"👤{oponent} [{str(self.life1)}]🆚[{str(self.life2)}] {oponent2}👤"
							write_message(self.sender, score, self.send)
							message = f"🏆{oponent} победил!🏆"
							write_message(self.sender, message, self.send)
							break

						else:
							score = f"👤{oponent} [{str(self.life1)}]🆚[{str(self.life2)}] {oponent2}👤"
							write_message(self.sender, score, self.send)
							damage_random = random.choice(self.damage_list)
							defender = random.choice(self.defender)
							if defender == False:

								if damage_random == self.damage_list[0]:
									message  = f"{oponent2} {damage_random}"
									write_message(self.sender, message, self.send)
									damage = random.choice(self.damage)
									self.life1 -= damage

								elif damage_random == self.damage_list[1]:
									message  = f"{oponent2} {damage_random}"
									write_message(self.sender, message, self.send)
									damage = random.choice(self.critical_damage)
									self.life1 -= damage

							elif defender == True:
								message  = f"{oponent2} {damage_random}"
								write_message(self.sender, message, self.send)
								message = f"{oponent} защитился(ась) от урона"
								write_message(self.sender, message, self.send)

		except:
			write_message(self.sender, "⚠Произошла ошибка!", self.send)

def start(text, send, sender):
	a = battle(text, send, sender)
	a.fight()