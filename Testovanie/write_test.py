# application helping me with genereting 'test sources' for testing 
#
#
import random 

def test_for_String_ends_with(file_write, file_read):
	# dlete previous text
	open(file_write,'w').close()

	# open files for writing or reading
	write_file = open(file_write, 'a', encoding='UTF-8')
	read_file = open(file_read, 'r', encoding='UTF-8')

	# just read lines 
	# 'i' ; one line in text file
	for i in read_file:
		lst = i[:-1].split()
		# elem is one word from line
		for elem in lst:
			if elem[-1] == '.':
				elem = elem[:-1]

			if random.random() <= 0.7:
				part_of_elem = elem[random.randint(1, len(elem)-1):]
				write_file.write(f'{elem} {part_of_elem} True\n')
			else:
			 	part_of_elem = elem[0 : random.randint(1, len(elem)-1)]
			 	write_file.write(f'{elem} {part_of_elem} False\n')
			print(part_of_elem, elem)

	write_file.close()
	read_file.close()

def test_for_Move_zeros(file_write, num = 3000):
	open(file_write, 'w').close()
	my_file = open(file_write, 'w', encoding='UTF-8')

	lst = list()

	for a in range(num+1):
		lst.clear()
		for i in range(random.randint(1, 30)):
			lst.append(random.randint(0, 5))

		lst_zero = [x for x in lst if x != 0 or x is False]+[x for x in lst if x == 0 and not(x is False)]
		my_file.write(f'{str(lst)} {str(lst_zero)}\n')
	pass


def main():
	test_for_String_ends_with('test_source/test_for_String_ends_with.txt','test_source/test_to_generete.txt')
	test_for_Move_zeros('test_source/test_for_Move_zeros.txt')
	
if __name__ == '__main__':
	#main()
	test_for_Move_zeros('test_source/test_for_Move_zeros.txt')









