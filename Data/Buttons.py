import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor #КЛАВИАТУРА

keyboard_joke = VkKeyboard(one_time=False, inline=True)
keyboard_joke.add_button('Следующий анекдот😂', color=VkKeyboardColor.POSITIVE)

keyboard_history = VkKeyboard(one_time=False, inline=True)
keyboard_history.add_button('Следующая история😱', color=VkKeyboardColor.NEGATIVE)

keyboard_citat = VkKeyboard(one_time=False, inline=True)
keyboard_citat.add_button('Следующая цитата📕', color=VkKeyboardColor.POSITIVE)

keyboard_balance = VkKeyboard(one_time=False, inline=True)
keyboard_balance.add_button('Баланс💰', color=VkKeyboardColor.POSITIVE)

keyboard_gethelp = VkKeyboard(one_time=False, inline=True)
keyboard_gethelp.add_button('Получить финансовую помощь💰', color=VkKeyboardColor.PRIMARY)
keyboard_gethelp.add_button('Бонус🎁', color=VkKeyboardColor.PRIMARY)


keyboard = None
class Buttons_user:

	def write_button(sender, message): 
		vk_session.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(), 'keyboard': keyboard.get_keyboard()})

