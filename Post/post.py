import json


class Package:
	def __init__(self, address, weight, number):
		if type(address) not in [str] or len(address) <= 0:
			raise ValueError('Invalid input! The Address must be a string with lenght more then 0.')
		if type(weight) not in [int] or weight <= 0:
			raise ValueError('Invalid input! The Weight must be a intiger and greater the 0.')
		if type(number) not in [int] or len(str(number)) != 4:
			raise ValueError('invalid input! The Number must be a intiger of 4 digits.')

		self.__address = address
		self.__weight = weight
		self.__number = number


	def __str__(self):
		st = f'{self.__number}:'
		st += f'{self.__address}'
		return st + f'({self.__weight})'


	def __eq__(self, other):
		return self.__number == other.__number


	def change_address(self, address):
		self.__address = address


	def get_number(self):
		return self.__number


	def get_weight(self):
		return self.__weight


	def get_address(self):
		return self.__address


class Post(Package):
	packages = []

	def __init__(self):
		pass


	def add_package(self, package):
		list_of_numbers = [package.get_number() for package in self.packages]
		if package.get_number() in list_of_numbers:
			print(f'Invalid number of package: {package.get_number()} is allready in use.')
			return
		self.packages.append(package)


	def remove_package(self, package):
		list_of_numbers = [package.get_number() for package in self.packages]
		if package.get_number() in list_of_numbers:
			self.packages.remove(package)
		else:
			print(f'Invalid number of package: {package.get_number()} is not in use.')


	def change_address_by_number(self, number, address):
		for package in self.packages:
			if package.get_number() == number:
				package.change_address(address)
				return
		print(f'Package with number: {number} do not exist.')


	def show_packages(self):
		packages = list()
		for package in self.packages:
			packages.append(str(package))
		return packages


	def sort_by_weight(self):
		packages = self.packages.copy()
		for i in range(len(packages) - 1):
			for j in range(0, len(packages) - i - 1):
				if packages[j].get_weight() > packages[j + 1].get_weight():
					packages[j],packages[j + 1] = packages[j + 1],packages[j]

		sorted_packages = list()	
		for package in packages:
			sorted_packages.append(str(package))

		return sorted_packages


	def sort_by_address(self):
		packages = self.packages.copy()
		for i in range(len(packages) - 1):
			for j in range(0, len(packages) - i - 1):
				if packages[j].get_address() > packages[j + 1].get_address():
					packages[j],packages[j + 1] = packages[j + 1],packages[j]

		sorted_packages = list()
		for package in packages:
			sorted_packages.append(str(package))

		return sorted_packages


	def get_package_by_address(self, address):
		packages_by_address = list()
		for package in self.packages:
			if package.get_address() == address:
				packages_by_address.append(str(package))

		return packages_by_address

	def save_packages(self):
		file = open('save.json','w')

		data = {}
		data['Packages'] = []
		for package in self.packages:
			data['Packages'].append({
				'address': package.get_address(),
				'weight': package.get_weight(),
				'number': package.get_number()
				}) 

		file.write(json.dumps(data,indent = 4))
		file.close()


	def load_packages(self):
		file = open('load.json','r')

		data = json.load(file)
		for package in data['Packages']:
			self.add_package(Package(package['address'], package['weight'], package['number']))


	def get_whole_weight(self):
		weight = 0
		for package in self.packages:
			weight += package.get_weight()

		return weight












def main():
	post_1 = Post()
	# package_1 = Package('Bosice', 20, 2341)
	# package_2 = Package('Kosice', 30, 2841)
	# package_3 = Package('Zosice', 10, 2443)
	# package_4 = Package('Aosice', 14, 2451)


	# post_1.add_package(package_1)
	# post_1.add_package(package_2)
	# post_1.add_package(package_3)
	# post_1.add_package(package_4)


	# post_1.remove_package(package_2)
	# post_1.remove_package(package_2)

		
	# print(post_1.sort_by_weight())
	# print(post_1.sort_by_address())
	

	# package_1.change_address('Presov')
	# post_1.change_address_by_number(2341, 'Blava')
	# print(post_1.get_package_by_address('Blava'))


	# print(package_1)
	# print(package_1 == package_2) 


	post_1.save_packages()
	post_1.load_packages()
	print(post_1.show_packages())
	print(post_1.get_whole_weight())
	pass

if __name__ == '__main__':
	main()
