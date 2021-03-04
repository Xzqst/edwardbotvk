import random
from Data import data
from Data import Answer			

class filter: #Разбор сообщения пользователя
	one = False
	words = [] #Список слов пользователя.
	def analysis(message):
		for s in data.sym: #Удаление знаков препинания
			if s in message:
				message = message.replace(s, "")
		if " " in message: #Разбиение строки на отдельные слова.
			filter.one = False
			message = message.lower().split()
			for m in message:
				words.append(m)
		else:
			filter.one = True
			words.append(message.lower())
	
words = filter.words

class Hello: #Ответ на сообщение пользователя
	text_bot = [] #Сообщение бота для пользователя.
	sex = 0 # 1 - женский, 2 - мужской, 0 - неопределён.
	def write(words, sex):
		check = False
		count_list = []
		for word in words:
			if filter.one == True:
				if word in data.hello: #Приветствие
					check = True
					if sex == 2 or sex == 0: #Если пишет пользователь мужского  или неопределенного рода.
						answer = random.choice(Answer.Man.hello)
						Hello.text_bot.append(answer)
					elif sex == 1: #Если пишет пользователь женского рода.
						answer = random.choice(Answer.Women.hello)
						Hello.text_bot.append(answer)

				elif word in data.affront: #Оскорбление
					if sex == 2 or sex == 0: #Если пишет пользователь мужского  или неопределенного рода.
						check = True
						i = []
						o = "Сам " + word
						w = random.choice(Answer.Man.mate)
						i.append(o)
						i.append(w)
						w = random.choice(i)
						Hello.text_bot.append(w)
					elif sex == 1: #Если пишет пользователь женского рода.
						check = True
						i = []
						o = "Сама " + word
						w = random.choice(Answer.Women.mate)
						i.append(o)
						i.append(w)
						w = random.choice(i)
						Hello.text_bot.append(w)

				elif word in data.yes:
					check = True
					if sex == 2 or sex == 0: #Если пишет пользователь мужского  или неопределенного рода.
						answer = random.choice(Answer.Man.yes)
						Hello.text_bot.append(answer)
					elif sex == 1: #Если пишет пользователь женского рода.
						answer = random.choice(Answer.Women.yes)
						Hello.text_bot.append(answer)

				elif word in data.no:
					check = True
					if sex == 2 or sex == 0: #Если пишет пользователь мужского  или неопределенного рода.
						answer = random.choice(Answer.Man.no)
						Hello.text_bot.append(answer)
					elif sex == 1: #Если пишет пользователь женского рода.
						answer = random.choice(Answer.Women.no)
						Hello.text_bot.append(answer)


			elif filter.one == False:
				if word in data.hello: #Приветствие
					check = True
					count_list.append(word)
					n = count_list.count(word)
					if n == 1:
						if sex == 2 or sex == 0: #Если пишет пользователь мужского  или неопределенного рода.
							answer = random.choice(Answer.Man.hello)
							Hello.text_bot.append(answer)
						elif sex == 1: #Если пишет пользователь женского рода.
							answer = random.choice(Answer.Women.hello)
							Hello.text_bot.append(answer)

				elif word in data.question and "дела" in words:
					check = True
					count_list.append(word)
					n = count_list.count(word)
					if n == 1:
						if sex == 2 or sex == 0: #мужской или н.род
							w = random.choice(Answer.Man.affairs)
							Hello.text_bot.append(w)

						elif sex == 1: #женский род
							w = random.choice(Answer.Women.affairs)
							Hello.text_bot.append(w)

		if check == False:
			if sex == 2 or sex == 0:
				answer = random.choice(Answer.Man.misunderstanding)
				text_bot.append(answer)
			elif sex == 1:
				answer = random.choice(Answer.Women.misunderstanding)
				text_bot.append(answer)

text_bot = Hello.text_bot

class remove:
	def delete(words, text_bot):
		words.clear()
		text_bot.clear()


	
		