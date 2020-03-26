# Run using JIT Compiler 3.8

import random


def ch1():
    print('Hello World!')


def ch2():
    for _ in range(10):
        print('Harri')


def ch3():
    name = input("What is your name? ")
    print(name * 15)


def ch4():
    name = input("What is your name? ")
    amount_repeats = int(input('How many times? '))
    for _ in range(amount_repeats):
        print(name)


def ch5():
    name = input("What is your name? ")
    print('Hello Harri') if name == "Harri" else print('You are not Harri')


def ch6():
    num = ""
    while not num.isdigit():
        num = input('Enter a number')


def ch7():
    return random.randint(1, 6)


def ch8(amount, sides):
    return [random.randint(1, sides) for _ in range(amount)]


def ch9():
    while True:
        num = input('Enter a number')
        try:
            if int(num) < 0:
                return
        except ValueError:
            pass


def ch10():
    numbers = []
    while True:
        num = input('Enter a number')
        try:
            if int(num) < 0:
                if len(numbers) > 0:
                    numbers.sort()
                    return numbers[::-1][0], numbers[0]
                else:
                    return -1
            numbers.append(int(num))
        except ValueError:
            pass



