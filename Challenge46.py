__Score_Dict__ = {}


def enter_score():
    global __Score_Dict__
    Valid = False
    while not Valid:
        Input_1 = input("Enter your name")
        if Input_1.lower() == "stop":
            Valid = True
        else:
            Input_2 = input("Enter your score")
            if len(Input_2) == 0: Input_2 = "No Score"

            __Score_Dict__[Input_1.lower()] = Input_2


def lookup_score():
    global __Score_Dict__
    User_Name = input("Who do you want to look up?")
    if User_Name.lower() in __Score_Dict__:
        print(f"User: {User_Name}, Score: {__Score_Dict__[User_Name.lower()]}")
    else:
        print("This user is not in this file.")


enter_score()
lookup_score()
