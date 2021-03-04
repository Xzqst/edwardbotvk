import vk_api
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent
from vk_api.utils import get_random_id


def user(sender, reseived_message):
	reseived_message_new = reseived_message.lower().split("/vs ", 1)
	reseived_message_new2 = reseived_message_new[1]
	index = reseived_message_new2.split(" против ", 1)
	index1 = index[0]
	index2 = index[1]
	damage1 = [15, 30, 35]
	damage2 = [40, 45, 50]
	damage_list = ["🥊наносит урон", "🔪наносит критический урон"]
	protection = "🛡защитился(ась) от урона"
	protection_tf = [True, False, False]
	write_message2(sender, "⚔Бой начинается!")
	vs = True
	life1 = 100
	life2 = 100
	while vs == True:
		score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
		write_message2(sender, score)
		damagelist = random.choice(damage_list)
		batle = index1 + " " + damagelist
		write_message2(sender, batle)
		protect = random.choice(protection_tf)

		if damagelist == "🥊наносит урон" and protect == False:
			damage = random.choice(damage1)
			life = life2 - damage
			life2 = life
			score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"

			if life2 > 0:
				write_message2(sender, score)
				damagelist = random.choice(damage_list)
				batle = index2 + " " + damagelist
				write_message2(sender, batle)

				if damagelist == "🥊наносит урон" and protect == False:
					damage = random.choice(damage1)
					life = life1 - damage
					life1 = life

					if life1 <= 0:
						vs = False
						life1 = 0
						score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
						write_message2(sender, score)
						win = "🏆" + index2 + " " + "победил!" + "🏆"
						write_message2(sender, win)
						life1 = 100
						life2 = 100

				elif damagelist == "🔪наносит критический урон" and protect == False:
					damage = random.choice(damage2)
					life = life1 - damage
					life1 = life

					if life1 <= 0:
						vs = False
						life1 = 0
						score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
						write_message2(sender, score)
						win = "🏆" + index2 + " " + "победил!" + "🏆"
						write_message2(sender, win)
						life1 = 100
						life2 = 100

				elif protect == True:
					batle = index1 + " " + "🛡защитился(ась) от урона"
					write_message2(sender, batle)

			elif life2 <= 0:
				vs = False
				life2 = 0
				score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				write_message2(sender, score)
				win = "🏆" + index1 + " " + "победил!" + "🏆"
				write_message2(sender, win)
				life1 = 100
				life2 = 100

		elif damagelist == "🔪наносит критический урон" and protect == False:
			damage = random.choice(damage2)
			life = life2 - damage
			life2 = life
			score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"

			if life2 > 0:
				write_message2(sender, score)
				damagelist = random.choice(damage_list)
				batle = index2 + " " + damagelist
				write_message2(sender, batle)

				if damagelist == "🥊наносит урон" and protect == False:
					damage = random.choice(damage1)
					life = life1 - damage
					life1 = life

					if life1 <= 0:
						vs = False
						life1 = 0
						score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
						write_message2(sender, score)
						win = "🏆" + index2 + " " + "победил!" + "🏆"
						write_message2(sender, win)
						life1 = 100
						life2 = 100

				elif damagelist == "🔪наносит критический урон" and protect == False:
					damage = random.choice(damage2)
					life = life1 - damage
					life1 = life

					if life1 <= 0:
						vs = False
						life1 = 0
						score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
						write_message2(sender, score)
						win = "🏆" + index2 + " " + "победил!" + "🏆"
						write_message2(sender, win)
						life1 = 100
						life2 = 100

				elif protect == True:
					batle = index1 + " " + "🛡защитился(ась) от урона"
					write_message2(sender, batle)

			elif life2 <= 0:
				vs = False
				life2 = 0
				score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
				write_message2(sender, score)
				win = "🏆" + index1 + " " + "победил!" + "🏆"
				write_message2(sender, win)
				life1 = 100
				life2 = 100

		elif protect == True:
			batle = index2 + " " + "🛡защитился(ась) от урона"
			write_message2(sender, batle)
			damagelist = random.choice(damage_list)
			batle = index2 + " " + damagelist
			protect = random.choice(protection_tf)
			write_message2(sender, batle)

			if damagelist == "🥊наносит урон" and protect == False:
				damage = random.choice(damage1)
				life = life1 - damage
				life1 = life

				if life1 <= 0:
					vs = False
					life1 = 0
					score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
					write_message2(sender, score)
					win = "🏆" + index2 + " " + "победил!" + "🏆"
					write_message2(sender, win)
					life1 = 100
					life2 = 100

			elif damagelist == "🔪наносит критический урон" and protect == False:
				damage = random.choice(damage2)
				life = life1 - damage
				life1 = life

				if life1 <= 0:
					vs = False
					life1 = 0
					score = "👤" + index1 + " " + "[" + str(life1) + "]" + "🆚" + "[" + str(life2) + "]" + " " + index2 + "👤"
					write_message2(sender, score)
					win = "🏆" + index2 + " " + "победил!" + "🏆"
					write_message2(sender, win)
					life1 = 100
					life2 = 100

			elif protect == True:
				batle = index1 + " " + "🛡защитился(ась) от урона"
				write_message2(sender, batle)