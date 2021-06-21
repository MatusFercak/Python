def user_write(email):
    file = open(f'/Users/user/Desktop/GIT/Login/{email}.txt', 'a+')
    note = input('Type your note: ')

    file.write(note + '\n')
    file.close()
    return


def user_read(email):
    file = open(f'/Users/user/Desktop/GIT/Login/{email}.txt', 'r+')
    for i in file:
        print(i[:-1])
    return


def reg_user():
    file = open('/Users/user/Desktop/GIT/Login/users.txt', 'r+')
    users = [i[:-1].split(', ') for i in file]

    print('Registration')
    name = input('Name: ')
    email = input('Email: ')
    password = input('Password: ')

    for i in users:
        if i[1] == email:
            print('\nAllready exist!')
            return

    file.write(f'{name}, {email}, {password}\n')
    print('\nSuccessfuly registed!')
    log_user()
    file.close()


def log_user():
    file = open('/Users/user/Desktop/GIT/Login/users.txt', 'r+')
    users = [i[:-1].split(', ') for i in file]

    print('Login')
    email = input('Email: ')
    password = input('Password: ')

    for i in users:
        if i[1] == email:
            if i[2] == password:
                print(f'Welcome {i[0]}!')
                print('1 - Write\n2 - Read\n3 - End')
                choose = int(input('Choose your option: '))
                if choose == 1:
                    user_write(email)
                elif choose == 2:
                    user_read(email)
                return
            else:
                print('Wrong password!')
                return
    print('With this email, you are not registred!')
    return


def main():
    end = True
    while end:
        print('Welcom to Testbook\n')
        print('1 - Login\n2 - Registration\n3 - End\n')
        choose = int(input('Choose your option: '))
        if choose == 1:
            log_user()
        elif choose == 2:
            reg_user()
        elif choose == 3:
            end = False
    pass


if __name__ == '__main__':
    main()
