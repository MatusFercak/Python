class cvicenie_a:
    def hello(self):
        name = input("Type your name: ")
        print("Hello, {}!".format(name))

    def power(self):
        i = float(input("Type num: "))
        result = i ** 2
        print(type(i))
        print("mocnina {}".format(round(result, 3)))
        # metoda ktora zaokruhluje {:."pocet miest"+typ}
        print("mocnina {:.3f}".format(result))

    def odd(self):
        num = int(input("Type a number: "))
        # if not num % 2:
        if num % 2 == 0:
            print("{} is odd number.".format(num))
        else:
            print("{} is not odd number.".format(num))

    def divider(self):
        num_1 = int(input("Enter int 1th : "))
        num_2 = int(input("Enter int 2th : "))
        for i in range(2, min(num_1, num_2) + 1):
            if num_1 % i == 0 and num_2 % i == 0:
                print(i)

    def prime(self, num_1):
        # num_1 = int(input("Enter integer: "))
        is_prime = True
        for i in range(2, num_1):
            if num_1 % i == 0:
                is_prime = False

        if not is_prime:
            print("{} is not prime!".format(num_1))
        else:
            print("{} is prime!".format(num_1))

    def is_prime(self, number):
        for i in range(2, number):
            if number % i == 0:
                return False

        return True

    def get_sum_of_multiples(self, max_number, number):
        sum_of = 0
        for i in range(0, max_number + 1, number):
            sum_of += i

        return sum_of

    def is_triangel(self, a, b, c):
        if a + b > c and a + c > b and c + b > a:
            return True
        else:
            return False

    def factorial(self, number):
        sumary = 1
        for i in range(1, number + 1):
            sumary *= i

        return sumary




