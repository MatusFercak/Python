def registracia(username, password):
    register_file = open('register.txt', 'a')
        
    check = True
    lst = list()
    for i in open('register.txt', 'r').readlines():
        user_n, pass_w = i[:-1].split(' : ')
        print(user_n ,pass_w)
        if username == user_n:
            check = False

    if check:
        print('+++Nexistuje+++')
        register_file.write('{} : {} \n'.format(username, password))
    if not check:
        print('---Existuje---')
    
    register_file.close() 

def validacia(meno=str(), heslo=int()):
    register_file = open('register.txt', 'r')
    for i in open('register.txt', 'r').readlines():
        user_n, pass_w = i[:-1].split(' : ')
        if meno == user_n and heslo == pass_w:
            print('Pristup povoleny')
            register_file.close()
            return None
    
    print('Pristup zamietnuty')
    register_file.close()
    


if __name__ == '__main__':

    registracia('Meno', 'heslo')
    validacia('Meno', 'heslo')
