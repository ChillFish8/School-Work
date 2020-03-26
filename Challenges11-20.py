# Run using JIT Compiler 3.8


def ch11():
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    running = True
    while running:
        num = input("Enter a number between 1 and 26 ")
        if num.isdigit():
            if int(num) in range(1, 27):
                print(LETTERS[int(num) - 1])
                running = False


def ch12():
    running = True
    while running:
        num = input("Enter a number between 32 and 126 ")
        if num.isdigit():
            if int(num) in range(32, 127):
                print(chr(int(num)))
                running = False


def ch13(string: str):  # Type hints be like
    string = str(string)    # Safety first kids
    if len(string) != 2:
        return False
    else:
        if (string[0] not in ['A', 'B', 'C']) and not string[1].isdigit():
            return False
        elif int(string[1]) in range(1, 4):
            return ['A', 'B', 'C'].index(string[0]), int(string[1]) - 1
        else:
            return False


def ch14(num: int):
    if num not in range(3, 11):
        return False
    for _ in range(num):
        print('[] ' * num)
    return True


def ch15(rows=5, columns=5):
    if (rows not in range(3, 11)) or (columns not in range(3, 11)):
        return False
    for _ in range(rows):
        print('[] ' * columns)
    return True


def ch16(string: str):
    text, export = "", []
    for letter in string:
        if letter != " ":
            text += letter
        else:
            export.append(text)
            text = ""
    else:
        export.append(text)
    return export


def ch17(string: str):
    string = string.lower()
    return string == string[::-1]


class Ch18:
    """ No idea why i chose todo this instead of a normal func """
    @classmethod
    def count_letters(cls, letter, string):
        count = 0
        for cha in string:
            if cha == letter:
                count += 1
        return count

    @classmethod
    def ch18(cls):
        text = ""
        while len(text) < 20:
            text = input("Enter a string ").lower()
        letter = ""
        while not letter.isalpha():
            letter = input("Enter a letter to count ")
        print(f"Letter {letter.lower()} appears; {cls.count_letters(letter.lower(), text)}")


class Ch19:
    @classmethod
    def is_float(cls, o_):
        if o_.count('.') != 1:
            return False
        else:
            content = o_.split('.')
            return content[0].isdigit() and content[1].isdigit()


class Ch20:
    @classmethod
    def c_to_f(cls, temp):
        if not isinstance(temp, int):
            return -999
        else:
            return (temp * 9/5) + 32

    @classmethod
    def f_to_c(cls, temp):
        if not isinstance(temp, int):
            return -999
        else:
            return 9/5 * (temp - 32)
