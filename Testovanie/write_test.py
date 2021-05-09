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

def main():
	test_for_String_ends_with('test_source/test_file.txt','test_source/test_to_generete.txt')
	
if __name__ == '__main__':
	main()