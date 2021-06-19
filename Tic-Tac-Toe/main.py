import random
import os



def g_name(male = True):
	file = open('name.txt','r',encoding='UTF-8')
	m_lst = list()
	f_lst = list()

	m_lst_p = list()
	f_lst_p = list()

	for i in file:
		lst = i[:-1].split(' ')
		if lst[1] == 'M':
			m_lst.append(lst[0])
			m_lst_p.append(lst[2])
		else:
			f_lst.append(lst[0])
			f_lst_p.append(lst[3])
	if male:
		print(f'{random.choice(m_lst)} {random.choice(m_lst_p)}')
	else:
		print(f'{random.choice(f_lst)} {random.choice(f_lst_p)}')


def main():
	dzender = os.environ['APPWRITE_FUNCTION_DATA']
	g_name(dzender == 'male')

if __name__ == '__main__':
	main()

