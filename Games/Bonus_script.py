iduser = None

class Check: #Проверка на то, есть ли пользователь в базе.
	data_list = []
	def Checkdata(iduser):
		Check_user = False
		f = open('Bonus.txt', 'r')
		Check.data_list = f.readlines()
		if Check.data_list == []:
			f.close()
			return 0
		elif not Check.data_list == []:
			for s in Check.data_list:
				if s == iduser:
					Check_user = True
					f.close()
					return 1
			if Check_user == False:
				f.close()
				return 0

class Write: #Запись данных.
	def Writedata(iduser):
		f = open('Bonus.txt', 'r+')
		if Check.Checkdata(iduser) == 0:
			string = str(iduser) + '\n'
			Check.data_list.append(string)
			for data in Check.data_list:
				f.write(data)
			f.close()

