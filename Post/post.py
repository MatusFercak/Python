class Zasielka:

	def __init__(self, vaha, smerovacie_cislo, meno_odosielatela, meno_prijmatela, cislo_zasielky):
		self.__vaha = vaha 
		self.__smerovacie_cislo = smerovacie_cislo
		self.__meno_odosielatela = meno_odosielatela
		self.__meno_prijmatela = meno_prijmatela
		self.__cislo_zasielky = cislo_zasielky
		self.__stav = 'False'

	def __del__(self):
		del self
	def get_vaha(self):
		return self.__vaha
	def set_vaha(self, arg):
		self.__vaha = arg

	def get_smerovacie_cislo(self):
		return self.__smerovacie_cislo
	def set_smerovacie_cislo(self, arg):
		self.__smerovacie_cislo = arg

	def get_meno_odosielatela(self):
		return self.__meno_odosielatela
	def set_meno_odosielatela(self, arg):
		self.__meno_odosielatela = arg

	def get_meno_prijmatela(self):
		return self.__meno_prijmatela
	def set_meno_prijmatela(self, arg):
		 self.__meno_prijmatela = arg
	
	def get_stav(self):
		return self.__stav
	def set_stav(self, arg):
		self.__stav = arg

	def get_cislo_zasielky(self):
		return self.__cislo_zasielky
	def set_cislo_zasielky(self, arg):
		self.__cislo_zasielky = arg

	def __str__(self):
		row = '-'*25 + '-\n'
		vaha = f'Vaha: {self.__vaha} kg\n'
		smerovacie_cislo = f'Smerovacie cislo: {self.__smerovacie_cislo}\n'
		meno_odosielatela = f'Meno odosielatela: {self.__meno_odosielatela}\n'
		meno_prijmatela = f'Meno prijmatela: {self.__meno_prijmatela}\n'
		stav = 'Prevziate\n' if self.__stav == 'True' else 'Neprevziate\n'
		cislo_zasielky = f'Cislo zasielky: {self.__cislo_zasielky}\n'
		return row+vaha+smerovacie_cislo+meno_odosielatela+meno_prijmatela+'Stav: '+stav+cislo_zasielky+row


class Posta(Zasielka):
	zasielky = list()

	def __init__(self, nazov, vaha, smerovacie_cislo, meno_odosielatela, meno_prijmatela, cislo_zasielky):
		Zasielka.__init__(self, vaha, smerovacie_cislo, meno_odosielatela, meno_prijmatela, cislo_zasielky)
		self.__pobocka_posty = nazov


	def add_zasielku(self):
		lst = list()
		for i in Posta.zasielky:
			 lst.append(i[-2])
		if self.get_cislo_zasielky() in lst:
			print('--'*20 +'\nCislo zasielky je uz pouzite\n' + '--'*20)
			return -1
		self.zasielky.append([
			self.get_vaha(), 
			self.get_smerovacie_cislo(), 
			self.get_meno_odosielatela(),
		 	self.get_meno_prijmatela(),
		 	self.get_cislo_zasielky(),
		 	self.get_stav()
		 	])

	def del_zasielku(cislo):
		index = None
		for i in range(len(Posta.zasielky)):
			if Posta.zasielky[i][-2] == str(cislo):
				index = i
				pass
		if index != None:
			Posta.zasielky.pop(index)
		else:
			print('--'*20+'\nZasielka s danym cislom neexistuje\n'+'--'*20)
			return -1

	def get_zasielky():
		return Posta.zasielky

	def set(self, arg, index):
		lst = list()
		for i in Posta.zasielky:
			if i[-2] == self.get_cislo_zasielky():
			 	i[index] = str(arg)

	def set_Vaha(self, arg):
		self.set_vaha(str(arg))
		Posta.set(self, arg, 0)
		
	def set_Smerovacie_cislo(self, arg):
		self.set_smerovacie_cislo(str(arg))
		Posta.set(self, arg, 1)

	def set_Meno_odosielatela(self, arg):
		self.set_meno_odosielatela(arg)
		Posta.set(self, arg, 2)

	def set_Meno_prijmatela(self, arg):
		self.set_meno_prijmatela(arg)
		Posta.set(self, arg, 3)

	def set_Cislo_Zasielky(self, arg):
		self.set_cislo_zasielky(arg)
		Posta.set(self, arg, 4)

	def set_Stav_zasielky(self, arg):
		self.set_stav(arg)
		Posta.set(self, arg, 5)

	def sort_vaha():
		for i in range(len(Posta.zasielky)):
			for i in range(len(Posta.zasielky)-1):
				if int(Posta.zasielky[i][0]) > int(Posta.zasielky[i+1][0]):
					Posta.zasielky[i][0], Posta.zasielky[i+1][0]= Posta.zasielky[i+1][0], Posta.zasielky[i][0]

	def get_celkova_vaha():
		vaha = 0
		for i in Posta.zasielky:
			vaha += int(i[0])
		return vaha

	def get_all_meno(meno):
		lst = list()
		for i in Posta.zasielky:
			if i[-3] == meno:
				lst.append(i)
		print(lst)


	def save_data(file_path):
		open(file_path, 'w').close()
		my_file = open(file_path, 'a')

		for i in Posta.zasielky:
			my_file.write(f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]}\n')
		my_file.close()

	def load_data(file_path):
		load = 0
		for i in open(file_path, 'r').readlines():
			lst = i[:-1].split(',')
			lst_of = list()
			for obj in Posta.zasielky:
				lst_of.append(obj[-2])
				
			if lst[-2] in lst_of:
				print('Fail to loaded data.')
			else:
				print('Successfully loaded.')
				Posta.zasielky.append(lst)
				load += 1
		print('Loaded',load,'/',len(open(file_path, 'r').readlines()))

	

			 	


if __name__ == '__main__':
	zasielka_1 = Posta('KVP','20','04023','Matus Fercak','James Bond','1234')
	zasielka_2 = Posta('KVP','25','04023','Matus Fercak','James Bond','1235')
	zasielka_3 = Posta('KVP','15','04023','Matus Fercak','James Bond','3')

	

	# #print(zasielka_1.__str__())
	# zasielka_1.set_Vaha('15')
	# #print(zasielka_1.__str__())
	Posta.add_zasielku(zasielka_1)
	Posta.add_zasielku(zasielka_2)
	Posta.add_zasielku(zasielka_3)

	#Posta.save_data('save.txt')
	#Posta.load_data('load.txt')
	Posta.load_data('load.txt')

	#Posta.del_zasielku(1234)
	#Posta.del_zasielku(3434)
	Posta.get_all_meno('James Bond')
	#Posta.save_data('save.txt')
	
	# print(zasielka_3.__str__())


	# zasielka_1.set_Vaha('40')
	# zasielka_2.set_Vaha('350')
	
	# print(zasielka_1.__str__())
	# #Posta.add_zasielku(zasielka_1)
	
	# #print(Posta.get_zasielky())

	Posta.sort_vaha()
	print(Posta.get_celkova_vaha())

	
	print(Posta.get_zasielky())
	pass
	

