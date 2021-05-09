from main import string_ends_with

def test_string_ends_with(file_path):
	my_file = open(file_path,'r',encoding = 'UTF-*')
	passed = 0 
	lenght = 0
	for i in my_file:
		string, ending, expectations = i[:-1].split()
		if string_ends_with(string, ending) == bool(expectations):
			print(f'Test passed for string: {string}.')
			passed += 1
		else:
			print(f'Test failed for string: {string}.')

		lenght += 1

	print('-'*30,f'\nPassed tests {passed} from {lenght}')

		
		

def main():
	test_string_ends_with('test_source/test_file.txt')

if __name__ == '__main__':
	main()


