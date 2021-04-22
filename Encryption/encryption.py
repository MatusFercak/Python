import sys

def check(leng, arguments):
	if arguments[1] in ['-s', '-d'] and arguments[2] == '-p' and leng == 5:
		if arguments[4][-4:] == '.txt':
			if arguments[1] == '-s':
				sifrovanie(arguments[3], arguments[4])
			elif arguments[1] == '-d':
				desifrovanie(arguments[3], arguments[4])
		else:
			print('chyba')
	else:
		print('chyba')

def sifrovanie(key, file):
	decrypted = b'abcdefghijklmnopqrstuvwxyz '
	encrypted = key_gen(key)

	encrypt_table = bytes.maketrans(decrypted, encrypted)
	decrypt_table = bytes.maketrans(encrypted, decrypted)
	
	try:		
		my_file = open(file, 'r').readlines()
		if len(my_file) > 0: 
			for i in my_file:
				print(i[:-1].translate(encrypt_table))
		else:
			print('Chyba')
	except IOError:
		print('Chyba')


def desifrovanie(key, file):
	decrypted = b'abcdefghijklmnopqrstuvwxyz '
	encrypted = key_gen(key)

	encrypt_table = bytes.maketrans(decrypted, encrypted)
	decrypt_table = bytes.maketrans(encrypted, decrypted)

	try:		
		my_file = open(file, 'r').readlines()
		if len(my_file) > 0: 
			for i in my_file:
				print(i[:-1].translate(decrypt_table))
			
		else:
			print('Chyba')
	except IOError:
		print('Chyba')

def key_gen(s):
	alpa = 'abcdefghijklmnopqrstuvwxyz'
	lst_abc = [i for i in alpa if i not in s]
	idk = ''
	lst_key = [i for i in s]
	for a in lst_key:
		if a not in idk:
			idk += a
	
	i = 26 / len(idk)
	index = 0
	key = ''
	tets = 0
	for x in range(26):
		tets += round(i)
		if x % round(i) == 0 and index < len(idk):
			key += idk[index]
			index += 1
		else:
			if x % 2 == 0:
				key += lst_abc.pop(-1)
			else:
				key += lst_abc.pop(0)

	key += '$'
	return key.encode()


if __name__ == '__main__':
	check(len(sys.argv), list(sys.argv))
	pass





