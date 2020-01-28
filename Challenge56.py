import random

__Cards__ = []
__Card_Numbers__ = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
__Card_House__ = ['Heart', 'CLUB', 'DIAMOND', 'SPADE']


def generate_cards():
    global __Cards__
    __Cards__ = []
    for points in range(len(__Card_Numbers__)):
        for signs in range(len(__Card_House__)):
            __Cards__.append(f"{__Card_Numbers__[points]} Of { __Card_House__[signs]}")


def get_cards():
    global __Cards__
    generate_cards()
    amount_ = input("How many cards do you want?")
    if amount_.isdigit():
        random.shuffle(__Cards__)
        for i in range(int(amount_)):
            print(random.choice(__Cards__))  # could just do __card__[i] but want eXtRA sHuFfLeS
    else:
        get_cards()


get_cards()
