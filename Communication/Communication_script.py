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

def write_message(sender, message, send):
	if send == 1:
		vk_session.method('messages.send', {'chat_id': sender, 'random_id': get_random_id(), 'message': message})
	elif send == 0:
		vk_session.method('messages.send', {'user_id': sender, 'random_id': get_random_id(), 'message': message})

symbols = ["?", "!", "/", ",", "+", "-", "=", "_", "#", ";", ":", "&", "*", ")", "(", "№", "[", "]", "'", "|", "%", "<", ">", ".", "~"]

class Communication():
	def __init__(self, text, sender, send, sex):
		self.text = text
		self.sender = sender
		self.send = send
		self.sex = sex
		self.text_new = []
		self.check = False
		self.speaking = None
		self.exit = False

	def filter(self):      
		text = list(self.text)
		for b in text:
			if not b in symbols:
				self.text_new.append(b)

		t = "".join(self.text_new)
		self.text_new = t.lower().split()

	def analysis(self):
		check = False
		for t in self.text_new:
			if t in data.bad["offense"]:
				check = True
			elif t in data.bad["sending"]:
				check = True
			elif t in data.bad["sending2"]:
				check = True
		if check == False:
			self.speaking = "Positive"
		elif check == True:
			self.speaking = "Negative"
		check = False

	def answer(self):
		if self.speaking == "Positive":
			print("позитив")
			for t in self.text_new:
				if self.exit == False:
					class Positive:
						print(self.text_new)
						print(t)
						class Hello: #ПРИВЕТСТВИЕ
							if t in data.hello:
								if self.check == False:
									self.check = True

									if self.sex == 2: #Мужской род
										message = random.choice(answer.hello["man"])
										write_message(self.sender, message, self.send)
										self.exit = True
									else:
										message = random.choice(answer.hello["woman"])
										write_message(self.sender, message, self.send)
										self.exit = True

						class Affairs: #КАК ДЕЛА
							if t in data.affairs and ("дела" in self.text_new or "делишки" in self.text_new):
								if self.check == False:
									self.check = True

									if self.sex == 2: #Мужской род
										message = random.choice(answer.affairs)
										write_message(self.sender, message, self.send)
										self.exit = True
									else:
										message = random.choice(answer.affairs)
										write_message(self.sender, message, self.send)
										self.exit = True

						class What_do: #ЧТО ДЕЛАЕШЬ
							if t in data.what_do["do"]:
								if self.check == False:
									self.check = True
									for s in self.text_new:
										if s in data.what_do["what"]:
											if self.sex == 2: #Мужской род
												message = random.choice(answer.what_do)
												write_message(self.sender, message, self.send)
												self.exit = True
											else:
												message = random.choice(answer.what_do)
												write_message(self.sender, message, self.send)
												self.exit = True
						class Question: #ВОПРОС
							if t in data.question:
								if self.check == False:
									self.check = True

									if self.sex == 2: #Мужской род
										message = random.choice(answer.question["man"])
										write_message(self.sender, message, self.send)
										self.exit = True
									else:
										message = random.choice(answer.question["woman"])
										write_message(self.sender, message, self.send)
										self.exit = True
				else:
					break

			class Misunderstanding: #Непонимание
				if self.check == False:
					if self.sex == 2: #Мужской род
						message = random.choice(answer.misunderstanding["man"])
						write_message(self.sender, message, self.send)
						self.exit = True
					else:
						message = random.choice(answer.misunderstanding["woman"])
						write_message(self.sender, message, self.send)
						self.exit = True

		elif self.speaking == "Negative":
			print("негатив")
			for t in self.text_new:
				if self.exit == False:
					class Negative:
						class Sending:
							if t in data.bad["sending"]:
								if self.check == False:
									self.check = True
									for s in self.text_new:
										if s in data.bad["sending2"]:
											if self.sex == 2: #Мужской род
												message = random.choice(answer.sending["man"])
												write_message(self.sender, message, self.send)
												self.exit = True
											else:
												message = random.choice(answer.sending["woman"])
												write_message(self.sender, message, self.send)
												self.exit = True

							if self.check == False:
								if self.sex == 2: #Мужской род
									message = random.choice(answer.negative["man"])
									write_message(self.sender, message, self.send)
									self.exit = True
								else:
									message = random.choice(answer.negative["woman"])
									write_message(self.sender, message, self.send)
									self.exit = True


def start(text, sender, send, sex):
	s = Communication(text, sender, send, sex)
	s.filter()
	s.analysis()
	s.answer()


