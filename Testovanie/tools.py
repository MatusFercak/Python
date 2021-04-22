def hello():
    name = input("Type your name: ")
    print("Hello, {}!".format(name))


def power():
    i = float(input("Type num: "))
    result = i**2
    print(type(i))
    print("mocnina {}".format(round(result, 3)))
    # metoda ktora zaokruhluje {:."pocet miest"+typ}
    print("mocnina {:.3f}".format(result))


def odd():
    num = int(input("Type a number: "))
   # if not num % 2:
    if num % 2 == 0:
        print("{} is odd number.".format(num))
    else:
        print("{} is not odd number.".format(num))


def divider():
    num_1 = int(input("Enter int 1th : "))
    num_2 = int(input("Enter int 2th : "))
    for i in range(2, min(num_1, num_2)+1):
        if num_1 % i == 0 and num_2 % i == 0:
            print(i)


def prime(num_1):
    # num_1 = int(input("Enter integer: "))
    is_prime = True
    for i in range(2, num_1):
        if num_1 % i == 0:
            is_prime = False

    if not is_prime:
        print("{} is not prime!".format(num_1))
    else:
        print("{} is prime!".format(num_1))


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def get_sum_of_multiples(max_number, number):
    sum_of = 0
    for i in range(0, max_number+1, number):
        sum_of += i

    return sum_of


def is_triangel(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False


def factorial(number):
    sumary = 1
    for i in range(1, number + 1):
        sumary *= i

    return sumary


def ipv4_decimal_to_binnary(ipv4):
    oct_1, oct_2, oct_3, oct_4 = ipv4.split(".")
    return (f"{int(oct_1):0>8b}.{int(oct_2):0>8b}.{int(oct_3):0>8b}.{int(oct_4):0>8b}")





