
iduser = None
balance = None

class Money: #Проверка на то, есть ли пользователь в базе.
	data_list = []
	balance = None
	Check_user = False
	def Check_and_write(iduser):
		f = open('E:/Python/EDWARD/Games/Data/Money.txt','r')
		Money.data_list = f.readlines()
		for s in Money.data_list:
			a = s.split()
			i = a[0]
			b = a[1]
			if i == str(iduser):
				Money.Check_user = True
				Money.balance = b
				f.close()
				return 1

		if Money.Check_user == False:
			start_balance = 50000
			Money.balance = start_balance
			f.close()
			f = open('E:/Python/EDWARD/Games/Data/Money.txt','r+')
			string = str(iduser) + " " + str(start_balance) + '\n'
			Money.data_list.append(string)
			for d in Money.data_list:
				f.write(d)

			f.close()
			return 0



